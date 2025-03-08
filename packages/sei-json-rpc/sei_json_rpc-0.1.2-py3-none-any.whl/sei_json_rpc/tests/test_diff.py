import pytest
from loguru import logger

from sei_json_rpc.core.client_manager import ClientPool
from sei_json_rpc.core.models import RPCResult
from sei_json_rpc.core.rpc_tester import RPCTester

CONFIG_PATH = "./config/chains.yml"
get_balance_cases = "./cases/eth/get_balance.yml"
get_block_cases = "./cases/eth/get_block.yml"
get_block_receipts_cases = "./cases/eth/get_block_receipts.yml"
get_code_cases = "./cases/eth/get_code.yml"
get_proof_cases = "./cases/eth/get_proof.yml"
get_storage_at_cases = "./cases/eth/get_storage_at.yml"
get_transaction_by_block_cases = "./cases/eth/get_transaction_by_block.yml"
get_transaction_by_count_cases = "./cases/eth/get_transaction_by_count.yml"
get_transaction_receipt_cases = "./cases/eth/get_transaction_receipt.yml"


@pytest.fixture(scope="module")
def tester():
    client_pool = ClientPool(CONFIG_PATH)
    clients = [RPCTester(client) for client in client_pool.clients]
    methods_set = client_pool.methods
    return clients, methods_set


def test_get_balance_cases(tester):
    clients, methods_set = tester

    test_cases = clients[0].load_cases(get_balance_cases)

    # for w3 in clients:
    #     w3: RPCTester
    w3 = clients[-1]
    for case in test_cases:
        method_name = case["method_name"]
        params = case.get("params", [])  # 默认为空列表
        kwargs = case.get("kwargs", {})  # 默认为空字典
        logger.info(f"{method_name} - {case["description"]}")
        logger.info(f"params:{params}, kwargs: {kwargs}")

        resp: RPCResult = w3.execute(method_name, *params, **kwargs)
        logger.info(f"resp:{resp}")
        if case.get("expected_error"):
            assert case.get("expected_error") in resp.result

        if case.get("expected_result"):
            assert case.get("expected_result") == resp.result


def test_get_block_cases(tester):
    clients, methods_set = tester

    test_cases = clients[0].load_cases(get_block_cases)

    # for w3 in clients:
    #     w3: RPCTester
    w3 = clients[-1]
    for case in test_cases:
        method_name = case["method_name"]
        params = case.get("params", [])  # 默认为空列表
        kwargs = case.get("kwargs", {})  # 默认为空字典
        logger.info(f"{method_name} - {case["description"]}")
        logger.info(f"params:{params}, kwargs: {kwargs}")

        resp: RPCResult = w3.execute(method_name, *params, **kwargs)
        logger.info(resp)
        if case.get("expected_error"):
            assert case.get("expected_error") in resp.result

        if case.get("expected_result"):
            assert case.get("expected_result") == resp.result


def test_get_block_receipts_cases(tester):
    clients, methods_set = tester

    test_cases = clients[0].load_cases(get_block_receipts_cases)

    # for w3 in clients:
    #     w3: RPCTester
    w3 = clients[-1]
    for case in test_cases:
        method_name = case["method_name"]
        params = case.get("params", [])  # 默认为空列表
        kwargs = case.get("kwargs", {})  # 默认为空字典
        logger.info(f"{method_name} - {case["description"]}")
        logger.info(f"params:{params}, kwargs: {kwargs}")

        resp: RPCResult = w3.execute(method_name, *params, **kwargs)
        logger.info(resp)
        if case.get("expected_error"):
            assert case.get("expected_error") in resp.result

        if case.get("expected_result"):
            assert case.get("expected_result") == resp.result


def test_get_code_cases(tester):
    clients, methods_set = tester

    test_cases = clients[0].load_cases(get_code_cases)

    # for w3 in clients:
    #     w3: RPCTester
    w3 = clients[-1]
    for case in test_cases:
        method_name = case["method_name"]
        params = case.get("params", [])  # 默认为空列表
        kwargs = case.get("kwargs", {})  # 默认为空字典
        logger.info(f"{method_name} - {case["description"]}")
        logger.info(f"params:{params}, kwargs: {kwargs}")

        resp: RPCResult = w3.execute(method_name, *params, **kwargs)
        logger.info(resp)
        if case.get("expected_error"):
            assert case.get("expected_error") in resp.result

        if case.get("expected_result"):
            assert case.get("expected_result") == resp.result


# resp = tester.test_fee_history(4, 'latest', [10, 90])
# print(resp)


# [RPCResult(url='http://127.0.0.1:8545', method='fee_history', result=AttributeDict({'oldestBlock': 176142, 'reward': [[], [], [], []], 'baseFeePerGas': [1000000000, 1000000000, 1000000000, 1000000000], 'gasUsedRatio': [0.5, 0.5, 0.5, 0.5]}), timestamp=datetime.datetime(2025, 2, 27, 18, 18, 11, 275731)),
# method='fee_history', result=AttributeDict({'baseFeePerBlobGas': ['0x1ec78987', '0x214b31c7', '0x20030c8a', '0x22a07abf', '0x1ec78987'],
#                                                                       'baseFeePerGas': [676226164, 670696855, 620622107, 572141380, 643649969], 'blobGasUsedRatio': [0.8333333333333334, 0.3333333333333333, 0.8333333333333334, 0],
#                                                                       'gasUsedRatio': [0.46729312097942316, 0.2013568888888889, 0.18753463888888888, 0.9999365],
#                                                                       'oldestBlock': 21937019, 'reward': [[675566, 2000000000], [533780, 2000000000], [28389668, 2000000000], [27858620, 500000000]]}), timestamp=datetime.datetime(2025, 2, 27, 18, 18, 11, 275731))]


def test_rpc_method(tester):
    # results = tester.test_get_block_number()
    # print(results)

    # results = tester.test_gas_price()
    # print(results)
    # results = tester.test_chain_id()
    # print(results)
    # results = tester.test_net_version()
    # print(results)

    result = tester.test_client_version()
    print(result)

    pass

    # results = tester.execute(rpc_method)
    # # 保存结果到CSV
    # with open("rpc_results.csv", "a") as f:
    #     writer = csv.DictWriter(f, fieldnames=RPCResult.__annotations__.keys())
    #     if f.tell() == 0:
    #         writer.writeheader()
    #     for res in results:
    #         writer.writerow(res.to_dict())

    # # 验证结果一致性
    # unique_results = len(set([res.result for res in results]))
    # assert unique_results == 1, f"发现 {unique_results} 种不同响应"
