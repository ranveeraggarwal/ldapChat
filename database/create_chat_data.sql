--drop table if exists chat_chat cascade;
--drop table if exists chat_chatroom cascade;
--drop table if exists chat_notice cascade;

delete from chat_chatroom;
delete from chat_chat;
delete from chat_notice;
ALTER sequence chat_chat_chat_id_seq restart with 1 cache 1;

insert into chat_chatroom(title, instructor_username, instructor_name, course_id, time_stamp) values
('Lab 01 Discussion','varsha', 'Varsha Apte', 'CS 348', current_timestamp(3)),
('Lab 02 Discussion','varsha', 'Varsha Apte', 'CS 348', current_timestamp(3));


insert into chat_chat(chat_id, chatroom_id_id, user_id, message, parent_id_id, time_stamp) values
('-1', '1', '120050035' , 'Hello World!', '-1', current_timestamp(3));

insert into chat_chat(chatroom_id_id, user_id, message, parent_id_id, time_stamp) values
('1', '120050033' , 'Hello World!', 1, current_timestamp(3)),
('1', '120050035' , 'Lab01 Doubts', 2, current_timestamp(3)),
('1', '120050020' , 'Lab01 Submission issue', 3,  current_timestamp(3)),
('1', '120050035' , 'Lab01 Cribs',4 , current_timestamp(3)),
('1', '120050034' , 'lab cribs',5 , current_timestamp(3));

insert into chat_notice(chatroom_id_id, message, time_stamp) values
('1', 'All cribs resolved', current_timestamp(3));

--insert into chat_subscribertable(chatroom_id, user_id) values

