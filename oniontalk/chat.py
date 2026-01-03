import socket
import threading
import signal
import subprocess
import sys

PORT = 5555
running = True
import os

def clear():
    os.system("clear")

def show_logo():
    try:
        with open("logo.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("[Logo file not found]")

def stop_all(sig, frame):
    global running
    print("\n[!] Stopping chat and Tor...")
    subprocess.call(["sudo", "systemctl", "stop", "tor"])
    running = False
    sys.exit(0)

signal.signal(signal.SIGINT, stop_all)

def receive(conn):
    while running:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print("\nFriend:", data.decode())
        except:
            break

def chat(conn):
    threading.Thread(target=receive, args=(conn,), daemon=True).start()
    while running:
        try:
            msg = input("> ")
            conn.send(msg.encode())
        except:
            break

def host():
    s = socket.socket()
    s.bind(("127.0.0.1", PORT))
    s.listen(1)
    print("[Waiting for connection...]")
    conn, _ = s.accept()
    print("[Connected]")
    chat(conn)

def connect(onion):
    s = socket.socket()
    s.connect((onion, PORT))
    print("[Connected]")
    chat(s)
clear()
show_logo()
print("\n")
mode = input("Host (h) or Connect (c)? ")

if mode.lower() == "h":
    host()
else:
    onion = input("Enter .onion address: ")
    connect(onion)

