#!/usr/bin/env python3
"""Serve this binary clock project locally with Python.

Usage:
    python app.py

Then open http://localhost:8000/index.html
"""

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os
import webbrowser
import sys

PORT = int(os.environ.get("PORT", 8000))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class BinaryClockHandler(SimpleHTTPRequestHandler):
    """Serve files from the project root directory."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT_DIR, **kwargs)


def run_server(port: int = PORT) -> None:
    address = ("", port)
    with TCPServer(address, BinaryClockHandler) as httpd:
        url = f"http://localhost:{port}/index.html"
        print(f"Serving Binary Clock at: {url}")
        print("Press Ctrl+C to stop.")
        try:
            webbrowser.open(url)
        except Exception:
            pass
        httpd.serve_forever()


if __name__ == "__main__":
    try:
        run_server()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)
