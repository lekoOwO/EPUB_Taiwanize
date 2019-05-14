const httpUri = location.origin + "/";
let tmp = location.hostname.split('.').splice(1, 0, 'ws')
const wsUri = location.hostname == "127.0.0.1" || location.hostname == "localhost" ? `ws://localhost:3000` : `wss://${tmp.join('.')}`

async function handleFile(e) {
    openWebSocket()
    // 隱藏已完成
    $('#done').attr('style', 'display:none')
    // 隱藏上傳區
    $('#uploader').attr('style', 'display:none')
    // 下載連結先弄好
    let file = document.querySelector('#upload');
    $('#done a').attr('download', file.files[0].name)
    $('#done a').html('<i class="download icon"></i>' + file.files[0].name)
    //轉轉轉
    $('#loader').addClass('active')
    // 發請求囉
    let formData = new FormData();
    formData.append("file", file.files[0]);
    let result = await axios.post(httpUri, formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })
    // clean ws
    $('#ws').html('')
    // 連接 ws
    websocket.send(result.data);
    console.group(result.data)
    writeToScreen('FileId: ' + result.data)
}

function openWebSocket() {
    websocket = new WebSocket(wsUri);
    websocket.onopen = x => writeToScreen("CONNECTED");
    websocket.onclose = x => onClose(x)
    websocket.onmessage = x => onMessage(x)
    websocket.onerror = x => writeToScreen('<span style="#ff3a3a">ERROR:</span> ' + x.data)
}

function onClose(evt) {
    writeToScreen("DISCONNECTED");
    console.groupEnd()
    let fileid = $('#ws *:nth-last-child(2)').text()
    $('#done a').attr('href', `${httpUri}${fileid}`)
    $('#done').removeAttr('style')
    $('#loader').removeClass('active')
    $('#loader').text('正在將檔案發給小恐龍！')
    $('#uploader').removeAttr('style')
    $("#ws").html('')
}

function onMessage(evt) {
    writeToScreen('<span style="color: #5a5a5a">' + evt.data + '</span>');
    console.log(evt.data)
    $('#loader').text(evt.data.replace(/>/g, ''))
}


function writeToScreen(message) {
    var pre = document.createElement("p");
    pre.style.wordWrap = "break-word";
    pre.innerHTML = message;
    $("#ws").append(pre);
    var scrollHeight = $('#ws').prop("scrollHeight");
    $('#ws').scrollTop(scrollHeight, 200)
}

document.querySelector('#upload').addEventListener('change', handleFile, false)