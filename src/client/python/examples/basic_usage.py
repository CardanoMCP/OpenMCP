from openmcp_cardano import OpenMCPCardanoClient


if __name__ == "__main__":
    client = OpenMCPCardanoClient()
    print(client.health()) 