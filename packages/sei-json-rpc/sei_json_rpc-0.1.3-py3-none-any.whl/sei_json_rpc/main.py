import sys
import pytest
from loguru import logger

logger.add("logs/case_{time}.log", rotation="500MB")

def main():
    # 运行tests目录下的测试
    test_args = ['sei_json_rpc/tests/test_query_rpc.py', '-v']
    
    # 添加其他pytest参数
    if len(sys.argv) > 1:
        test_args.extend(sys.argv[1:])
    
    # 执行测试并获取结果
    exit_code = pytest.main(test_args)
    
    # 根据测试结果设置退出码
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
