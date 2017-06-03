import urllib
import time
import json

class Basic:
    def __init__(self):
        self.__accessToken = ''
        self.appId = "wxa539829ab3db82bb"
        self.appSecret = "95d072c693e06aca2f1243069a21a62b"

    def getAccessToken(self):
        json_file = open('access_token.json')   
        data = json.load(json_file)
        json_file.close()
        access_token = data['access_token']
    
        if data['expire_time'] < time.time():
            url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" %\
                  (self.appId, self.appSecret)
            urlResp = urllib.urlopen(url)
            urlResp = json.loads(urlResp.read())
            
            access_token = urlResp['access_token']
            data['access_token'] = access_token
            data['expire_time'] = int(time.time()) + 7000
            json_file = open('access_token.json', 'w')
            json_file.write(json.dumps(data))
            json_file.close()
        return access_token 
    
    def getUserInfo(self, openid):
        # https://api.weixin.qq.com/cgi-bin/user/info?access_token=ACCESS_TOKEN&openid=OPENID&lang=zh_CN
        url = "https://api.weixin.qq.com/cgi-bin/user/info?access_token=%s&openid=%s&lang=zh_CN" \
              % (self.getAccessToken(), openid)
        response = requests.get(url)
        return response.json()
