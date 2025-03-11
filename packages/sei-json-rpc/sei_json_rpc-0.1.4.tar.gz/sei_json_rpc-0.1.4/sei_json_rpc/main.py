import sys
import pytest
from loguru import logger
from pathlib import Path

logger.add("logs/case_{time}.log", rotation="500MB")

def get_test_path():
    try:
        # 使用相对路径获取测试文件位置
        current_dir = Path(__file__).parent
        test_file = current_dir / 'tests' / 'test_query_rpc.py'
        if not test_file.exists():
            raise FileNotFoundError(f"Test file not found at {test_file}")
        return str(test_file)
    except Exception as e:
        logger.error(f"Failed to locate test file: {e}")
        return None

def main():
    test_path = get_test_path()
    if not test_path:
        logger.error("Cannot find test file in package")
        sys.exit(1)

    test_args = [test_path, '-v']

    # 添加其他pytest参数
    if len(sys.argv) > 1:
        test_args.extend(sys.argv[1:])

    # 执行测试并获取结果
    exit_code = pytest.main(test_args)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
