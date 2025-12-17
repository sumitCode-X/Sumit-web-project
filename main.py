#!/usr/bin/env python3
"""
main.py
Simple server entrypoint intended for VPS deployment.
Defaults to listening on 0.0.0.0:14365 (adjustable via CLI args or env vars).
This script serves the current project directory with a threaded HTTP server.
"""
import os
import argparse
from http.server import SimpleHTTPRequestHandler
from socketserver import ThreadingTCPServer

DEFAULT_HOST = os.environ.get('HOST', '0.0.0.0')
DEFAULT_PORT = int(os.environ.get('PORT', '14365'))


def run(host: str, port: int):
    web_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(web_dir)

    handler = SimpleHTTPRequestHandler
    with ThreadingTCPServer((host, port), handler) as httpd:
        httpd.allow_reuse_address = True
        print(f"Serving {web_dir}")
        print(f"Listening on http://{host}:{port}/index.html")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nStopped by user')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start simple threaded HTTP server (VPS).')
    parser.add_argument('--host', '-H', default=DEFAULT_HOST, help='Host/IP to bind to (default from HOST env or 0.0.0.0)')
    parser.add_argument('--port', '-p', type=int, default=DEFAULT_PORT, help='Port to listen on (default from PORT env or 14365)')
    args = parser.parse_args()
    run(args.host, args.port)
