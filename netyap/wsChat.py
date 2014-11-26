#!/usr/bin/env python

import sys
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
from chat.models import Chat, Chatroom
from collections import defaultdict
from django.core import serializers


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
        self.username = username
        self.room = int(room)
        ChatSocketHandler.client[self.room].add(self)


    def on_close(self):
        print "user left out"
        ChatSocketHandler.client[self.room].remove(self)


    @classmethod
    def send_updates(cls, chat, room):
        logging.info("sending message to %d client", len(cls.client))
        for waiter in cls.client[room]:
            try:
                waiter.write_message(chat)
            except Exception:
                logging.error("Error sending message", exc_info=True)

    def on_message(self, msg):
        print "function called"

        chatroom = Chatroom.objects.filter(chatroom_id=1)[0]
        chatparent = Chat.objects.filter(chat_id=-1)[0]
        chat = Chat(
            user_id=self.username,
            chatroom_id=chatroom,
            message=msg,
            parent_id=chatparent
        )
        chat.save()
        logging.info("got message %r", msg)
        parsed = serializers.serialize('json', [chat, ])
        ChatSocketHandler.send_updates(parsed, self.room)

        #print "chatroom %s not found" % self.room
        #self.close()

