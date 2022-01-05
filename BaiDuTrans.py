# coding=utf-8
import http.client
import hashlib
import urllib
import random
import json
import configparser
from pip._vendor.distlib.compat import raw_input

def getText(originalBox,translationBox,originalText):
    # 百度appid和密钥(需要通过注册百度【翻译开放平台】账号后获得)
    config = configparser.ConfigParser()
    config.read('flt.ini')
    config.sections()
    appid = config['BaiduSettings']['AppId']
    secretKey = config['BaiduSettings']['SecretKey']
    # 调用百度API
    httpClient = None
    myurl = '/api/trans/vip/translate'  # 通用翻译API HTTP地址
    # 暂时保留自动接口
    fromLang = originalBox.replace("自動", "auto").replace("中国語", "zh").replace("日本語", "jp").replace("英語", "en")
    toLang = translationBox.replace("中国語", "zh").replace("日本語", "jp").replace("英語", "en")
    salt = random.randint(32768, 65536)
    # 手动录入翻译内容，text存放
    sign = appid + originalText + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(originalText) + '&from=' + fromLang + \
            '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

    # 建立会话，返回结果
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        return result

    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()