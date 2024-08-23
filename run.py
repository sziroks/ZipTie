from server import Server

def main():
    """
    Entrypoint to application. It starts the server.
    """
    try:
        server = Server()
        server.start_server()
    except KeyboardInterrupt:
        print("Server stopping")
    except Exception as e:
        print(f"Unhandled exception occured: {e}")
    finally:
        print("Server stopped")


if __name__ == "__main__":
    main()