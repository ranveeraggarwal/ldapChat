from django.db import models


class chatroom(models.Model):
    chatroom_id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    instructor_username = models.CharField(max_length=100)
    instructor_name = models.CharField(max_length=100)
    course_id = models.CharField(max_length=100)
    time_stamp = models.DateTimeField(auto_now_add= True)


class chat(models.Model):
    chatroom_id = models.ForeignKey(chatroom)
    chat_id = models.CharField(max_length=100, primary_key=True)
    user_id = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    time_stamp = models.DateTimeField(auto_now_add= True)
    parent_id = models.ForeignKey('self')


class notice(models.Model):
    notice_id = models.CharField(max_length=100, primary_key=True)
    message = models.CharField(max_length=500)
    time_stamp = models.DateTimeField(auto_now_add= True)

class subscribertable(models.Model):
    chatroom_id = models.ForeignKey(chatroom)
    user_id = models.CharField(max_length=100)

