import json
import sys
import os
import csv

import pytest
from eth_abi import abi
from eth_account import Account
from eth_account.signers.local import LocalAccount
from loguru import logger
from web3 import Web3

from sei_json_rpc.core.client_manager import ClientPool
from sei_json_rpc.core.models import RPCResult
from sei_json_rpc.core.rpc_tester import RPCTester
from sei_json_rpc.utils import assert_handler as ah
from sei_json_rpc.utils.compile import compile_solidity_contract

logger.add("logs/case_{time}.log", rotation="500MB")

contracts_file_path = "./tests/contract/SimpleStorage.sol"
erc20_file_path = "./tests/contract/ERC20.sol"

from_pk = os.getenv("ETH_PK")
if not from_pk:
    raise RuntimeError("Not get PrivateKey from env")
to_address = "0x863221244596659aE10C4383021b4Da3ACe907C1"


# base_fee = w3.eth.blob_base_fee  blob类型需要
# gas_price = w3.eth.gas_price   legacy类型需要


def test_tx_1559(sei_tester) -> None:
    admin: LocalAccount = Account.from_key(from_pk)
    w3 = sei_tester.client

    max_priority_fee = w3.eth.max_priority_fee
    base_fee = w3.eth.get_block('latest').baseFeePerGas  # 会动态改变
    from_addr_balance = w3.eth.get_balance(admin.address)
    to_addr_balance = w3.eth.get_balance(to_address)
    logger.info(f"from: {admin.address}, balance: {from_addr_balance}, \n"
                f"base_fee: {base_fee}, max_priority_fee: {max_priority_fee}")
    # 实际支付 =  min(maxFeePerGas, baseFee + maxPriorityFeePerGas)
    # 实际矿工费 = min(maxPriorityFeePerGas, maxFeePerGas - baseFee)
    txn_params = dict(
        nonce=w3.eth.get_transaction_count(admin.address),
        maxFeePerGas=base_fee + max_priority_fee,
        maxPriorityFeePerGas=max_priority_fee,
        to=to_address,
        value=1000000000,
        data=b'',
        # (optional) the type is now implicitly set based on appropriate transaction params
        type=2,
        chainId=w3.eth.chain_id,
    )
    # 预估gas
    txn_params['gas'] = w3.eth.estimate_gas(txn_params)
    logger.info(f"txn_params: {txn_params}", )

    signed_txn = w3.eth.account.sign_transaction(txn_params, admin.key, )
    tx_bytes = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
    logger.info(f"tx_bytes: {tx_bytes.hex()}")
    # transaction_receipt 中并不包含完整交易信息
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_bytes)
    logger.info(
        f"blockNumber:{tx_receipt.blockNumber}, transactionHash:0x{tx_receipt.transactionHash.hex()}")

    # 交易回执信息验证
    ah.assert_transaction_receipt(w3, tx_receipt, txn_params)

    # 交易详情信息验证
    tx = w3.eth.get_transaction(tx_receipt.get("transactionHash"))
    ah.assert_transaction(
        w3, tx, tx_type=txn_params["type"], txn_params=txn_params)

    # 业务金额验证
    fees = txn_params.get("maxFeePerGas") * txn_params["gas"]
    from_addr_balance_after = w3.eth.get_balance(admin.address)
    to_addr_balance_after = w3.eth.get_balance(to_address)
    assert from_addr_balance - from_addr_balance_after == fees + \
           txn_params["value"], "转账交易金额错误"
    assert to_addr_balance + \
           txn_params["value"] == to_addr_balance_after, "转账交易金额错误"
    pass


def test_tx_legacy(sei_tester) -> None:
    admin: LocalAccount = Account.from_key(from_pk)
    w3 = sei_tester.client

    from_addr_balance = w3.eth.get_balance(admin.address)
    to_address_balance = w3.eth.get_balance(to_address)

    # 构造交易参数
    legacy_tx = {
        'to': to_address,  # 接收地址
        'value': w3.to_wei(1, 'gwei'),  # 转账金额
        'gasPrice': w3.eth.gas_price,
        'nonce': w3.eth.get_transaction_count(admin.address),
        'chainId': w3.eth.chain_id,
    }

    # 预估gas
    legacy_tx['gas'] = w3.eth.estimate_gas(legacy_tx)
    logger.info(f"transaction: {legacy_tx}", )

    # 签名交易
    signed_tx = w3.eth.account.sign_transaction(legacy_tx, admin.key, )

    # 发送交易
    tx_bytes = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_bytes)
    logger.info(
        f"blockNumber:{tx_receipt.blockNumber}, transactionHash:0x{tx_receipt.transactionHash.hex()}")

    # 交易回执信息验证
    ah.assert_transaction_receipt(w3, tx_receipt, legacy_tx)

    # 交易详情信息验证
    tx = w3.eth.get_transaction(tx_receipt.get("transactionHash"))
    ah.assert_transaction(w3, tx, tx_type=0, txn_params=legacy_tx)

    # 业务金额验证
    fees = legacy_tx.get("gasPrice") * legacy_tx["gas"]
    from_addr_balance_after = w3.eth.get_balance(admin.address)
    to_address_balance_after = w3.eth.get_balance(to_address)
    assert from_addr_balance - from_addr_balance_after == fees + \
           legacy_tx["value"], "转账交易金额错误"
    assert to_address_balance + \
           legacy_tx["value"] == to_address_balance_after, "转账交易金额错误"

    pass


def test_access_list(sei_tester):
    # TODO
    pass


def test_4844(eth_tester) -> None:
    w3 = eth_tester.client
    admin: LocalAccount = Account.from_key(from_pk)

    from_addr_balance = w3.eth.get_balance(admin.address)
    to_address_balance = w3.eth.get_balance(to_address)

    tx_payload_body = {
        'type': 3,
        "maxFeePerGas": 2000000000,
        "maxPriorityFeePerGas": 2000000000,
        "maxFeePerBlobGas": 2000000000,
        'to': "0x0000000000000000000000000000000000000000",
        'value': 0,
        'nonce': w3.eth.get_transaction_count(admin.address),
        'chainId': w3.eth.chain_id,
    }

    # 预估gas
    tx_payload_body['gas'] = w3.eth.estimate_gas(tx_payload_body)
    logger.info(f"transaction: {tx_payload_body}", )

    # Blob 数据必须由 4096 个 32 字节字段元素组成
    text = "hello world"
    encoded_text = abi.encode(["string"], [text])
    BLOB_DATA = (b"\x00" * 32 * (4096 - len(encoded_text) // 32)
                 ) + encoded_text

    signed_tx = w3.eth.account.sign_transaction(
        tx_payload_body, admin.key, blobs=[BLOB_DATA])

    # 发送交易
    # tx_bytes = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    # tx_receipt = w3.eth.wait_for_transaction_receipt(tx_bytes)
    # logger.info(f"blockNumber:{tx_receipt.blockNumber}, transactionHash:{tx_receipt.transactionHash.hex()}")


def test_deploy_contract(sei_tester) -> None:
    admin: LocalAccount = Account.from_key(from_pk)
    w3 = sei_tester.client

    from_addr_balance = w3.eth.get_balance(admin.address)
    logger.info(f"address:{admin.address}, balance:{from_addr_balance}")

    result = compile_solidity_contract(contracts_file_path)
    logger.info(f"compile_solidity_contract:{result}")
    contract = w3.eth.contract(abi=result["abi"], bytecode=result["bytecode"])

    tx = contract.constructor().build_transaction({
        'chainId': w3.eth.chain_id,
        'from': admin.address,
        'gasPrice': w3.eth.gas_price,
        'nonce': w3.eth.get_transaction_count(admin.address),
    })
    tx['gas'] = w3.eth.estimate_gas(tx)
    logger.info(f"transaction: {tx}", )

    signed_tx = w3.eth.account.sign_transaction(tx, admin.key, )
    logger.info(f"signed_tx: {signed_tx}", )
    tx_bytes = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_bytes)
    logger.info(f"tx_receipt: {tx_receipt}")
    logger.info(f"contractAddress:{tx_receipt.contractAddress}")
    pass


def test_deploy_erc20(sei_tester) -> None:
    admin: LocalAccount = Account.from_key(from_pk)
    w3 = sei_tester.client

    from_addr_balance = w3.eth.get_balance(admin.address)
    logger.info(f"address:{admin.address}, balance:{from_addr_balance}")

    result = compile_solidity_contract(erc20_file_path)
    logger.info(f"compile_solidity_contract:{result}")
    contract = w3.eth.contract(abi=result["abi"], bytecode=result["bytecode"])

    tx = contract.constructor("Tether", "USDT").build_transaction({
        'chainId': w3.eth.chain_id,
        'from': admin.address,
        'gasPrice': w3.eth.gas_price,
        'nonce': w3.eth.get_transaction_count(admin.address),
    })
    tx['gas'] = w3.eth.estimate_gas(tx)
    logger.info(f"transaction: {tx}", )

    signed_tx = w3.eth.account.sign_transaction(tx, admin.key, )
    logger.info(f"signed_tx: {signed_tx}", )
    tx_bytes = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_bytes)
    logger.info(f"tx_receipt: {tx_receipt}")
    logger.info(f"contractAddress:{tx_receipt.contractAddress}")
    pass


def test_erc20_transfer(sei_tester) -> None:
    admin: LocalAccount = Account.from_key(from_pk)
    w3: Web3 = sei_tester.client

    from_addr_balance = w3.eth.get_balance(admin.address)

    result = compile_solidity_contract(erc20_file_path)

    contract = w3.eth.contract(address=Web3.to_checksum_address(
        "0xB283FDB64CFe13A896Bb22B8F4157C6d3c2C43f2"), abi=result["abi"])

    # 构建mint交易
    tx = contract.functions.mint(10000000000000000000).build_transaction(
        {'chainId': w3.eth.chain_id,
         'gas': 200000,
         'from': admin.address,
         'gasPrice': w3.eth.gas_price,
         'nonce': w3.eth.get_transaction_count(
             admin.address), })
    # # 签名并发送
    signed_tx = w3.eth.account.sign_transaction(tx, admin.key, )
    logger.info(f"signed_tx: {signed_tx}", )
    tx_bytes = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_bytes)
    logger.info(f"tx_receipt: {tx_receipt}")
    # tx_data = w3.eth.get_transaction("0xb68dffa3c3f2723cfa88ceb4cc66091145ddf0849a8abfe64a54b4d073baf33c")
    # logger.info(f"tx_data: {tx_data}")
    token_balance = contract.functions.balanceOf(admin.address).call()
    logger.info(f"token_balance: {token_balance}")
    total_supply = contract.functions.totalSupply().call()
    logger.info(f"Total Supply: {total_supply} ")
    assert contract.functions.name().call() == "Tether"
    assert contract.functions.symbol().call() == "USDT"
    logger.info(contract.functions.name().call())
    logger.info(contract.functions.symbol().call())
    logger.info(contract.functions.decimals().call())

    # # 构建转账交易
    # tx = contract.functions.transfer(to_address, 10).build_transaction(
    #     {'chainId': w3.eth.chain_id,
    #      'from': admin.address,
    #      'gasPrice': w3.eth.gas_price,
    #      'nonce': w3.eth.get_transaction_count(
    #          admin.address), })
    # tx['gas'] = w3.eth.estimate_gas(tx)
    # signed_tx = w3.eth.account.sign_transaction(tx, admin.key, )
    # tx_bytes = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    # tx_receipt = w3.eth.wait_for_transaction_receipt(tx_bytes)
    # logger.info(f"tx_receipt: {tx_receipt}")
    # tx_data = w3.eth.get_transaction(tx_bytes)
    # logger.info(f"tx_data: {tx_data}")


def test_call_contract(sei_tester) -> None:
    admin: LocalAccount = Account.from_key(from_pk)
    w3 = sei_tester.client

    result = compile_solidity_contract(contracts_file_path)

    tx_transaction = w3.eth.get_transaction_receipt(
        "0xbe620094f9711b551147ccbe0d174ab582e8e91c5c3c81a405e5ac4a7624f38b")
    contract_instance = w3.eth.contract(abi=result["abi"],
                                        address=tx_transaction["contractAddress"])

    # 调用 set 方法
    tx = contract_instance.functions.set(42).build_transaction(
        {"from": admin.address,
         "nonce": w3.eth.get_transaction_count(admin.address),
         "gas": 200000,
         "gasPrice": w3.eth.gas_price, })
    signed_tx = w3.eth.account.sign_transaction(tx, admin.key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("set 方法调用成功，交易哈希:", tx_receipt.transactionHash.hex())

    call = contract_instance.functions.get().call()
    print(call)

    pass


def test_get_transaction_by_block_number(sei_tester):
    w3 = sei_tester.client
    block_number = w3.eth.block_number
    tx = w3.eth.get_block_transaction_count(block_number)
    logger.info(f"Block number: {block_number}, Transaction count: {tx}")
    w3 = sei_tester.client
