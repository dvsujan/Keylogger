import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
   
    def handle(self):
        
        self.data = self.request.recv(1024).strip()
        file = open('log.txt', 'a')
        file.write(str(self.data)+"\n")
        
        print(str(self.data))
       
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 7000  
    
    


    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    server.serve_forever()