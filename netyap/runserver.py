#!/usr/bin/env python
from tornado.options import options, define, parse_command_line
from django.core.wsgi import get_wsgi_application
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
import os

from wsChat import ChatSocketHandler


define("port", type=int, default=8000)

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
    server.listen(options.port)
    print "server started. Press Ctrl-C to close"
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "You Pressed Ctrl-C. Closing server"
