from dataclasses import dataclass
import os


@dataclass
class CardanoConfig:
    blockfrost_api_key: str = os.getenv("BLOCKFROST_API_KEY", "")
    maestro_api_key: str = os.getenv("MAESTRO_API_KEY", "")
    dbsync_dsn: str = os.getenv("DBSYNC_DSN", "")


cardano_config = CardanoConfig() 