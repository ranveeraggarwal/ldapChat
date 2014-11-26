#!/usr/bin/env python

import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import uuid
from collections import defaultdict

class GetMessageHandler(tornado.web.RequestHandler):
    def get(self, room):
        data = tornado.escape.json_encode(ChatSocketHandler.cache[room])
        self.write(data)

class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    client = defaultdict(set)
    cache = defaultdict(list)
    cache_size = 200

    def get_compression_options(self):
        # Non-None enables compression with default options.
        return {}

    def open(self, room):
        self.room = room
        ChatSocketHandler.client[self.room].add(self)

    def on_close(self):
        ChatSocketHandler.client[self.room].remove(self)

    @classmethod
    def update_cache(cls, chat, room):
        cls.cache[room].append(chat)
        if len(cls.cache[room]) > cls.cache_size:
            cls.cache[room] = cls.cache[room][-cls.cache_size:]

    @classmethod
    def send_updates(cls, chat, room):
        logging.info("sending message to %d client", len(cls.client))
        for waiter in cls.client[room]:
            try:
                waiter.write_message(chat)
            except:
                logging.error("Error sending message", exc_info=True)

    def on_message(self, message):
        logging.info("got message %r", message)
        parsed = tornado.escape.json_decode(message)
        chat = {
            "id": str(uuid.uuid4()),
            "body": parsed["body"],
            }

        ChatSocketHandler.update_cache(chat, self.room)
        ChatSocketHandler.send_updates(chat, self.room)

