import sys
import socket
from sock import sock

class Proxy(object):
    
    def __init__(self,arg):
        if(len(arg) != 2):
            print("You have to pass 2 arguments")
            print("EX: python main.py and [porta]")
            exit(1)

       
        self.Port = arg[1]
        print("Porta de entrada "+(self.Port)+ "\n")
    def requisition(self) :
        s = sock(self.Port)
        s.server()
        # try : 
        #     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
        #     s.bind(add,self.Port)
        #     s.listen()
            
        # except : 
        #     print("Error during connection")
        #     exit(1)
        # while 1 : 
        #     con,addr  = s.accept()

if __name__ == "__main__":
    proxy = Proxy(sys.argv)
    proxy.requisition()
    #print("url : "+proxy.URL)
    #print("porta : "+proxy.Port)
    
    pass