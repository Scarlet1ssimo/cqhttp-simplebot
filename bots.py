# -*- coding: utf-8 -*
from funcs import Repeat
from apichecker import wrapper
'''
    基类
    调用 router 来获得api以及回复的json
    class BotName(BotType):
        self_id=940012978
        funcs=[xxx,]
'''
class bot:
    close=0
    # def __init__():
        # self_id=467577283
        # default_api="/send_private_msg"
        # funcs=[]
    # 检测是否同一人
    def Close(self):
        self.close=1
    def Open(self):
        self.close=0
    def router(self,data):
        if self.close==1:
            return None,None
        if not self.match(data):
            print(self.self_id,"not match")
            return None,None
        print(self.self_id,"matched")   
        idd=self.getid(data)
        '''
        #只要match也可以没有回复
        '''
        lst=[]
        for func in self.funcs:
            if func.match(data):
                api,reply=func.process(data,self.default_api)
                if reply is not None:
                    lst.append((api,reply))  
            if reply is not None:
                return wrapper(api,reply,idd)
        return None,None

class PersonBot(bot):
    default_api="/send_private_msg"
    def getid(self,data):
        return data["user_id"] if self.self_id<0 else self.self_id
    def match(self,data):
        if data["message_type"]=="private":
            if data["user_id"]==self.self_id:
                return True
        return False
class GroupBot(bot):
    default_api="/send_group_msg"
    def getid(self,data):
        return data["group_id"] if self.self_id<0 else self.self_id
    def match(self,data):
        if data["message_type"]=="group":
            if data["group_id"]==self.self_id:
                return True
        return False
class DiscussBot(bot):
    default_api="/send_discuss_msg"
    def getid(self,data):
        return data["discuss_id"] if self.self_id<0 else self.self_id
    def match(self,data):
        if data["message_type"]=="discuss":
            if data["discuss_id"]==self.self_id:
                return True
        return False
class DefaultPB(PersonBot):
    self_id=-1
    BotName="Default Private Bot"
    funcs=[Repeat(),]
    def match(self,data):
        if data["message_type"]=="private":
            return True
        return False
class DefaultGB(GroupBot):
    self_id=-2
    BotName="Default Group Bot"
    funcs=[Repeat(),]
    def match(self,data):
        if data["message_type"]=="group":
            return True
        return False
class DefaultDB(DiscussBot):
    self_id=-3
    BotName="Default Discuss Bot"
    funcs=[Repeat(),]
    def match(self,data):
        if data["message_type"]=="discuss":
            return True
        return False
class ScarletBot(PersonBot):
    self_id=940012978
    BotName="Scarlet Bot"
    funcs=[Repeat(),]