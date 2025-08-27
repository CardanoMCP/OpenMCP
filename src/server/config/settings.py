from dataclasses import dataclass
import os


@dataclass
class Settings:
    environment: str = os.getenv("OPENMCP_ENV", "development")
    log_level: str = os.getenv("OPENMCP_LOG", "INFO")
    cardano_network: str = os.getenv("CARDANO_NETWORK", "mainnet")


settings = Settings() 