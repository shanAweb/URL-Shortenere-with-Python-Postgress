import os
from http.server import HTTPServer
from dotenv import load_dotenv
from handler import URLShortenerHandler

load_dotenv()

host = os.getenv("HOST", "localhost")
port = int(os.getenv("PORT", 8080))

if __name__ == "__main__":
    server = HTTPServer((host, port), URLShortenerHandler)
    print(f"Server running on http://{host}:{port}")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("Server stopped")