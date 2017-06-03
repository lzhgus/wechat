# -*- coding: utf-8 -*-
# filename: handle.py
import hashlib
import reply
import receive
import web
import json
from material import Material
from basic import Basic

class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    if recMsg.Content == 'help':
                        content = u'暂时啥都木有'
                        replyMsg = reply.TextMsg(toUser, fromUser, content.encode("utf-8"))
                        return replyMsg.send()

                    elif recMsg.Content == "未茶":
                        mediaType = "news"
                        items = Material().batch_get(mediaType)
                        item = items['item'][0] 
                        content = item['content']
                        sourceList = []
                        print content
                        for news_item in content['news_item']:
                            source = []
                            title = news_item['title']
                            description = news_item['digest']
                            thumb_url = news_item['thumb_url']
                            url = news_item['url']
                            source.append(title.encode("utf-8"))
                            source.append(description)
                            source.append(thumb_url)
                            source.append(url)
                            sourceList.append(source) 
                        replyMsg = reply.NewsMsg(toUser, fromUser, sourceList)
                        return replyMsg.send()
                    else:
                        content = u'初入茶道 请输入help查看操作指令'
                        replyMsg = reply.TextMsg(toUser, fromUser, content.encode("utf-8"))
                        return replyMsg.send()
                elif recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()

            elif isinstance(recMsg, receive.EventMsg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.Event == "subscribe":
                    content = u'''您好，欢迎关注未茶！
回复“未茶”浏览本期匠志'''
                    replyMsg = reply.TextMsg(toUser, fromUser, content.encode("utf-8"))
                    return replyMsg.send()

                elif recMsg.Event == "unsubscribe":
                    content = u'一茶未尽 何日盼君再来'
                    replyMsg = reply.TextMsg(toUser, fromUser, content.encode("utf-8"))
                    return replyMsg.send()

                elif recMsg.Event == 'CLICK':
                    print "test123 ", recMsg.EventKey
                    if recMsg.EventKey == 'myMedia':
                        content = u"编写中，尚未完成".encode('utf-8')
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
                    else:
                        content = "test"
                        replyMsg = reply.TextMsg(toUser,fromUser, content)
                        return replyMsg.send()

                else:
                        content = "test"
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
  
            else:
                print "nothing"
                return reply.Msg().send()
        except Exception, Argment:
            return Argment

    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "weixin" 

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument
