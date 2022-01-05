# coding:utf-8

import sys
import traceback

from PyQt5.QtCore import Qt

import Translate
import BaiDuTrans
import Googletrans
import json
import time
import pykakasi
from PyQt5.QtWidgets import QApplication, QDialog



class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = Translate.Ui_Translate()
        self.ui.setupUi(self)

    def queryText(self):
        hirakana = "";
        originalText = self.ui.originalText.toPlainText()
        fromLang = self.ui.originalBox.currentText()
        toLangBaidu = self.ui.translationBox.currentText()
        toLangGoogle = self.ui.translationBox_2.currentText()
        #原文区域再设定
        hirakana = MainDialog.kanjiToHirakana(self, fromLang, originalText)
        self.ui.originalText.setText(hirakana + originalText)
        print(self.ui.baiduTranslationCheck.isTristate())
        # 百度翻訳设定
        translationTextBaidu = MainDialog.setBaidu(self, fromLang, toLangBaidu, originalText)
        hirakana = MainDialog.kanjiToHirakana(self, toLangBaidu, translationTextBaidu)
        self.ui.translationText.setText(hirakana + translationTextBaidu)
        # Google翻訳设定
        translationTextGoogle = MainDialog.setGoogle(self, fromLang, toLangGoogle, originalText)
        hirakana = MainDialog.kanjiToHirakana(self, toLangGoogle, translationTextGoogle)
        self.ui.translationText_2.setText(hirakana + translationTextGoogle)
        time.sleep(0.1)
        # 百度翻译反向翻译
        # translationTextBaiduRev = MainDialog.setBaidu(self, toLangBaidu, fromLang, translationTextBaidu)
        # self.ui.transToOriginalText.setText(translationTextBaiduRev)
        # Google翻译反向翻译
        #translationTextGoogleRev = MainDialog.setGoogle(self, toLangGoogle, fromLang, translationTextGoogle)
        #self.ui.transToOriginalText_2.setText(translationTextGoogleRev)

    #百度翻訳设定
    def setBaidu(self,fromLang,toLang,originalText):
        translationText = "";
        try:
            s = json.dumps(BaiDuTrans.getText(fromLang, toLang, originalText))
            s1 = json.loads(json.dumps(json.loads(s)["trans_result"]))
            for s2 in s1:
                s3 = json.dumps(s2["dst"])
                translationText += json.loads(s3) + "\n"
        except:
            translationText = "異常発生、ログ内容を確認ください";
            #with open('../log', "a") as f:
            #    traceback.print_exc(file=f)
        return translationText

    #百度翻译反向翻译
    def setBaiduReverse(self,fromLang,toLang,translationText):
        transToOriginalText = "";
        s = json.dumps(BaiDuTrans.getText(toLang, fromLang, translationText))
        s1 = json.loads(json.dumps(json.loads(s)["trans_result"]))
        for s2 in s1:
            s3 = json.dumps(s2["dst"])
            transToOriginalText += json.loads(s3) + "\n"
        self.ui.transToOriginalText.setText(transToOriginalText)

    #Google翻訳设定
    def setGoogle(self,fromLang,toLang,originalText):
        # try:
        translationText = Googletrans.getText(fromLang, toLang, originalText)
        # except:
        #     translationText = "異常発生、ログ内容を確認ください";
        #     #with open('../log', "a") as f:
        #     #    traceback.print_exc(file=f)
        return translationText

    #漢字⇒平仮名
    def kanjiToHirakana(self, lang, text):
        textHirakana = ''
        try:
            if lang == "日本語":
                kks = pykakasi.kakasi()
                results = kks.convert(text.replace("\n",""))
                for result in results:
                    if result['orig'] == "\n":
                        textHirakana = textHirakana + "\n"
                    else:
                        textHirakana =textHirakana + result['hira']
                return textHirakana + "\n"
            return textHirakana
        except:
            with open('log.txt', "a") as f:
                traceback.print_exc(file=f)

    def clearText(self):
        self.ui.originalText.clear()
        self.ui.transToOriginalText.clear()
        self.ui.transToOriginalText_2.clear()
        self.ui.translationText.clear()
        self.ui.translationText_2.clear()

    def minBtn(self):
        self.setWindowState(Qt.WindowMinimized)

    def queryBtnJTOC(self):
        self.ui.originalBox.setCurrentIndex(0)
        self.ui.translationBox.setCurrentIndex(0)
        self.ui.translationBox_2.setCurrentIndex(0)

    def queryBtnJTOE(self):
        self.ui.originalBox.setCurrentIndex(0)
        self.ui.translationBox.setCurrentIndex(2)
        self.ui.translationBox_2.setCurrentIndex(2)

    def queryBtnCTOJ(self):
        self.ui.originalBox.setCurrentIndex(1)
        self.ui.translationBox.setCurrentIndex(1)
        self.ui.translationBox_2.setCurrentIndex(1)

    def queryBtnCTOE(self):
        self.ui.originalBox.setCurrentIndex(1)
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