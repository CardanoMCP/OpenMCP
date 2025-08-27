def test_cardano_connectors_exist():
    from src.server.data.connectors.cardano_db_sync import CardanoDBSyncConnector
    from src.server.data.connectors.blockfrost import BlockfrostConnector
    from src.server.data.connectors.maestro import MaestroConnector

    assert CardanoDBSyncConnector
    assert BlockfrostConnector
    assert MaestroConnector 