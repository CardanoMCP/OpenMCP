def test_server_start_stop():
    from src.server.core.mcp_server import MCPServer

    s = MCPServer()
    s.start()
    assert s.started is True
    s.stop()
    assert s.started is False 