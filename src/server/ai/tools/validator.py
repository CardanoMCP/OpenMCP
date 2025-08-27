def validate_address(address: str) -> bool:
    return isinstance(address, str) and len(address) > 0 