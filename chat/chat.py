#!/usr/bin/env python

import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import uuid
from collections import defaultdict

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/chatsocket/(.*)", ChatSocketHandler),
            (r"/fetchmsg/(.*)", GetMessageHandler),
        ]
        settings = dict(
            cookie_secret="lkwj39askj@Oi2ue98Kjdaisldkjri2o",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

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


def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
