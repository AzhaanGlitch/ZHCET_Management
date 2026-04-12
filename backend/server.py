import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import urllib.parse

import database

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    def do_POST(self):
        if self.path == '/api/login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            body = json.loads(post_data.decode('utf-8'))
            
            role = body.get("role")
            identifier = body.get("identifier")
            password = body.get("password")
            
            user = database.login(role, identifier, password)
            if user:
                self._set_headers(200)
                sanitized_user = {k: v for k, v in user.items() if k != "password_hash"}
                res = {"success": True, "user": sanitized_user, "role": role}
                self.wfile.write(json.dumps(res).encode('utf-8'))
            else:
                self._set_headers(401)
                self.wfile.write(json.dumps({"success": False, "message": "Invalid credentials"}).encode('utf-8'))
        elif self.path.startswith('/api/'):
            # Handling Creates
            table = self.path.split('/')[-1]
            content_length = int(self.headers['Content-Length'])
            body = json.loads(self.rfile.read(content_length).decode('utf-8'))
            record = database.create_record(table, body)
            self._set_headers(201)
            self.wfile.write(json.dumps({"success": True, "data": record}).encode('utf-8'))
        else:
            self._set_headers(404)
            self.wfile.write(b'{"error": "Not found"}')


    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path.startswith('/api/all/'):
            table = parsed.path.split('/')[-1]
            data = database.get_all(table)
            
            # Remove password_hash from response
            cleaned_data = []
            for item in data:
                c_item = dict(item)
                c_item.pop('password_hash', None)
                cleaned_data.append(c_item)
                
            self._set_headers(200)
            self.wfile.write(json.dumps({"data": cleaned_data}).encode('utf-8'))
        else:
             self._set_headers(404)
             self.wfile.write(b'{"error": "Not found"}')
             
    def do_PUT(self):
        if self.path.startswith('/api/update/'):
            parts = self.path.split('/')
            table = parts[3]
            id_col = parts[4]
            id_val = parts[5]
            
            content_length = int(self.headers['Content-Length'])
            body = json.loads(self.rfile.read(content_length).decode('utf-8'))
            
            updated = database.update_record(table, id_col, id_val, body)
            if updated:
                self._set_headers(200)
                self.wfile.write(json.dumps({"success": True, "data": updated}).encode('utf-8'))
            else:
                self._set_headers(404)
                self.wfile.write(b'{"error": "Not found"}')
                
    def do_DELETE(self):
        if self.path.startswith('/api/delete/'):
            parts = self.path.split('/')
            table = parts[3]
            id_col = parts[4]
            id_val = parts[5]
            
            deleted = database.delete_record(table, id_col, id_val)
            if deleted:
                self._set_headers(200)
                self.wfile.write(json.dumps({"success": True}).encode('utf-8'))
            else:
                self._set_headers(404)
                self.wfile.write(b'{"error": "Not found"}')

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting API server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
