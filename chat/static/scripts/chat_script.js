const chatSocket = new WebSocket("ws://" + window.location.host + "/ws/socket-server") ;

const username = JSON.parse(document.getElementById('username').textContent);
chatSocket.onopen = function(e){
    console.log("connection was set up successfully")
};
chatSocket.onclose = function(e){
    console.log("connection was closed");
};

chatSocket.onerror = function(e){
    console.log(e)
}

let messageInputSelector = document.querySelector("#id_message_send_input");
let messageButtonSelector = document.querySelector("#id_message_send_button");
// let chatItemContainer = document.querySelector("#id_chat_item_container")
let mainContainer = document.querySelector("#id_main_container")

messageInputSelector.focus();

messageInputSelector.onkeyup = function(e) {
    if(e.keyCode == 13){
        messageButtonSelector.click();
    }
};

messageButtonSelector.onclick = function(e){
    let messageInput = messageInputSelector.value;
    chatSocket.send(JSON.stringify({message: messageInput, username: username}));
};

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    var chatBubble = document.createElement("div");
    chatBubble.setAttribute('class', 'bubbleWrapper')
    chatBubble.innerHTML = `
    <div class="inlineContainer other">
    <div class="otherBubble other">
        ${data.message}
    </div>
    </div><span class="other">${data.timestamp} ${data.username}</span>
    `
    messageInputSelector.value = "";
    mainContainer.appendChild(chatBubble)
    // chatItemContainer.appendChild(div);
}