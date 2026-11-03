#!/usr/bin/env python3
"""Local-only HTTP training server for basic proxy/scanner exercises."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from html import escape

HOST = "127.0.0.1"
PORT = 8000

class Handler(BaseHTTPRequestHandler):
    server_version = "CodomaxTrainingHTTP/1.0"

    def send_page(self, status, body, content_type="text/html; charset=utf-8"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body.encode("utf-8"))))
        # Deliberately minimal headers for learning; not intended for production.
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/":
            body = """<!doctype html><html><head><title>Local Security Training Lab</title></head>
<body><h1>Codomax Local Training Lab</h1>
<p>This service is bound to 127.0.0.1 only.</p>
<ul><li><a href='/hello'>Hello</a></li><li><a href='/health'>Health</a></li>
<li><a href='/search?q=training'>Search demo</a></li></ul></body></html>"""
            self.send_page(200, body)
        elif parsed.path == "/hello":
            self.send_page(200, "<html><body><h1>Hello from the local lab</h1></body></html>")
        elif parsed.path == "/health":
            self.send_page(200, "OK\n", "text/plain; charset=utf-8")
        elif parsed.path == "/search":
            q = parse_qs(parsed.query).get("q", [""])[0]
            body = "<html><body><h1>Search demo</h1><p>Query: " + escape(q) + "</p></body></html>"
            self.send_page(200, body)
        else:
            self.send_page(404, "<html><body><h1>Not found</h1></body></html>")

    def log_message(self, fmt, *args):
        print("[HTTP] " + (fmt % args))

if __name__ == "__main__":
    print(f"Training app listening at http://{HOST}:{PORT}")
    print("Local-only demo. Press Ctrl+C to stop.")
    HTTPServer((HOST, PORT), Handler).serve_forever()
