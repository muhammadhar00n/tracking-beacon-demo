# beacon_server.py — safe demo server
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)
        print("---- Beacon received ----")
        print("Path:", parsed.path)
        print("Query:", qs)
        print("Client:", self.client_address)
        print("-------------------------")
        # Reply OK
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

if __name__ == "__main__":
    HOST = "0.0.0.0"   # listen on all interfaces
    PORT = 8080
    print(f"Listening on http://{HOST}:{PORT} — Ctrl+C to stop")
    HTTPServer((HOST, PORT), Handler).serve_forever()
