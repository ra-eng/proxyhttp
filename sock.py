import socket
import utils
MYHOST  = '127.0.0.1'
MYPORT = 8080

class sock(object):
    def __init__(self,*args):
        try : 
            self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error as e:
            print("Fail to create a socket")
            print(e)
            exit(1)
        if len(args)!=0 :
            self.MYHOST = MYHOST
            self.MYPORT = int(args[0])
        else : 
            self.MYHOST = MYHOST
            self.MYPORT = MYPORT

        print("classe : [PORT] {}".format(self.MYPORT))


    def client(self):
        while True: 
                self.s.connect((MYHOST,MYPORT))
        #data =self.s.recv(512000)
        #(data.decode())
    def server(self):
        try:
            self.s.bind((self.MYHOST,self.MYPORT))
            self.s.listen(3)
        except socket.error as err : 
            print(err)
            exit(1)
        
        
        while True:
            conn, addr= self.s.accept()
            data = conn.recv(5120)
            if data.startswith("GET"):
                data =str(data)
                print(data.decode())
                a=utils.getdic(data.split("\n"))
                print("dicionario \n")
                print(a)
            else : 
                print("Erro: Not implemented (501)\n")

#if __name__ == "__main__":
    #soc= sock()
    #print("SOCKET : [HOST] {}  , [PORT] {}".format(soc.MYHOST,soc.MYPORT))
    #soc.server()

        