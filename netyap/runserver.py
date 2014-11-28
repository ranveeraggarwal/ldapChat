#!/usr/bin/env python
from tornado.options import options, define, parse_command_line
from django.core.wsgi import get_wsgi_application
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
import os
import threading
from datetime import datetime


from wsChat import ChatSocketHandler


define("port", type=int, default=8000)


def start_server(app):
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


def main():
    parse_command_line()
    os.environ['DJANGO_SETTINGS_MODULE'] = 'netyap.settings'
    wsgi_app = tornado.wsgi.WSGIContainer(
        get_wsgi_application()
    )
    tornado_app = tornado.web.Application(
        [
            (r"/chatsocket/(\d+)/(-?\d+)", ChatSocketHandler),
            (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static/"}),
            ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
        ],
        debug=True
    )
    server = tornado.httpserver.HTTPServer(tornado_app)
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    message = 'Starting server at %s\n Press Ctrl-C to stop' % current_time
    print message
    threading.Thread(target=start_server(server)).start()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "You Pressed Ctrl-C. Closing server"
