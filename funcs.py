# -*- coding: utf-8 -*
'''
    功能基类
    输入对话，操作，返回回复
    需要外部文件
    class Name(func):
        def __init__(): 
        def match(self,data):
        def getreply(self,data):
    match用来决定是否运作，返回布尔值
    getreply返回api和回话，不发话后者返回None，前者返回None表示采用默认api
'''

class func:
    def getreply(self,data):
        return "?"
    def match(self,data):
        return False
    def process(self,data,default_api):
        api,message=self.getreply(data)
        if message is None:
            return None, None
        if api is None:
            api=default_api
        return api,message
    
class Repeat(func):
    LastSentence=""
    cnt=0
    def match(self,data):
        return True
    def getreply(self,data):
        if data["message"]==self.LastSentence:
            self.cnt+=1
        else:
            self.LastSentence=data["message"]
            self.cnt=1
        if self.cnt==2:
            return None,{"message":self.LastSentence,}
        return None,None

# class 

