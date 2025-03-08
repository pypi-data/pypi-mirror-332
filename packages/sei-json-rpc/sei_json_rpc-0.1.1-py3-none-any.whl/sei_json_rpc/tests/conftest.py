import os
import pytest
from core.client_manager import ClientPool
from core.rpc_tester import RPCTester

client_urls: list[str] = os.getenv("SEI_URL", "").split(',')
if client_urls:
    if isinstance(client_urls, str):
        client_urls = client_urls.split(',')
    # 确保所有的 URL 都被视作列表元素（处理多个URL的情况）
    client_urls = [url.strip() for url in client_urls]

if not client_urls:
    client_urls = ["https://evm-rpc.sei-apis.com"]




@pytest.fixture(scope="module")
def sei_tester():
    pool = ClientPool(client_urls)
    return RPCTester(pool[0])


@pytest.fixture(scope="module")
def eth_tester():
    pool = ClientPool(client_urls)
    return RPCTester(pool[1])
