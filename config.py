# coding: utf-8

import os

#Application配置参数
settings = {
    "static_path":os.path.join(os.path.dirname(__file__),"static"),
    "template_path":os.path.join(os.path.dirname(__file__),"template"),
    "cookie_secret":'wangmaotong',
    "xsrf_cookies":True,
    "debug":True,
}

#mysql
mysql_options = dict(
    host = '127.0.0.1',
    database = 'ihome',
    user = 'root',
    password = 'qw13198321328',
)

#redis
redis_options = dict(
    host = '127.0.0.1',
    port = 6379,
)
