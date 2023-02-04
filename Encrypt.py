from cryptography.fernet import Fernet
import os
import socket
import pickle
import PySimpleGUI as sg
#from moonhole import moonlander

HOST= "127.0.0.1"
PORT= 7660

class enc_mess:
    def __init__(self,mess,dKey):
        self.mess=mess
        self.dKey=dKey

def encodems():
    event, values = sg.Window('Messag Window',
                  [[sg.T('Write a secret message'), sg.In(key='m')],
                  [sg.B('Send')]]).read(close=True)
    recomess = values['m']
    message = recomess.encode()
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message)
    em1=enc_mess(encrypted_message, key)
    tSend=pickle.dumps(em1)
    return tSend

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    emss=encodems()
    #print(emss)
    s.send(emss)
    data = s.recv(1024)

print(f"Received {data!r}")
event, values = sg.Window('Messag Window',
                [[sg.T('Server responded'), sg.T(data)],
                [sg.B('Cancel') ]]).read(close=True)
