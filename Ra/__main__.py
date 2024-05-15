import os
import socket
import json
from .modules import func

SERVER_ADDRESS = '/tmp/unix_socket'

def handle_commands(json:dict) -> int : 
    cmd = json.get('setting_name', None)
    args = json.get('args', None)
    val = func[cmd](args)
    resp = {
        "status" : 0 if val != -1 else -1,
        "return_value" : val
    }
    return resp 

def handle_client_connection(connection):
    try:
        data = connection.recv(1024).decode()
        if data:
            message = json.loads(data)
            response = handle_commands(message)
            print("Received JSON message:", message)

            connection.send(json.dumps(response).encode())
    except Exception as e:
        print("Error:", e)
    finally:
        connection.close()

def run_server():
    if os.path.exists(SERVER_ADDRESS):
        os.remove(SERVER_ADDRESS)

    server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_socket.bind(SERVER_ADDRESS)
    server_socket.listen(5)

    print("Server is listening...")

    try:
        while True:
            connection, addr = server_socket.accept()
            handle_client_connection(connection)
    except KeyboardInterrupt:
        pass
    finally:
        server_socket.close()
        os.remove(SERVER_ADDRESS)
        print("Server shut down.")

if __name__ == "__main__":
    run_server()