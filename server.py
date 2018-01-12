#coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import torndb
import redis

from tornado.options import define,options
from urls import handlers
import config

define("port",type=int,default=8000,help="run server on the given port")

class Application(tornado.web.Application):
    """"""
    def __init__(self,*args,**kwargs):
        super(Application,self).__init__(*args,**kwargs)
        # self.db = torndb.Connection(
        #     host = '127.0.0.1',
        #     database = 'ihome',
        #     user = 'root',
        #     password = 'mysql',
        # )
        self.db = torndb.Connection(**config.mysql_options)
        # self.redis = redis.StrictRedis(
        #     host = '127.0.0.1',
        #     port = 6379,
        # )
        self.redis = redis.StrictRedis(**config.redis_options)

def main():
    tornado.options.parse_command_line()
    app = Application(
        handlers,**config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()