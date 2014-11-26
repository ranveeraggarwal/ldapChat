--drop table if exists chat_chat cascade;
--drop table if exists chat_chatroom cascade;
--drop table if exists chat_notice cascade;


insert into chat_chatroom(title, instructor_username, instructor_name, course_id) values
("Lab 01 Discussion","varsha", "Varsha Apte", "CS 348"),
("Lab 02 Discussion","varsha", "Varsha Apte", "CS 348")
;

insert into chat_chat(chatroom_id, user_id, message, chat_id) values
("1", "120050035" , "Hello World!", "-1");

insert into chat_chat(chatroom_id, user_id, message) values
("1", "120050033" , "Hello World!"),
("1", "120050035" , "Lab01 Doubts"),
("1", "120050020" , "Lab01 Submission issue"),
("1", "120050035" , "Lab01 Cribs"),
("1", "120050034" , "lab cribs");

insert into chat_notice(chatroom_id, message) values
("1", "All cribs resolved");

--insert into chat_subscribertable(chatroom_id, user_id) values

