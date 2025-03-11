import os
import re

from solcx import compile_standard, install_solc


def compile_solidity_contract(file_path: str, solc_version: str = "0.8.0") -> dict:
    """
    编译 Solidity 合约并返回 ABI 和字节码，支持导入的其他合约文件。

    参数：
        file_path (str): 主 Solidity 文件的路径。
        solc_version (str): 指定 Solidity 编译器版本，默认为 "0.8.0"。

    返回：
        dict: 包含 ABI 和字节码的字典，格式如下：
            {
                "abi": [...],  # 合约的 ABI
                "bytecode": "0x..."  # 合约的字节码
            }

    异常：
        FileNotFoundError: 如果文件路径无效或文件不存在。
        solcx.exceptions.SolcError: 如果编译过程中发生错误。
    """
    try:
        # 安装指定版本的 Solidity 编译器
        install_solc(solc_version)

        # 获取主文件的绝对路径和相对目录
        base_dir = os.path.dirname(os.path.abspath(file_path))
        main_file_rel = os.path.relpath(file_path, base_dir)

        # 收集所有依赖文件
        def collect_sources(main_file: str, base_dir: str) -> dict:
            sources = {}
            stack = [main_file]

            while stack:
                current = stack.pop()
                if current in sources:
                    continue

                abs_path = os.path.join(base_dir, current)
                if not os.path.isfile(abs_path):
                    raise FileNotFoundError(f"导入的文件未找到: {abs_path}")

                with open(abs_path, "r", encoding="utf-8") as f:
                    content = f.read()

                sources[current] = {"content": content}

                # 查找所有的 import 语句
                import_regex = r'import\s+["\'](.*?)["\'];'
                imports = re.findall(import_regex, content)
                for imp in imports:
                    # 处理相对路径和绝对路径
                    if imp.startswith(".") or imp.startswith("/"):
                        imp_abs = os.path.normpath(os.path.join(os.path.dirname(abs_path), imp.lstrip(".")))
                    else:
                        imp_abs = os.path.normpath(os.path.join(os.path.dirname(abs_path), imp))

                    if not os.path.exists(imp_abs):
                        # 尝试在 base_dir 下查找
                        imp_abs = os.path.join(base_dir, imp)

                    if os.path.exists(imp_abs):
                        imp_rel = os.path.relpath(imp_abs, base_dir)
                        if imp_rel not in sources:
                            stack.append(imp_rel)
                    else:
                        raise FileNotFoundError(f"导入的文件未找到: {imp}")

            return sources

        # 收集所有源文件
        sources = collect_sources(main_file_rel, base_dir)

        # 构造编译配置
        compile_input = {
            "language": "Solidity",
            "sources": sources,
            "settings": {
                "outputSelection": {
                    "*": {
                        "*": ["abi", "evm.bytecode"]
                    }
                }
            }
        }

        # 编译合约
        compiled = compile_standard(compile_input, solc_version=solc_version)

        # 提取 ABI 和字节码
        # 假设主合约文件名与合约名称相同
        contract_name = os.path.splitext(os.path.basename(main_file_rel))[0]

        # 遍历编译结果以找到对应的合约
        for file_name, contracts in compiled.get("contracts", {}).items():
            for contract_name_in_file, contract_data in contracts.items():
                if contract_name_in_file == contract_name:
                    return {
                        "abi": contract_data["abi"],
                        "bytecode": contract_data["evm"]["bytecode"]["object"]
                    }

        # 如果未找到，尝试通过合约名称匹配
        for file_name, contracts in compiled.get("contracts", {}).items():
            for contract_name_in_file, contract_data in contracts.items():
                if contract_data.get("abi"):  # 简单检查是否有 ABI
                    # 可以根据需要进一步匹配合约名称
                    # 此处假设第一个找到的合约即为所需
                    return {
                        "abi": contract_data["abi"],
                        "bytecode": contract_data["evm"]["bytecode"]["object"]
                    }

        raise ValueError("无法找到编译后的合约 ABI 和字节码。")

    except FileNotFoundError as e:
        raise FileNotFoundError(f"文件未找到: {e.filename}") from e
    except Exception as e:
        raise RuntimeError(f"编译 Solidity 合约时发生错误: {str(e)}") from e


if __name__ == "__main__":
    # 请将此路径替换为你的主 Solidity 文件的相对或绝对路径
    file_path = "../tests/contract/ERC20.sol"
    # file_path = "../tests/contract/SimpleStorage.sol"
    try:
        result = compile_solidity_contract(file_path)
        print("ABI:")
        print(result["abi"])
        print("Bytecode:")
        print(result["bytecode"])
    except Exception as e:
        print(f"错误: {e}")
