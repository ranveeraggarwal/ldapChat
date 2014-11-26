# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chat-old',
            fields=[
                ('chat_id', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('user_id', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=500)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='chatroom',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('prof', models.CharField(max_length=100)),
                ('course_id', models.CharField(max_length=100)),
                ('chatroom_id', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notice_id', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=500)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='chat-old',
            name='chatroom_id',
            field=models.ForeignKey(to='chat-old.chatroom'),
            preserve_default=True,
        ),
    ]
