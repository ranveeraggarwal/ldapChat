from django.db import models


class Chatroom(models.Model):
    chatroom_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    instructor_username = models.CharField(max_length=100)
    instructor_name = models.CharField(max_length=100)
    course_id = models.CharField(max_length=100)
    time_stamp = models.DateTimeField(auto_now_add= True)


class Chat(models.Model):
    chatroom_id = models.ForeignKey(Chatroom)
    chat_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    time_stamp = models.DateTimeField(auto_now_add= True)
    parent_id = models.ForeignKey('self')


class Notice(models.Model):
    chatroom_id=models.ForeignKey(Chatroom)
    notice_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=500)
    time_stamp = models.DateTimeField(auto_now_add= True)


class SubscriberTable(models.Model):
    chatroom_id = models.ForeignKey(Chatroom)
    user_id = models.CharField(max_length=100)



