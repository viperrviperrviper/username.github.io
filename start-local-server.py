from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import socket
import webbrowser


ROOT = Path(__file__).resolve().parent
HOST = "127.0.0.1"
START_PORT = 4173


def free_port(start):
    port = start
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            if sock.connect_ex((HOST, port)) != 0:
                return port
        port += 1


def main():
    port = free_port(START_PORT)
    handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT))
    url = f"http://{HOST}:{port}/index.html"

    print("Kart Sekai local server")
    print()
    print(f"Folder: {ROOT}")
    print(f"Open:   {url}")
    print()
    print("Keep this window open while using the site.")
    print("Press Ctrl+C to stop the server.")
    print()

    webbrowser.open(url)
    ThreadingHTTPServer((HOST, port), handler).serve_forever()


if __name__ == "__main__":
    main()
