import anvil.server

from anvil_handler import AnvilHandler


def main():
    AnvilHandler()
    anvil.server.wait_forever()


if __name__ == "__main__":
    main()
