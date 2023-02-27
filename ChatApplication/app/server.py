import socket
import threading
# Defining Constant
class Server:
    def __init__(self):
        self.SERVER_IP='192.168.56.1'
        self.PORT_NO=5050
        self.INFO=(self.SERVER_IP,self.PORT_NO)
        self.FORMAT='utf-8'

        self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)# its used to defining which type of connection does this connection will accept
        self.server.bind(self.INFO)# binding the server_confirguation with its address
        self.active_users={}
        self.user=None

    def Handel_Request(self,conn,addr):
        print("hello This is Server How can i help you?")
        while 1:                #we have to specify the byte size as first parameter to specify how much bytes to recive 
            message=conn.recv(8).decode(self.FORMAT)# we have to specify the format in which format we have to translate/decode the bytecodes like in asci - utf-8 utf-16
            if message == 'bye':
                conn.send('Bye')
                break;
            print(message)
        conn.close();

    def Start_Server(self):
            self.server.listen() # this will listen infinity
            print('Listeneing. . . . ')
            while 1:
                conn, addr=self.server.accept()
                thread=threading.Thread(target=self.Handel_Request,args=(conn,addr)) # initializing threading and passing the function name and arguments to run as a thread
                print('Connected To \n', addr)
                #self.Save_to_database(addr,self.user)
                thread.start()
                print(threading.active_count())# this method returns the no of active theards are running includes the main thread

    def Save_to_database(self,addr,user):
        user,created=Users.objects.get_or_create(pk=user.id,defaults={'id':user.id,'name':user.username,'ip':addr})
        if created:
            print('created successfully ..')
        else:
            print('not created successfully ');
        self.active_user=[user.ip]=[user.name];

        