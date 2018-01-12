#coding:utf-8
import logging
import constants

from .BaseHandler import BaseHandler

from utils.captcha import captcha

class ImageCodeHandler(BaseHandler):
    """"""
    def get(self):
        code_id = self.get_argument("codeid")
        pre_code_id = self.get_argument("pcodeid")
        if pre_code_id:
            try:
                self.redis.delete("image_code_%s" %pre_code_id)
            except Exception as e:
                logging.error(e)
        name,text,image = captcha.captcha.generate_captcha()
        try:
            self.redis.setex("image_code_%s"% code_id,constants.IMAGE_CODE_EXPIRES_SECOND ,text)
        except Exception as e:
            logging.error(e)
            self.write("")
        self.set_header("Content-Type","image/jpg")
        self.write(image)