from server import Server


def main() -> None:
    """
    Entrypoint to the application. It starts the server.

    This function is the main entry point of the application. It initializes a server object,
    starts the server, and handles any exceptions that may occur during the server's execution.

    Parameters:
    None

    Returns:
    None
    """
    try:
        server: Server = Server()
        server.start_server()
    except KeyboardInterrupt:
        print("Server stopping")
    except Exception as e:
        print(f"Unhandled exception occurred: {e}")
    finally:
        print("Server stopped")


if __name__ == "__main__":
    main()
