const httpUri = window.location.origin + "/";
let tmp = window.location.hostname.split('.')
tmp.splice(1, 0, 'ws')
const wsUri = tmp.join('.')

async function handleFile(e) {
    openWebSocket()
    $('#done').attr('style', 'display:none')
    let formData = new FormData();
    let file = document.querySelector('#upload');
    $('#done a').attr('download', file.files[0].name)
    $('#done a').html('<i class="download icon"></i>' + file.files[0].name)
    $('#loader').addClass('active')
    formData.append("file", file.files[0]);
    let result = await axios.post(httpUri, formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })
    $('#loader').removeClass('active')
    $("#ws").removeAttr('style')
    doSend(result.data)
    onMessage({
        data: "fileId: " + result.data
    });
}

function openWebSocket() {
    websocket = new WebSocket(wsUri);
    websocket.onopen = x => onOpen(x)
    websocket.onclose = x => onClose(x)
    websocket.onmessage = x => onMessage(x)
    websocket.onerror = x => onError(x)
}

function onOpen(evt) {
    writeToScreen("CONNECTED");
}

function doSend(message) {
    onMessage({
        data: ">>>> 開始轉換！"
    });
    websocket.send(message);
}

function onClose(evt) {
    writeToScreen("DISCONNECTED");
    let fileid = $('#ws *:nth-last-child(2)').text()
    $('#ws').html('')
    $('#done a').attr('href', `${httpUri}${fileid}`)
    $('#done').removeAttr('style')
}

function onMessage(evt) {
    writeToScreen('<span style="color: rgb(16, 142, 233);">' + evt.data + '</span>');
}

function onError(evt) {
    writeToScreen('<span style="color: red;">ERROR:</span> ' + evt.data);
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