var chatroom;
var parent;
$(document).ready(function() {
    var urlpath = window.location.pathname;
    urlpath = urlpath.split("/")
    chatroom = urlpath[2];
    parent = urlpath[3];
    if (typeof(parent) == 'undefined'){
        parent = -1;
    }
    console.log(parent);
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
        var url = "ws://" + location.host + "/chatsocket/" + chatroom+"/"+String(parent);
        updater.socket = new WebSocket(url);
        updater.socket.onmessage = function(event) {
            updater.showMessage(JSON.parse(event.data));
        };
        updater.socket.onclose = function (event){
            console.log('socket closed');
        };
    },

    showMessage: function(msg) {
        console.log(msg.parent_id);
        console.log(parent);
        type = msg.msgtype;
        if (type == 'bc'){
            if (chatroom == msg.chatroom_id){
                $("#brodal-body").html(msg.message);
                $("#brodal").modal('toggle');
            }
            return;
        }
        if (type == 'leavestatus'){
            var msgitem1 = '<div class="media msg"> \
                                <div class="media-body"> \
                                    <h5 class="media-heading">'+msg.user_id+'</h5> \
                                    <small class="col-lg-10">Has left the chat.</small> \
        \
                                </div> \
                            <hr> \
                            </div>';
            $(".msg-wrap").prepend(msgitem1);
            return;
        }
        if (type == 'joinstatus'){
            var msgitem2 = '<div class="media msg"> \
                                <div class="media-body"> \
                                    <h5 class="media-heading">'+msg.user_id+'</h5> \
                                    <small class="col-lg-10">Has joined the chat.</small> \
        \
                                </div> \
                            <hr> \
                            </div>';
            $(".msg-wrap").prepend(msgitem2);
            return;
        }
        var username =  msg.user_id;
        var message = msg.message;
        var timestamp = msg.time_stamp;
        var id = msg.chat_id;

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
