# coding:utf-8
import os
import sys
from threading import Thread
import traceback

from PyQt5.QtCore import Qt

import Translate
import BaiDuTrans
import Googletrans
import json
import time
import pykakasi
from PyQt5.QtWidgets import QApplication, QDialog

class MyThread(Thread):
    def __init__(self, func, args):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = Translate.Ui_Translate()
        self.ui.setupUi(self)

    def queryText(self):
        hirakana = "";
        # 取得画面选择信息
        # 原文
        originalText = self.ui.originalText.toPlainText()
        # 翻译元语言和翻译目标语言
        fromLang = self.ui.originalBox.currentText()
        toLangBaidu = self.ui.translationBox.currentText()
        toLangGoogle = self.ui.translationBox_2.currentText()
        # 履历区域现有内容
        resumeTextArea = self.ui.resume.toPlainText()
        # 翻译区域各checkbox选择
        baiduTranslationCheck = self.ui.baiduTranslationCheck.isChecked()
        baiduTranslationReCheck = self.ui.baiduTranslationReCheck.isChecked()
        googleTranslationCheck = self.ui.googleTranslationCheck.isChecked()
        googleTranslationCheck_2 = self.ui.googleTranslationCheck_2.isChecked()
        # 履历区域各checkbox选择
        resumeBaidu = self.ui.resumeBaidu.isChecked()
        resumeGoogle = self.ui.resumeGoogle.isChecked()
        savefile = self.ui.savefile.isChecked()

        # 现有内容清除
        self.ui.translationText.clear()
        self.ui.transToOriginalText.clear()
        self.ui.translationText_2.clear()
        self.ui.transToOriginalText_2.clear()

        # 原文为日语时，平假名追加,区域再设定
        hirakana = MainDialog.kanjiToHirakana(self, fromLang, originalText)
        self.ui.originalText.setText(hirakana + originalText)
        # 翻译方法追加到线程
        t1 = MyThread(MainDialog.setBaiduText, args=(self, fromLang, toLangBaidu, originalText,
                                                     baiduTranslationReCheck))
        t2 = MyThread(MainDialog.setGoogleText, args=(self, fromLang, toLangGoogle, originalText,
                                                      googleTranslationCheck_2))
        # 百度翻译check被选中,执行百度翻译操作
        if baiduTranslationCheck:
            t1.start()
            t1.join()
        # Google翻译check被选中,执行谷歌翻译操作
        if googleTranslationCheck:
            t2.start()
            t2.join()
        # 取得百度翻译结果
        if baiduTranslationCheck:
            listBaiduText = t1.get_result()
            translationTextBaidu = listBaiduText[0]
            translationTextBaiduRev = listBaiduText[1]
            # 文字内容为日语时，进行平假名追加
            hirakana = MainDialog.kanjiToHirakana(self, toLangBaidu, translationTextBaidu)
            self.ui.translationText.setText(hirakana + translationTextBaidu)
            # 百度反向翻译check被选中,执行百度反向翻译操作
            if baiduTranslationReCheck:
                self.ui.transToOriginalText.setText(translationTextBaiduRev)
        # 取得谷歌翻译结果
        if googleTranslationCheck:
            listGoogleText = t2.get_result()
            translationTextGoogle = listGoogleText[0]
            translationTextGoogleRev = listGoogleText[1]
            # 文字内容为日语时，进行平假名追加
            hirakana = MainDialog.kanjiToHirakana(self, toLangGoogle, translationTextGoogle)
            self.ui.translationText_2.setText(hirakana + translationTextGoogle)
            # Google反向翻译check被选中,执行Google反向翻译操作
            if googleTranslationCheck_2:
                self.ui.transToOriginalText_2.setText(translationTextGoogleRev)
        # 翻译内容保存到右侧区域或者文本
        # 设置区域内容
        if resumeBaidu or resumeGoogle:
            resumeText = '■原文:' + originalText + '\n'
            if resumeBaidu and baiduTranslationCheck:
                resumeText += '■百度:' + translationTextBaidu
            if resumeGoogle and googleTranslationCheck:
                resumeText += '■谷歌:' + translationTextGoogle + '\n'
            resumeText += '--------------------------------------' + '\n'
            resumeTextArea += resumeText
            # 翻译内容保存到文件
            if savefile:
                # openFile
                fo = open("Translate.txt", "a", encoding='utf-8')
                fo.write(resumeText)
                # closeFile
                fo.close()
        self.ui.resume.setText(resumeTextArea)

    # 取得并设置百度翻译结果
    def setBaiduText(self, fromLang, toLangBaidu, originalText, baiduTranslationReCheck):
        listBaiduText = []
        translationTextBaiduRev = ''
        # 翻译内容取得
        translationTextBaidu = MainDialog.setBaidu(self, fromLang, toLangBaidu, originalText)
        # 百度反向翻译check被选中,执行百度反向翻译操作
        if baiduTranslationReCheck:
            time.sleep(0.5)
            # 百度翻译反向翻译
            translationTextBaiduRev = MainDialog.setBaidu(self, toLangBaidu, fromLang, translationTextBaidu)
        listBaiduText.append(translationTextBaidu)
        listBaiduText.append(translationTextBaiduRev)
        return listBaiduText

    # 取得并设置谷歌翻译结果
    def setGoogleText(self, fromLang, toLangGoogle, originalText, googleTranslationCheck_2):
        listGoogleText = []
        translationTextGoogleRev = ''
        # 翻译内容取得
        translationTextGoogle = MainDialog.setGoogle(self, fromLang, toLangGoogle, originalText)
        # Google反向翻译check被选中,执行Google反向翻译操作
        if googleTranslationCheck_2:
            translationTextGoogleRev = MainDialog.setGoogle(self, toLangGoogle, fromLang, translationTextGoogle)
        listGoogleText.append(translationTextGoogle)
        listGoogleText.append(translationTextGoogleRev)
        return listGoogleText

    # 百度翻訳设定
    def setBaidu(self, fromLang, toLang, originalText):
        translationText = "";
        try:
            # 取得返回结果
            result = BaiDuTrans.getText(fromLang, toLang, originalText)
            errorCode = result.get("error_code")
            # 返回结果错误判断
            if None != errorCode:
                translationText = MainDialog.getErrorMsg(errorCode)
            else:
                s = json.dumps(result)
                s1 = json.loads(json.dumps(json.loads(s)["trans_result"]))
                for s2 in s1:
                    s3 = json.dumps(s2["dst"])
                    translationText += json.loads(s3) + "\n"
        except:
            translationText = "異常発生、ログ内容を確認ください\n";
            with open('../log', "a") as f:
                traceback.print_exc(file=f)
        return translationText

    # 百度翻译反向翻译
    def setBaiduReverse(self, fromLang, toLang, translationText):
        transToOriginalText = "";
        s = json.dumps(BaiDuTrans.getText(toLang, fromLang, translationText))
        s1 = json.loads(json.dumps(json.loads(s)["trans_result"]))
        for s2 in s1:
            s3 = json.dumps(s2["dst"])
            transToOriginalText += json.loads(s3) + "\n"
        self.ui.transToOriginalText.setText(transToOriginalText)

    # Google翻訳设定
    def setGoogle(self, fromLang, toLang, originalText):
        # try:
        translationText = Googletrans.getText(fromLang, toLang, originalText)
        return translationText

    # 漢字⇒平仮名
    def kanjiToHirakana(self, lang, text):
        textHirakana = ''
        try:
            if lang == "日本語":
                kks = pykakasi.kakasi()
                results = kks.convert(text.replace("\n", ""))
                for result in results:
                    if result['orig'] == "\n":
                        textHirakana = textHirakana + "\n"
                    else:
                        textHirakana = textHirakana + result['hira']
                return textHirakana + "\n"
            return textHirakana
        except:
            with open('log.txt', "a") as f:
                traceback.print_exc(file=f)

    def getErrorMsg(self,errorCode):
        translationText = ''
        if errorCode == '52001':
            translationText = '请求超时(请重试)'
        elif errorCode == '52001':
            translationText = '系统错误(系统错误)'
        elif errorCode == '52003':
            translationText = '未授权用户(请检查appid是否正确或者服务是否开通)'
        elif errorCode == '54000':
            translationText = '必填参数为空(请检查是否少传参数)'
        elif errorCode == '54001':
            translationText = '签名错误(请检查您的签名生成方法)'
        elif errorCode == '54003':
            translationText = '访问频率受限(请降低您的调用频率，或进行身份认证后切换为高级版/尊享版)'
        elif errorCode == '54004':
            translationText = '账户余额不足(请前往管理控制台为账户充值)'
        elif errorCode == '54005':
            translationText = '长query请求频繁(请降低长query的发送频率，3s后再试)'
        elif errorCode == '58000':
            translationText = '客户端IP非法(检查个人资料里填写的IP地址是否正确，可前往开发者信息-基本信息修改 )'
        elif errorCode == '58001':
            translationText = '译文语言方向不支持(检查译文语言是否在语言列表里)'
        elif errorCode == '54002':
            translationText = '服务当前已关闭(请前往管理控制台开启服务)'
        elif errorCode == '90107':
            translationText = '认证未通过或未生效(请前往我的认证查看认证进度)'
        return translationText

    # 清除画面内容
    def clearText(self):
        self.ui.originalText.clear()
        self.ui.transToOriginalText.clear()
        self.ui.transToOriginalText_2.clear()
        self.ui.translationText.clear()
        self.ui.translationText_2.clear()

    # 最小化
    def minBtn(self):
        self.setWindowState(Qt.WindowMinimized)

    def queryBtnJTOC(self):
        self.ui.originalBox.setCurrentIndex(1)
        self.ui.translationBox.setCurrentIndex(1)
        self.ui.translationBox_2.setCurrentIndex(1)

    def queryBtnJTOE(self):
        self.ui.originalBox.setCurrentIndex(1)
        self.ui.translationBox.setCurrentIndex(2)
        self.ui.translationBox_2.setCurrentIndex(2)

    def queryBtnCTOJ(self):
        self.ui.originalBox.setCurrentIndex(0)
        self.ui.translationBox.setCurrentIndex(0)
        self.ui.translationBox_2.setCurrentIndex(0)

    def queryBtnCTOE(self):
        self.ui.originalBox.setCurrentIndex(0)
        self.ui.translationBox.setCurrentIndex(2)
        self.ui.translationBox_2.setCurrentIndex(2)

    def queryBtnETOJ(self):
        self.ui.originalBox.setCurrentIndex(2)
        self.ui.translationBox.setCurrentIndex(0)
        self.ui.translationBox_2.setCurrentIndex(0)

    def queryBtnETOC(self):
        self.ui.originalBox.setCurrentIndex(2)
        self.ui.translationBox.setCurrentIndex(1)
        self.ui.translationBox_2.setCurrentIndex(1)


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(myapp.exec_())
