#!/usr/bin/python

import sys
import os
from tornado import ioloop
import tornado.web
from huinya_master_settings import *


class UploadHandler(tornado.web.RequestHandler):
    def get(self):
        print "Hello, world!"

if __name__ == "__main__":
    application = tornado.web.Application([(r"/upload", UploadHandler)])
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
