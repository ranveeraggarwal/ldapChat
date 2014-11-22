from django import forms
from models import chatroom


class createChatroomForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    prof = forms.CharField(max_length=100, required=True)
    course_id = forms.CharField(max_length=100, required=True)

    class Meta:
        model = chatroom
        fields = ('title', 'prof', 'course_id')