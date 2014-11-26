# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('chat_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_id', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=500)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('chatroom_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100, null=True, blank=True)),
                ('instructor_username', models.CharField(max_length=100, null=True, blank=True)),
                ('instructor_name', models.CharField(max_length=100, null=True, blank=True)),
                ('course_id', models.CharField(max_length=100)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('notice_id', models.AutoField(serialize=False, primary_key=True)),
                ('message', models.CharField(max_length=500)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('chatroom_id', models.ForeignKey(to='chat.Chatroom')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubscriberTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=100)),
                ('chatroom_id', models.ForeignKey(to='chat.Chatroom')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='chat',
            name='chatroom_id',
            field=models.ForeignKey(to='chat.Chatroom'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chat',
            name='parent_id',
            field=models.ForeignKey(default=-1, to='chat.Chat'),
            preserve_default=True,
        ),
    ]
