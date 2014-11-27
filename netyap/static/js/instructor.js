/**
 * Created by dheerendra on 11/27/14.
 */

var giveup_count = 0;
function waitForSocketConnection(socket, callback){
    if (giveup_count > 15){
        $("#bc-form").append('<div class="alert alert-error alert-dismissible fade in" role="alert"> \
      <button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button> \
      <strong>Broadcast Failed!</strong> Please check your internet connection.\
    </div>');
        return;
    }
    setTimeout(
        function () {
            if (socket.readyState === 1) {
                console.log("Connection is made")
                if(callback != null){
                    callback();
                }
                return;

            } else {
                console.log("wait for connection...")
                waitForSocketConnection(socket, callback);
            }

        }, 5); // wait 5 milisecond for the connection...
    giveup_count++;
};

function sendMessage(socket, msg) {
    waitForSocketConnection(socket, function () {
        socket.send(msg);
        var title = $("#bc-title").html()
        $("#bc-form").append('<div class="alert alert-success alert-dismissible fade in" role="alert"> \
      <button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button> \
      <strong>Broadcast Successful!</strong> You have broadcasted to '+title+'.\
    </div>');

    });
};


$("a[id^=room]").click(function(e){

    e.preventDefault();
    var chatroom_id = $(this).data('id');
    var instructorusername = $(this).data('instructorusername');
    var instructorname = $(this).data('instructorname');
    var title = $(this).data('title');

    $("#bc-id").data('id', chatroom_id);
    $("#bc-title").html(title);
    $("#join-chat").attr('href', '/chat/'+chatroom_id);
});

$("#bc-id").click(function (e){
    e.preventDefault();
   var chatroom_id = $(this).data('id');
   var bcMessage = $("#bc-msg").val();
   var bcurl = "ws://"+location.host+"/chatsocket/"+chatroom_id+"/-2";
   console.log(bcurl);
   var bcws = new WebSocket(bcurl);
   bcMessage = "bc~~::~~"+bcMessage;
   sendMessage(bcws, bcMessage);
});
