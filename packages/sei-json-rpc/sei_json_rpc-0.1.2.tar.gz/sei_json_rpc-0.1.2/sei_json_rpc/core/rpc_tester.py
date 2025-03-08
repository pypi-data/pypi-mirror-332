import json
from typing import List, Optional, Any

from eth_account import Account
from loguru import logger
from web3 import Web3
import yaml

from sei_json_rpc.core.models import RPCResult


class RPCTester:
    def __init__(self, client: Web3):
        self.client: Web3 = client

    def _call_eth_method(self, client: Web3, method_name: str, *args, **kwargs) -> Any:
        """统一调用 eth 模块下的方法或属性"""
        eth_module = client.eth
        try:
            # 动态获取属性/方法
            attr = getattr(eth_module, method_name)

            if callable(attr):
                # 处理方法调用
                return attr(*args, **kwargs)
            else:
                # 处理属性访问
                return attr
        except Exception as e:
            return f"ERROR: {str(e)}"

    def execute(
            self,
            method_name: str,
            *args,
            **kwargs
    ) -> RPCResult:
        """通用执行方法"""
        try:
            result = self._call_eth_method(
                self.client, method_name, *args, **kwargs)
            serialized = self._serialize(result)
        except Exception as e:
            serialized = f"ERROR: {str(e)}"

        return RPCResult(
            url=str(self.client.provider),
            method=method_name,
            result=serialized
        )

    def _serialize(self, data: Any) -> str:
        """处理序列化"""
        if isinstance(data, bytes):
            return data.hex()
        if isinstance(data, (dict, list)):
            try:
                return json.dumps(data, default=str)
            except:
                pass
        return data

    def load_cases(self, config_path):
        with open(config_path) as f:
            config = yaml.safe_load(f)
            return config['test_cases']

    def tx_legacy(self, from_pk: str, to_address: str, amount: int) -> Any:
        admin = Account.from_key(from_pk)
        from_addr_balance = self.client.eth.get_balance(admin.address)
        if from_addr_balance < 1:
            raise ValueError("账户余额不足")

        legacy_tx = {
            'to': to_address,
            'value': amount,
            'gasPrice': self.client.eth.gas_price,
            'nonce': self.client.eth.get_transaction_count(admin.address),
            'chainId': self.client.eth.chain_id,
        }
        legacy_tx['gas'] = self.client.eth.estimate_gas(legacy_tx)
        signed_tx = self.client.eth.account.sign_transaction(legacy_tx, admin.key, )
        tx_bytes = self.client.eth.send_raw_transaction(signed_tx.raw_transaction)
        tx_receipt = self.client.eth.wait_for_transaction_receipt(tx_bytes)
        logger.info(f"Number:{tx_receipt.blockNumber}, transactionHash:0x{tx_receipt.transactionHash.hex()}")
        return tx_receipt