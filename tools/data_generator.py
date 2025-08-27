import json


def generate_transactions(n: int = 1) -> list[dict]:
    return [{"tx_hash": f"tx{i}", "inputs": [], "outputs": []} for i in range(n)]


if __name__ == "__main__":
    print(json.dumps(generate_transactions(3))) 