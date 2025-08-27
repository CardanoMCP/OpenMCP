def test_python_client_health():
    from src.client.python.openmcp_cardano.client import OpenMCPCardanoClient

    c = OpenMCPCardanoClient()
    assert c.health()["status"] == "ok" 