import socket

class Client:
    def __init__(self):
        self.SERVER_IP='192.168.56.1'
        self.PORT_NO=5050
        self.INFO=(self.SERVER_IP,self.PORT_NO)
        self.FORMAT='utf-8'
        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect(self.INFO)
    def Send_message(self):
        while True:
            msg=str(input("enter the message!"))#first we have to encode the message into utf format before sending
            msg.encode(self.FORMAT)
            self.client.send(msg)
        
