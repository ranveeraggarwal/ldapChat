from django.db import models

class chatroom(models.Model):
	title = models.CharField(max_length=100)
	prof = models.CharField(max_length=100)
	course_id = models.CharField(max_length=100)
	chatroom_id = models.CharField(max_length=100,primary_key = True)
	time_stamp = models.DateTimeField(auto_now_add= True)
	
class chat(models.Model):
	chatroom_id = models.ForeignKey(chatroom)
	chat_id = models.CharField(max_length=100,primary_key = True)
	user_id = models.CharField(max_length=100)
	message = models.CharField(max_length=500)
	time_stamp = models.DateTimeField(auto_now_add= True)
	#parent_id = models.ForeignKey(chat)
	
class notice(models.Model):
	notice_id = models.CharField(max_length=100)
	message = models.CharField(max_length=500)
	time_stamp = models.DateTimeField(auto_now_add= True)
	

# Create your models here.
