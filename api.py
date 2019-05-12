from epubconv.epubconv import convertEPUB, config
import asyncio
import websockets
import os
from threading import Timer, Thread

settings = config.load()

async def api(websocket, path):
    file_path = f'./temp/{await websocket.recv()}.epub'
    result = await convertEPUB(file_path, lambda x:websocket.send(x))
    if (result['status']):
        await websocket.send(">>>>> 正在傳輸轉換結果...")
        await websocket.send(result['id'])

        confirm = await websocket.recv()
        while (confirm != result['id']):
            confirm = await websocket.recv()

        Timer(settings['tempTime'], lambda x: os.remove(x) if os.path.isfile(x) else None, [f"./temp/{result['id']}.epub"]).start()
        
    else:
        await websocket.send(f"轉換失敗。\n錯誤: {result['error']}")

async def start_server():
    print("///// EPUB 轉換服務已啟動 /////")
    await websockets.serve(api, settings["apiHost"], settings["apiPort"])
    print(f'ws://{settings["apiHost"]}:{settings["apiPort"]}')
    
loop = asyncio.get_event_loop()
loop.create_task(start_server())
loop.run_forever()

