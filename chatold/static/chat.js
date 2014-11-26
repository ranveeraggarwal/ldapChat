var chatroom;
$(document).ready(function() {
    if (!window.console) window.console = {};
    if (!window.console.log) window.console.log = function() {};
    $("#input").hide();
    $("#roomform").show();
    $("#chatroom").select();

    $("#roomform").submit(function(e){
        e.preventDefault;
        startConnection($(this));
        return false;
    });

    $("#messageform").submit(function (e){
        newMessage($(this));
        return false;
    });

});

function startConnection(form){
    form.hide();
    chatroom = form.find("input#chatroom").val();
    updater.start();
    $("#input").show();
    $("#message").select();

}
function formToJSON(form) {
    var fields = form.serializeArray();
    var json = {}
    for (var i = 0; i < fields.length; i++) {
        json[fields[i].name] = fields[i].value;
    }
    if (json.next) delete json.next;
    return json;
};

function newMessage(form) {
    var message = formToJSON(form);
    updater.socket.send(JSON.stringify(message));
    form.find("input[type=text]").val("").select();
}


function createMsg(msg){
    return '<div class="message" id="m' + msg.id + '">'+ msg.body + '</div>';
}

function fetchmsg(){
    $.ajax({
        async: false,
        type: 'GET',
        url: "http://" + location.host + "/fetchmsg/" + chatroom,
        dataType: 'JSON',
        success: function (data) {
            $.each(data, function(key,msg){
                $("#inbox").append(createMsg(msg));
                $(createMsg(msg)).slideDown();
            });
        }
    });
}

var updater = {
    socket: null,

    start: function() {
        var url = "ws://" + location.host + "/chatsocket/" + chatroom;
        updater.socket = new WebSocket(url);
        updater.socket.onmessage = function(event) {
            updater.showMessage(JSON.parse(event.data));
        }
        fetchmsg();
    },

    showMessage: function(msg) {
        var existing = $("#m" + msg.id);
        if (existing.length > 0) return;
        $("#inbox").append(createMsg(msg));
        $(createMsg(msg)).slideDown();
    }
};
