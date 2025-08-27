class CardanoDBSyncConnector:
    def __init__(self, dsn: str) -> None:
        self.dsn = dsn

    def fetch_transaction(self, tx_hash: str) -> dict:
        return {"tx_hash": tx_hash} 