class MaestroConnector:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_utxos(self, address: str) -> list[dict]:
        return [] 