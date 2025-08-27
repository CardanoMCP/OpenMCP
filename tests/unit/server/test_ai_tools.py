def test_validate_address():
    from src.server.ai.tools.validator import validate_address

    assert validate_address("addr1...") is True
    assert validate_address(123) is False 