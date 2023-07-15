import threading
from threading import Thread
from Clients.TelnetClient import*
from Controller.DataBase.Reader import*
import Model.ClientsModel as Cmodel

clientList=GetClients()
values=[]


def Connect():
    for x in clientList:
        print(x[Cmodel.Host])
        if x[Cmodel.Type]==Cmodel._Telnet:
            t=threading.Thread(target=Telnet, args=(x,))
            t.start()
            t.join()
        if x[Cmodel.Type]==Cmodel._Tcp:
            pass

def Read(str_arg):
        t= CustomThread(target= ReadData, args=(str_arg,))
        t.start()
        
        #print ("Router Print : ",t.join())
        values.append(t.join())
        #t= str(threading.Thread(target=ReadData,args=(str_arg,)).start())


def DataSendTimer():
    while True:
        time.sleep(60)
        a=0
        for x in values:
            a+=int(x)
        
        print(f"Total Values {a}")
        values.clear()




  
class CustomThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)

        self._target=target
        self._args=args
        self._kwargs=kwargs
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)
            
    def join(self, *args):
        Thread.join(self, *args)
        return self._return