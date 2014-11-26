var chatroom;
$(document).ready(function() {
    var urlpath = window.location.pathname;
    urlpath = urlpath.split("/")
    chatroom = urlpath[2];
    updater.start();
    console.log(updater.socket);

});

$("#send-message").click(function (e) {
    console.log("here")
    e.preventDefault();
    var message = $("#reply-text").val();
    updater.socket.send(message);
    $("#reply-text").val("");
});

$("#leave-room").click(function (e){
    e.preventDefault();
    updater.socket.close();
    window.location.href = '/chat/leaveRoom/'+chatroom;
});


var updater = {
    socket: null,

    start: function() {
        var url = "ws://" + location.host + "/chatsocket/" + chatroom;
        updater.socket = new WebSocket(url);
        updater.socket.onmessage = function(event) {
            updater.showMessage(JSON.parse(event.data));
        };
        updater.socket.onclose = function (event){
            console.log('socket closed');
        };
    },

    showMessage: function(msg) {
        console.log(msg)
        msg = msg[0].fields;
        console.log(JSON.stringify(msg));
        var username =  msg.user_id;
        var message = msg.message;
        var timestamp = msg.time_stamp;
        var id = msg.pk;
        var parentId = msg.parentId;

        var msgitem = '<div class="media msg"> \
	                    <div class="media-body" id="'+id+'"> \
	                        <small class="pull-right time"><i class="fa fa-clock-o"></i>'+timestamp+'</small> \
                            \
	                        <h5 class="media-heading">' + username + '</h5> \
	                        <small class="col-lg-10">'+message+'</small> \
	                    </div> \
	                </div>';

        $(".msg-wrap").append(msgitem);
    }
};
