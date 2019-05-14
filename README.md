# EPUB_Taiwanize
  
Convert EPUB from zh_CN to zh_TW using [ZHConvert](https://zhconvert.org/)

透過[繁化姬](https://zhconvert.org/)將 EPUB 電子書台灣化

## Requirement 需求
* Python 3.7 or later

## Installation 安裝
`pip3 install -r ./requirements.txt`

## Usage 使用
`python3 main.py YOUR_EPUB_FILE`

## API
[文件](API.md)

## Docker
Build and run the Dockerfile.
Forward a.b.tld to port 3000 of the container, a.ws.b.tld to port 3001.
Example: epub.example.com -> 3000, epub.ws.example.com -> 3001

build 並 run Dockerfile 後，將 a.b.tld 網域對應至容器內 Port 3000，a.ws.b.tld 對應至容器內 Port 3001
舉例: epub.example.com -> 3000, epub.ws.example.com -> 3001

## Update history 更新歷史
* 1.0.1
新增網頁 API 功能
* 1.0.0
Init Release.

## Special Thanks 特別感謝
This project is based on [EpubConv_Python](https://github.com/ThanatosDi/EpubConv_Python).

This project cannot work without [ZHConvert](https://zhconvert.org/).


本專案以 [EpubConv_Python](https://github.com/ThanatosDi/EpubConv_Python) 為基礎開發。

本專案的運作仰賴於[繁化姬](https://zhconvert.org/)。

