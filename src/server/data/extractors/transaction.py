def extract_transaction(raw: dict) -> dict:
    return {"hash": raw.get("tx_hash"), "inputs": [], "outputs": []} 