from epubconv.epubconv import convertEPUB, config
import asyncio
import websockets
import uuid

settings = config.load()

def send(websocket, *args):
    loop = asyncio.get_event_loop()
    loop.create_task(websocket.send(*args))

async def api(websocket, path):
    file_path = f'./temp/{str(uuid.uuid4())}.epub'
    with open(file_path, "wb") as output_file:
        output_file.write(await websocket.recv())
    
    await websocket.send("檔案傳輸完成。")

    result = convertEPUB(file_path, lambda x: send(websocket, x))
    if (result['status']):
        await websocket.send("正在傳輸轉換結果...")
        with open(result['url'], "rb") as f:
            await websocket.send(f.read())
    else:
        await websocket.send(f"轉換失敗。\n錯誤: {result['error']}")



start_server = websockets.serve(api, settings["apiHost"], settings["apiPort"])

print("///// EPUB 轉換服務已啟動 /////")
print(f'ws://{settings["apiHost"]}:{settings["apiPort"]}')

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()