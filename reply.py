# -*- coding: utf-8 -*-
# filename: reply.py
import time

class Msg(object):
    def __init__(self):
        pass
    def send(self):
        return "success"

class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content
        print "test"

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content>{Content}</Content>
        </xml>
        """
        print XmlForm.format(**self.__dict)
        return XmlForm.format(**self.__dict)
    
class ImageMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId
    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        </Image>
        </xml>
        """
        return XmlForm.format(**self.__dict)

class NewsMsg(Msg):
    def __init__(self, toUserName, fromUserName, sourceList):
        self.ToUserName = toUserName
        self.FromUserName = fromUserName
        self.SourceList = sourceList 

    def send(self):
        itemXml = []
        for source in self.SourceList:
            singleXml = """
                <item>
                    <Title><![CDATA[%s]]></Title>
                    <Description><![CDATA[%s]]></Description>
                    <PicUrl><![CDATA[%s]]></PicUrl>
                    <Url><!CDATA[%s]]></Url>
                </item>
            """ % (source[0], source[1], source[2], source[3])
            itemXml.append(singleXml)
        reply = """
            <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[news]]></MsgType>
                <ArticleCount>%d</ArticleCount>
                <Articles>
                    %s
                </Articles>
            </xml>
        """ % (self.ToUserName, self.FromUserName, str(int(time.time())), len(self.SourceList), " ".join(itemXml))
        print reply
        return reply
        
