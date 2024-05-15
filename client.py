import socket
import json

SERVER_ADDRESS = '/tmp/unix_socket'

def send_json_message(message):
    client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDRESS)

    try:
        client_socket.send(json.dumps(message).encode())
        response = client_socket.recv(1024).decode()
        print("Received response:", json.loads(response))
    except Exception as e:
        print("Error:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    message = {"setting_name": "set_wallpaper", "args": '/home/hushm/wallpaper/MainWallpaper.jpg'}
    send_json_message(message)
