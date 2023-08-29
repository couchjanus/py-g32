from http.server import HTTPServer, BaseHTTPRequestHandler

from os import curdir, sep

class Handler(BaseHTTPRequestHandler):
    mimetype = 'text/html'
     
    def _set_headers(self, http_code:int = 200, mimetype:str = 'text/html'):
        self.send_response(http_code)
        self.send_header('Content-type', mimetype)
        self.end_headers()
    
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        if self.path == '/gallery':
            self.path = 'gallery.html'
        try:
            if self.path.endswith(".html"):
                self.mimetype = 'text/html'
            if self.path.endswith(".jpg"):
                self.mimetype = 'image/jpeg'
            if self.path.endswith(".css"):
                self.mimetype = 'text/css'
            # file = open(self.path[1:]).read()
            file = open(curdir + sep + self.path, 'rb')
            # self.send_response(200)
            # self.end_headers()
            self._set_headers(200, self.mimetype)
            self.wfile.write(file.read())
        except:
            # self.send_response(404)
            # self.end_headers()
            self._set_headers(404)
            self.wfile.write(b"404 -Not Found.")
            
if __name__ == "__main__":
    httpd = HTTPServer(('localhost', 8000), Handler)
    print(f"\nStarted http server on localhost:8000.\n")
    httpd.serve_forever()