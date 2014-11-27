#!/usr/bin/env python

import sys
import json
from django.forms.models import model_to_dict
import ast
import logging
import django.conf
import django.core.handlers.wsgi
import django.db
import django.utils.importlib
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'netyap.settings'
from chat.models import Chat, Chatroom, Notice
from collections import defaultdict
from django.core import serializers


class Message(object):

    def __init__(self, chat, type):
        self.chat = chat
        self.type = type


def get_session(request):
    if not hasattr(request, '_session'):
        engine = django.utils.importlib.import_module(
            django.conf.settings.SESSION_ENGINE
        )
        session_key = request.get_cookie(django.conf.settings.SESSION_COOKIE_NAME)
        request._session = engine.SessionStore(session_key)
    return request._session


class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    client = defaultdict(set)

    def get_compression_options(self):
        # Non-None enables compression with default options.
        return {}

    def open(self, room):
        username = get_session(self).get('username')
        if username is None:
            self.close()
            return
        userType = get_session(self).get('userType')
        self.username = username
        self.room = int(room)
        self.userType = userType
        ChatSocketHandler.client[self.room].add(self)
        chat = Chat()
        chat = model_to_dict(chat)
        chat['user_id'] = self.username
        chat['msgtype'] = 'joinstatus'
        ChatSocketHandler.send_updates(chat, self.room)


    def on_close(self):
        print "user left out"
        ChatSocketHandler.client[self.room].remove(self)
        chat = Chat()
        chat = model_to_dict(chat)
        chat['user_id'] = self.username
        chat['msgtype'] = 'leavestatus'
        ChatSocketHandler.send_updates(chat, self.room)


    @classmethod
    def send_updates(cls, chat, room):
        logging.info("sending message to %d client", len(cls.client))
        for waiter in cls.client[room]:
            try:
                waiter.write_message(chat)
            except Exception:
                logging.error("Error sending message", exc_info=True)

    def on_message(self, msg):
        userType = self.userType
        if (userType == 'f'):
            if msg.startswith("bc~~::~~"):
                chatroom = Chatroom.objects.filter(chatroom_id=int(self.room))[0]
                notice = Notice(
                    chatroom_id=chatroom,
                    message=msg[8:]
                )
                notice.save()
                time_stamp = notice.time_stamp
                parsed = model_to_dict(notice)
                parsed['msgtype'] = 'bc'
                parsed['time_stamp'] = str(time_stamp)
                ChatSocketHandler.send_updates(parsed, self.room)
                return
        chatroom = Chatroom.objects.filter(chatroom_id=int(self.room))[0]
        chatparent = Chat.objects.filter(chat_id=-1)[0]
        chat = Chat(
            user_id=self.username,
            chatroom_id=chatroom,
            message=msg,
            parent_id=chatparent
        )
        chat.save()
        logging.info("got message %r", msg)
        time_stamp = chat.time_stamp
        parsed = model_to_dict(chat)
        parsed['msgtype'] = 'msg'
        parsed['time_stamp'] = str(time_stamp)
        ChatSocketHandler.send_updates(parsed, self.room)


