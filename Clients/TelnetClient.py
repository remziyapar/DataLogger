import telnetlib
import time


tn_host=""
tn_port=0
tn_timeout=1000
tn_username=""
tn_password=""
tn_status=False

def Telnet(list_arg):

    global tn_host,tn_port, tn_timeout,tn_username,tn_password
    
    tn_host=list_arg["Host"]
    tn_port=list_arg["Port"]
    tn_timeout=list_arg["TimeOut"]
    tn_username=list_arg["UserName"]
    tn_password=list_arg["Password"]

    if(tn_host!="" and tn_port!=0):
        Connect()
    
def Connect():
    global tn_status
    while True:
        if(tn_status==False):
            try:
                global tn
                tn = telnetlib.Telnet(tn_host,int(tn_port),int(tn_timeout))
                tn.set_debuglevel(100)
                tn.read_until(b"IX30 login:")
                tn.write(tn_username.encode('ascii') + b"\n")
                tn.read_until(b"Password:")
                tn.write(tn_password.encode("ascii") + b"\n")
                tn.read_until(b"Select access or quit [admin] :")
                tn.write(b"a\n")
                tn.read_until(b">").decode('ascii')
                tn_status=True
            except:
                tn_status=False
        time.sleep(5)


def ConnectStatus():
    return tn_status

def ReadData(list_arg):
    if(tn.sock_avail):
        tn.write(list_arg["WriteCommand"].encode("ascii") +b"\n")
        s=tn.read_until(b">").decode("ascii")
        if (len(s)>4):
            a=s.split(list_arg["ReadCommand"],4)
            b=a[1]
            c=b.split(" ")
            return c[4]
            #v=CurrentCalculation(c[4],50)
    else:
        tn_status=False
        return ""


            

