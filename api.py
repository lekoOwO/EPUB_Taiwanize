from epubconv.epubconv import convertEPUB, config
import asyncio
import websockets
import os
from threading import Timer

settings = config.load()

def send(websocket, *args):
    loop = asyncio.get_event_loop()
    loop.create_task(websocket.send(*args))

async def api(websocket, path):
    file_path = await websocket.recv()
    result = convertEPUB(file_path, lambda x: send(websocket, x))
    if (result['status']):
        await websocket.send("正在傳輸轉換結果...")
        await websocket.send(result['url'])
        t = Timer(settings['tempTime'], lambda x: os.remove(x) if os.path.isfile(x) else None, [result['url']])
        t.start()
        
    else:
        await websocket.send(f"轉換失敗。\n錯誤: {result['error']}")



start_server = websockets.serve(api, settings["apiHost"], settings["apiPort"])

print("///// EPUB 轉換服務已啟動 /////")
print(f'ws://{settings["apiHost"]}:{settings["apiPort"]}')

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()