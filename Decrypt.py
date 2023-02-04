import socket
from cryptography.fernet import Fernet
import pickle
#from moonhole import moonlander

class enc_mess:
    def __init__(self,mess,dKey):
        self.mess=mess
        self.dKey=dKey

def demess(outLo):
    EcMess=enc_mess(outLo.mess, outLo.dKey)
    f = Fernet(EcMess.dKey)
    decrypted_message = f.decrypt(EcMess.mess)
    data=decrypted_message
    return data


HOST = "127.0.0.1" 
PORT = 7660 


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")    
        data = conn.recv(1024)
        outLo=pickle.loads(data)
        deco_mess=demess(outLo)
        data=deco_mess
        conn.sendall(data)
        if not data:
            conn.sendall(data)