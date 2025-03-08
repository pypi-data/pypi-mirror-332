from typing import List, Any

import yaml
from web3 import Web3, HTTPProvider


class ClientPool:
    def __init__(self, urls: List[str]):
        self.clients = self._load_clients(urls)

    def _load_clients(self, urls) -> list[Web3]:
        return [self._create_client(url) for url in urls]

    def _create_client(self, url: str) -> Web3:
        try:
            return Web3(HTTPProvider(url, request_kwargs={'timeout': 5}))
        except Exception as e:
            raise ValueError(f"Failed to connect to {url}: {str(e)}")

    def get_all_clients(self) -> List[Web3]:
        return self.clients

    def __getitem__(self, index):
        return self.clients[index]

    def __len__(self):
        return len(self.clients)
