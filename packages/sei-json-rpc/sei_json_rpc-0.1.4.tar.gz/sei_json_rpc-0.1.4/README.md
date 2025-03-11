# eth-json-rpc
EVM json-rpc endpoints

## 1.安装准备
- 申请alchemy账号,获取API_KEY,并配置环境变量
```shell
export RPC_URL="${ETH_MAIN_RPC_URL}${ETH_MAIN_APIKEY}"

# 安装依赖项
poetry install --no-root 

# 添加依赖
poetry add pytest 
```

