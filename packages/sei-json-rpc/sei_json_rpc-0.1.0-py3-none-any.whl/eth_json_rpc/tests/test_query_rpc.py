import sys
import os
import csv
from typing import TypedDict

from loguru import logger
import pytest
from web3 import Web3

from core.client_manager import ClientPool
from core.models import RPCResult
from core.rpc_tester import RPCTester
from utils.compile import compile_solidity_contract

get_balance_cases = "./cases/sei/get_balance.yml"
get_transaction_receipt_cases = "./cases/sei/get_transaction_receipt.yml"
get_transaction_by_block_number_cases = "./cases/sei/get_transaction_by_block_number.yml"

get_block_cases = "./cases/sei/get_block.yml"
get_block_receipts_cases = "./cases/sei/get_block_receipts.yml"
get_code_cases = "./cases/sei/get_code.yml"
get_proof_cases = "./cases/sei/get_proof.yml"
get_storage_at_cases = "./cases/sei/get_storage_at.yml"
get_transaction_by_count_cases = "./cases/sei/get_transaction_by_count.yml"

logger.add("logs/case_{time}.log", rotation="500MB")

contracts_file_path = "./tests/contract/SimpleStorage.sol"
erc20_file_path = "./tests/contract/ERC20.sol"

from_pk = os.getenv("ETH_PK")
if not from_pk:
    raise RuntimeError("Not get PrivateKey from env")
to_address = "0x863221244596659aE10C4383021b4Da3ACe907C1"


def test_get_balance(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    test_cases = sei_tester.load_cases(get_balance_cases)
    for case in test_cases:
        method_name = case["method_name"]
        params = case.get("params", [])  # 默认为空列表
        kwargs = case.get("kwargs", {})  # 默认为空字典
        logger.info(f"{method_name} - {case["description"]}")
        logger.info(f"params:{params}, kwargs: {kwargs}")

        resp: RPCResult = sei_tester.execute(method_name, *params, **kwargs)
        logger.info(f"resp:{resp}")
        if case.get("expected_error"):
            assert case.get("expected_error") in resp.result

        if case.get("expected_result"):
            assert case.get("expected_result") == resp.result


def test_get_transaction_receipt(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    test_cases = sei_tester.load_cases(get_transaction_receipt_cases)
    for case in test_cases:
        method_name = case["method_name"]
        params = case.get("params", [])  # 默认为空列表
        kwargs = case.get("kwargs", {})  # 默认为空字典
        logger.info(f"{method_name} - {case["description"]}")
        logger.info(f"params:{params}, kwargs: {kwargs}")

        resp: RPCResult = sei_tester.execute(method_name, *params, **kwargs)
        logger.info(f"resp:{resp}")
        expected_error = case.get("expected_error")
        if expected_error:
            assert expected_error in str(resp.result)

        expected_result = case.get("expected_result")
        if expected_result:
            assert expected_result.get("tx_hash") in str(resp.result)


def test_get_transaction_by_block(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    test_cases = sei_tester.load_cases(get_transaction_by_block_number_cases)

    block_info = w3.eth.get_block(w3.eth.get_block_number(), True)
    response = w3.eth.get_transaction_by_block(block_info.number, block_info.transactions[0].transactionIndex)
    logger.info(f"Automated test cases:{response}")
    for case in test_cases:
        method_name = case["method_name"]
        params = case.get("params", [])  # 默认为空列表
        kwargs = case.get("kwargs", {})  # 默认为空字典
        logger.info(f"{method_name} - {case["description"]}")
        logger.info(f"params:{params}, kwargs: {kwargs}")

        resp: RPCResult = sei_tester.execute(method_name, *params, **kwargs)
        logger.info(f"resp:{resp}")
        expected_error = case.get("expected_error")
        if expected_error:
            assert expected_error in str(resp.result)

        expected_result = case.get("expected_result")
        if expected_result:
            assert expected_result.get("blockNumber") in str(resp.result)
            assert expected_result.get("transactionIndex") in str(resp.result)


def test_get_transaction_by_block_hash_and_index(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    expect_block = w3.eth.get_block_number()
    block_info = w3.eth.get_block(expect_block, True)
    response = w3.eth.get_transaction_by_block(block_info.hash, block_info.transactions[0].transactionIndex)
    assert response.get("number") == expect_block


def test_get_transaction_by_hash(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    to_addr = "0x863221244596659aE10C4383021b4Da3ACe907C1"
    tx_receipt = sei_tester.tx_legacy(from_pk, to_addr, 1000000000)
    response = w3.eth.get_transaction(tx_receipt.transactionHash)
    assert response.get("hash") == tx_receipt.transactionHash


def test_get_transaction_count(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    to_addr = "0x863221244596659aE10C4383021b4Da3ACe907C1"
    nonce = w3.eth.get_transaction_count(to_addr),
    assert nonce is not None


def test_get_code(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    result = compile_solidity_contract(erc20_file_path)
    contract = w3.eth.contract(address=Web3.to_checksum_address(
        "0xB283FDB64CFe13A896Bb22B8F4157C6d3c2C43f2"), abi=result["abi"])
    code = w3.eth.get_code(contract.address)
    assert code is not None


def test_get_storage_at(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    result = compile_solidity_contract(erc20_file_path)
    contract = w3.eth.contract(address=Web3.to_checksum_address(
        "0xB283FDB64CFe13A896Bb22B8F4157C6d3c2C43f2"), abi=result["abi"])
    storage = w3.eth.get_storage_at(contract.address, 1)
    assert storage is not None


def test_get_proof(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    result = compile_solidity_contract(erc20_file_path)
    contract = w3.eth.contract(address=Web3.to_checksum_address(
        "0xB283FDB64CFe13A896Bb22B8F4157C6d3c2C43f2"), abi=result["abi"])
    proof_tuple = w3.eth.get_proof_munger(contract.address, [0, 1, 2])
    proof = w3.eth.get_proof(*proof_tuple)
    # web3.exceptions.Web3RPCError: {'code': -32000, 'message': 'cannot find EVM IAVL store'}
    assert proof is not None


def test_get_block_transaction_count_number(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    block = w3.eth.block_number
    resp = w3.eth.get_block_transaction_count(block)
    # block 中evm transactions 总数
    assert resp is not None


def test_get_block_transaction_count_hash(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    block = w3.eth.block_number
    block_info = w3.eth.get_block(block, True)
    resp = w3.eth.get_block_transaction_count(block_info.hash)
    assert resp is not None


def test_get_block_hash(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    block = w3.eth.block_number
    block_info = w3.eth.get_block(block, True)
    block_info = w3.eth.get_block(block_info.hash, True)
    assert block_info is not None


def test_get_block_number(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    block = w3.eth.block_number
    block_info = w3.eth.get_block(block, True)
    assert block_info is not None


def test_get_block_receipts(sei_tester) -> None:
    """根据区块号获取收据树"""
    w3: Web3 = sei_tester.client
    block = w3.eth.block_number
    response = w3.eth.get_block_receipts(block)
    assert response is not None


def test_block(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    block = w3.eth.block_number
    assert block is not None


def test_chain_id(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    chain_id = w3.eth.chain_id
    assert chain_id is not None


def test_fee_history(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    block = w3.eth.block_number
    resp = w3.eth.fee_history(20, block)
    assert resp is not None
    assert len(resp.get("baseFeePerGas")) == 20
    assert len(resp.get("gasUsedRatio")) == 20


def test_gas_price(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    resp = w3.eth.gas_price
    assert resp is not None and resp >= 1100000000


def test_net_version(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    logger.info(w3.net.version)
    assert w3.net.version is not None


def test_client_version(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    logger.info(w3.client_version)
    assert w3.client_version is not None


def test_new_filter(sei_tester) -> None:
    """监听合约事件"""
    w3: Web3 = sei_tester.client

    # 创建自定义事件过滤器（需定义过滤参数）
    event_filter_params = {"fromBlock": 135319720,  # 起始区块
                           "toBlock": 135319728,  # 结束区块（可设为 "latest" 持续监听）
                           "address": "0xB283FDB64CFe13A896Bb22B8F4157C6d3c2C43f2",  # 合约地址
                           "topics": ["0x" + w3.keccak(text="Mint(uint256)").hex()]}

    try:
        filter = w3.eth.filter(event_filter_params)
        filter_id = filter.filter_id
        logger.info(filter.filter_id)
    except Exception as e:
        logger.error(e)

    logs = w3.eth.get_filter_logs(filter_id)
    logger.info(logs)
    pass


def test_uninstall_filter(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    block = w3.eth.block_number
    logger.info(block)
    block_filter = w3.eth.filter("latest")
    # 轮询区块过滤器
    new_blocks = block_filter.get_new_entries()
    logger.info(f"新区块哈希: {new_blocks}", )

    try:
        w3.eth.uninstall_filter(block_filter.filter_id)
    except Exception as e:
        logger.error(e)


def test_estimate_gas(sei_tester) -> None:
    w3: Web3 = sei_tester.client
    address = "0x863221244596659aE10C4383021b4Da3ACe907C1"
    legacy_tx = {
        'to': address,
        'value': 10000,
        'gasPrice': w3.eth.gas_price,
        'nonce': w3.eth.get_transaction_count(address),
        'chainId': w3.eth.chain_id,
    }
    legacy_tx['gas'] = w3.eth.estimate_gas(legacy_tx)

    assert legacy_tx["gas"] is not None and legacy_tx["gas"] == 21000


def test_call(sei_tester) -> None:
    """
    读取合约状态 调用合约的 view 或 pure 函数（不修改链上状态）。
    例如：查询 ERC20 代币余额、获取智能合约配置参数。
    模拟交易结果 预执行一笔交易，检查其返回值或潜在错误。
    例如：在发送交易前，模拟一笔转账是否会失败（如余额不足）。
    调试合约逻辑 通过覆盖合约状态（ state_override ）测试不同条件下的合约行为。
    例如：临时修改某个地址的余额或合约存储值。
    """
    w3: Web3 = sei_tester.client

    transaction = {}
    response = w3.eth.call(transaction,  # 调用参数（必需）
                           block_identifier="latest",  # 执行调用的区块状态（默认 "latest"）
                           state_override=None,  # 临时覆盖链上状态（可选）
                           ccip_read_enabled=True,  # 是否允许链下数据读取（如 ENS/IPFS）
                           )
    assert response is not None
