class BlockfrostConnector:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_address_balance(self, address: str) -> dict:
        return {"address": address, "balance": "0"} 