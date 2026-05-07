from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse
from db import get_original_url, save_url
from shortener import check_short_code
import os
from dotenv import load_dotenv
load_dotenv()

class URLShortenerHandler(BaseHTTPRequestHandler):
    def send_json_response(self, status_code, data):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        json_data = json.dumps(data)
        json_data = json_data.encode('utf-8')
        self.wfile.write(json_data)
        return None
    

    def do_POST(self):
        if self.path != "/shorten":
            self.send_json_response(404, {"error": "Not Found"})
            return
        
        try:
            content_length = int(self.headers.get("Content-Length"))
            raw_body = self.rfile.read(content_length)
            body = json.loads(raw_body)
            original_url = body.get("original_url")

            if not original_url:
                self.send_json_response(400, {"error": "original_url is required"})
                return

            short_code = check_short_code()
            save_url(original_url, short_code)
            base_url = os.getenv("BASE_URL", "http://localhost:8080")
            short_url = base_url + "/" + short_code
            self.send_json_response(200, {"short_url": short_url})

        except json.JSONDecodeError:
            self.send_json_response(400, {"error": "Invalid JSON"})
        except Exception as e:
            self.send_json_response(500, {"error": str(e)})


    def do_GET(self):
        short_code = self.path[1:]
        
        if not short_code:
            self.send_json_response(200, {"message": "Welcome to URL Shortener"})
            return
        
        try:
            original_url = get_original_url(short_code)
            
            if original_url:
                self.send_response(301)
                self.send_header("Location", original_url)
                self.end_headers()
            else:
                self.send_json_response(404, {"error": "Short code not found"})
        
        except Exception as e:
            self.send_json_response(500, {"error": str(e)})