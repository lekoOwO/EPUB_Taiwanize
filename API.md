
# API

  

## Run 運行

  

### File Server

  

##### Windows 10

`./file_server.bat`

  

##### Unix-Like Systems

`bash ./file_server.sh`

  

---

### Websocket Server

`python3 ./api.py`

  

## Usage 使用

  

### File Server

####`GET /{file_id}`

  

Get a file by file id.

  
  

#### `POST /`

  

##### Body:

  

```
{

	"file": File

}
```

  

##### Response:

`file_id`

  
  

Upload a EPUB book.

  

### Websocket Server

After the connection established, send a file_id to start the convertion. The progress will be sent continuously until the convertion is finished, and the file_id of the converted EPUB will be sent.

  

連線後，傳送 file_id 以開始轉換。轉換過程中會持續發送進度直到轉換完成。完成轉換的 file_id 將會被送回。