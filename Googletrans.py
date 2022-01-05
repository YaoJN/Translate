from googletrans import Translator

service_urls = ['translate.google.cn', 'translate.google.com']
proxies = {'http': "localhost:80"}

def getText(originalBox,translationBox,originalText):
    fromLang = originalBox.replace("中国語", "zh-cn").replace("日本語", "ja").replace("英語", "en")
    toLang = translationBox.replace("中国語", "zh-cn").replace("日本語", "ja").replace("英語", "en")
    translator = Translator(service_urls=['translate.google.co.jp'], proxies=proxies)
    trans_result = translator.translate(originalText, src=fromLang, dest=toLang).text
    return trans_result