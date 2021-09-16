from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from drone import runDrone

class SimpleHttpServer:
    def __init__(self, hostName, serverPort):
        def handler(*args):
            SimpleHandler(*args)
        print("Server started http://%s:%s" % (hostName, serverPort))
        server = HTTPServer((hostName, serverPort), handler)
        server.serve_forever()


class SimpleHandler(BaseHTTPRequestHandler):
    def __init__(self, *args):
        BaseHTTPRequestHandler.__init__(self, *args)


    def do_OPTIONS(self):           
        self.send_response(200, "ok")       
        self.send_header('Access-Control-Allow-Origin', '*')                
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "*")   
        self.end_headers()


    def do_GET(self):
        runDrone()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(self.response("It's alive!"))


    def response(self, message):
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")



class main:
    def __init__(self):
        self.server = SimpleHttpServer("localhost", 3030)



if __name__ == '__main__':
    m = main()
