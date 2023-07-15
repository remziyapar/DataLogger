import threading
import Controller.Router as cr
from Controller.DataBase.Reader import*
import time


params=GetParameters()

def main():


    StreamTask= threading.Thread(target=cr.Connect)
    StreamTask.start()
    StreamTask.join()

    threading.Thread(target=cr.DataSendTimer).start()
    threading.Thread(target=ReadDataFromDevices).start()

def ReadDataFromDevices():
    while True:
        if cr.ConnectStatus():
            for x in params:
                threading.Thread(target=cr.Read,args=(x,)).start()
        time.sleep(2)

if __name__=="__main__":
    main()