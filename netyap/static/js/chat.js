var chatroom;
var parent;
$(document).ready(function() {
    var urlpath = window.location.pathname;
    urlpath = urlpath.split("/")
    chatroom = urlpath[2];
    updater.start();
    console.log(updater.socket);

});

$("#send-message").click(function (e) {
    e.preventDefault();
    var message = $("#reply-text").val();
    updater.socket.send(message);
    $("#reply-text").val("");
});

$("#leave-room").click(function (e){
    e.preventDefault();
    updater.socket.close();
    window.location.href = '/chat/leaveroom/'+chatroom;
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
        type = msg.msgtype;
        if (type == 'leavestatus'){
            $(".msg-wrap").prepend(msg.user_id + " has left the chat\n");
            return;
        }
        if (type == 'joinstatus'){
            $(".msg-wrap").prepend(msg.user_id +" has joined the chat\n");
            return;
        }
        var username =  msg.user_id;
        var message = msg.message;
        var timestamp = msg.time_stamp;
        var id = msg.chat_id;
        var parentId = msg.parentId;

        var msgitem = '<div class="media msg"> \
	                	<div class="pull-right"> \
									<small class="time"><i class="fa fa-clock-o"></i>'+timestamp+'</small> \
									&middot; \
									<small class="time"><a href="/chat/'+chatroom+'/'+id+'"><i class="fa fa-reply"></i> Reply</a></small> \
								</div> \
		                    <div class="media-body"> \
		                        <h5 class="media-heading">'+username+'</h5> \
		                        <small class="col-lg-10">'+message+'</small> \
    \
		                    </div> \
		                <hr> \
	                	</div>';

        $(".msg-wrap").prepend(msgitem);
    }
};
