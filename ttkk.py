sourceList = [['Test', '\xe7\x94\xa8\xe4\xba\x8e\xe5\xbc\x80\xe5\x8f\x91\xe6\xb5\x8b\xe8\xaf\x95', u'http://mmbiz.qpic.cn/mmbiz_jpg/pgYibJnRLaXIxZXSK3bL4XuKZJBYvo609MPicYIW5aZuXosHmBGLfLm64Q59II1yxTV2pENYYRtHyN5SFE8zzJ8Q/0?wx_fmt=jpeg', u'http://mp.weixin.qq.com/s?__biz=MzI2NTQ3MTI5OQ==&mid=100000002&idx=1&sn=14dea6587a14d5276f976f875ffcbd8d&chksm=6a9d952e5dea1c383fc9200a69cbfecb27b097ad1c61c6153edf55b99f3b00e7e66d1e6ae76e#rd']]
itemXml = []
for source in sourceList:
   print source
   singleXml = """
       <item>
           <Title><![CDATA[%s]]></Title>
           <Description><![CDATA[%s]]></Description>
           <PicUrl><![CDATA[%s]]></PicUrl>
           <Url><!CDATA[%s]]></Url>
       </item>
   """ % (source[0], source[1], source[2], source[3])
   itemXml.append(singleXml)
print itemXml
