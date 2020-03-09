# -*- coding: utf-8 -*
def spm(data,sid):
    ret={
        'user_id':sid,
        'message':"?",
        'auto_escape':False
    }
    ret.update(data)
    return ret
def sgm(data,sid):
    ret={
        'group_id':sid,
        'message':"?",
        'auto_escape':False
    }
    ret.update(data)
    return ret
def sdm(data,sid):
    ret={
        'discuss_id':sid,
        'message':"?",
        'auto_escape':False
    }
    ret.update(data)
    return ret
switcher={
    "/send_private_msg":spm,
    "/send_group_msg":sgm,
    "/send_discuss_msg":sdm,
}
def wrapper(api,data,sid):
    return api,switcher[api](data,sid)
