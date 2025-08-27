from .base import BaseResource


class WalletResource(BaseResource):
    def balance(self, address: str) -> dict:
        return {"address": address, "balance": "0"} 