#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class APIHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/":
            # Send a simple text response
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(
                b"Hello, this is a simple API!"
            )

        elif self.path == "/data":
            # Send JSON data
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(
                json.dumps(data).encode("utf-8")
            )

        elif self.path == "/status":
            # Check API status
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(b"OK")

        else:
            # Handle undefined endpoints
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(b"404 Not Found")


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, APIHandler)

    print("Server running on port 8000...")

    httpd.serve_forever()
