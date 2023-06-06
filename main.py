import http.server # Parametrage : location, handler 
import socketserver # Ecoute

#Handler
class APIHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) :
        print("Coucou")
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write("coucou".encode('utf-8'))

MyAPIHandler = APIHandler

# Server
try:
    with socketserver.TCPServer(("",8080), MyAPIHandler) as httpd:
        print("server working")
        httpd.allow_reuse_address = True
        httpd.serve_forever()
except KeyboardInterrupt:
    print("Stopping server")
    httpd.server_close()
