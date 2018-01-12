#coding:utf-8
import logging

from .BaseHandler import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        logging.error('error msg')
        self.write('hello world')