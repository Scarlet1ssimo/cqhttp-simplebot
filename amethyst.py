# -*- coding: utf-8 -*
from flask import Flask,request
from json import loads
import requests
import traceback
import sys

from bots import ScarletBot,DefaultDB,DefaultGB,DefaultPB

bot_server = Flask(__name__)
        

class Processor:
    # def __init__(self):
    identity=[ScarletBot()]+[DefaultPB(),DefaultGB(),DefaultDB()]
        

    def router(self,data):
        for bot in self.identity:
            api,reply=bot.router(data)
            if reply is not None:
                return api,reply
        return None,None
    def render(self,api,data):
        if api is not None:
            api_url = 'http://127.0.0.1:5700{}'.format(api)
            r = requests.post(api_url,data=data)
            print(r.text)
    def info(self,msg):
        api_url = 'http://127.0.0.1:5700/send_private_msg'
        data = {
            'user_id':940012978,
            'message':msg,
            'auto_escape':False
        }
        r = requests.post(api_url,data=data)
        print(r.text)
    def process(self,data):
        try:
            if data["post_type"]=="message":
                api,data=self.router(data)
                self.render(api,data)
            elif data["post_type"]=="meta_event":
                self.info("给点？")
        except Exception as e:
            self.info("我炸了，异常信息：{}。异常追溯：\n{}。".format(e,traceback.format_exc()))
       
processor=Processor()
@bot_server.route('/',methods=['POST'])
#路径是你在酷Q配置文件里自定义的
def server():
    data = request.get_data().decode('utf-8')
    data = loads(data)
    print(data)
    processor.process(data)
    return ''

if __name__ == '__main__':
    bot_server.run(host="127.0.0.1",port=8101)
    #端口也是你在酷Q配置文件里自定义的