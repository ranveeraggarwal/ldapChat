from django.forms import ModelForm
from django import forms
from models import Chatroom


class createChatroomForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True)
    instructor_name = forms.CharField(max_length=100, required=True)
    instructor_username = forms.CharField(max_length=100, required=True)
    course_id = forms.CharField(max_length=100, required=True)

    class Meta:
        model = Chatroom
        fields = ('title', 'instructor_name', 'instructor_username', 'course_id')