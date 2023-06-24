import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
host = "182.176.104.87"
port = 5001
filename = "01.Blender 3.0 Beginner Tutorial - Part 1.mp4"
filesize = os.path.getsize(filename)

s = socket.socket()

print(f"[+] Connecting to {host}:{port}")
s.connect((socket.gethostname(), port))
print("[+] Connected.")

s.send(f"{filename}{SEPARATOR}{filesize}".encode())
try:
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            s.sendall(bytes_read)
            progress.update(len(bytes_read))
    s.close()

except Exception as e:
    print(e)