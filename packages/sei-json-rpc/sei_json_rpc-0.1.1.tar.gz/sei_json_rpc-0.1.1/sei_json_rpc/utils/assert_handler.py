from web3 import Web3
from eth_utils import to_checksum_address


# 转换地址为校验和格式
def _addr(addr):
    return to_checksum_address(addr) if addr else None


def assert_transaction_receipt(w3: Web3, tx_receipt, txn_params, from_address=None):
    """
    交易回执断言验证

    参数：
    tx_receipt: 交易收据对象（AttributeDict）
    txn_params: 原始交易参数（dict）
    from_address: 可选，发送方地址的校验（如果不在txn_params中）
    """
    assert len(tx_receipt) == 14, "交易收据字段数量错误"
    try:
        # 1. 交易状态断言
        assert 'status' in tx_receipt, "交易收据缺少状态字段"
        assert tx_receipt.status == 1, f"交易执行失败，状态码：{tx_receipt.status}"

        # 2. 地址系统验证
        sender = _addr(tx_receipt['from'])
        recipient = _addr(tx_receipt['to'])
        expected_recipient = _addr(txn_params.get('to'))

        # 发送方验证
        if from_address:
            expected_sender = _addr(from_address)
            assert sender == expected_sender, \
                f"发送方地址不匹配，预期：{expected_sender}，实际：{sender}"

        # 接收方验证
        assert recipient == expected_recipient, \
            f"接收方地址不匹配，预期：{expected_recipient}，实际：{recipient}"

        # 3. Gas 消耗安全验证
        gas_used = tx_receipt['gasUsed']
        gas_limit = txn_params['gas']
        assert gas_used <= gas_limit, \
            f"Gas 超限：使用 {gas_used}，限制 {gas_limit}"

        # 4. 费用验证（EIP-1559 专属）
        if tx_receipt['type'] == 2:
            actual_price = tx_receipt['effectiveGasPrice']  # 为每单位燃料支付的基础费和小费的总和
            max_priority = txn_params['maxPriorityFeePerGas']  # 交易中的最大优先级费用
            max_fee = txn_params['maxFeePerGas']  # 交易中的最大费用

            # # 优先级费用验证,预计cosmos的链，只有总费用的验证
            # assert actual_price == max_priority, \
            #     f"实际费用 {actual_price} 低于优先费 {max_priority}"

            # 总费用上限验证
            assert actual_price == max_fee, \
                f"实际费用 {actual_price} 超过最大费用 {max_fee}"

            # 基础费用合理性验证
            base_fee = txn_params['maxPriorityFeePerGas']
            assert actual_price == base_fee + max_priority, \
                f"费用计算错误，预期 {base_fee + max_priority}，实际 {actual_price}"

        # 5. Nonce 序列验证
        actual_nonce = w3.eth.get_transaction_count(from_address or sender)
        expected_nonce = txn_params['nonce'] + 1
        assert actual_nonce == expected_nonce, \
            f"Nonce 序列错误，预期：{expected_nonce}，实际：{actual_nonce}"

        # 6. 合约创建特殊检查
        if not expected_recipient and 'contractAddress' in tx_receipt:
            assert w3.is_address(tx_receipt['contractAddress']), \
                "合约地址无效"

    except AssertionError as e:
        # 生成详细错误报告
        error_report = (
            f"交易验证失败：{str(e)}\n"
            f"交易哈希：{tx_receipt.transactionHash.hex()}\n"
            f"区块：{tx_receipt.blockNumber}（{tx_receipt.blockHash.hex()}）\n"
            f"发送方：{sender}\n接收方：{recipient}\n"
            f"Gas 使用：{gas_used}/{gas_limit}\n"
            f"实际费用：{actual_price} "
        )
        raise AssertionError(error_report) from e


def assert_transaction(w3: Web3, tx_receipt, tx_type=0, txn_params=None):
    assert tx_receipt.get("type") == tx_type, "交易类型不匹配"
    if tx_type == 0:
        assert len(tx_receipt) == 16, "交易字段数量错误"

    if tx_type == 2:
        assert len(tx_receipt) == 20, "交易字段数量错误"
        y_parity = tx_receipt.get('yParity')
        assert y_parity in (0, 1), f"无效的 yParity 值： {y_parity} "

    assert tx_receipt.get('hash') is not None, "缺少交易哈希"
    assert tx_receipt.get("blockHash") is not None, "缺少区块哈希"
    assert tx_receipt.get("blockNumber") is not None, "缺少区块编号"

    # 签名要素验证
    v = tx_receipt.get('v')
    r = tx_receipt.get('r')
    s = tx_receipt.get('s')

    assert v is not None and r is not None and s is not None, "缺少签名要素"

    pass
