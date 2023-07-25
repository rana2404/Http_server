import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("CST 8808 - Cyber Incident Handling server is up and running...!")
    httpd.serve_forever()



#reference: https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler