def test_extract_transaction():
    from src.server.data.extractors.transaction import extract_transaction

    result = extract_transaction({"tx_hash": "abc"})
    assert result["hash"] == "abc" 