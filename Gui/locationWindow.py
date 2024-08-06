from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import pyqtProperty, pyqtSignal
from PyQt5.QtCore import QStandardPaths
from PyQt5.QtWebEngineWidgets import QWebEngineProfile
import shutil


class LocationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.qv = QVBoxLayout()
        # clear your browser
        clear_cache()
        # set your view
        self.view = QWebEngineView(self)
        with open('./Gui/location.html', 'r') as file:
            file_content = file.read()
        self.qv.addWidget(self.view)
        self.setLayout(self.qv)
        self.view.setHtml(file_content)


    def js_run(self):
        jscode = "upgrade("+"125," +"45" +");"
        self.view.page().runJavaScript(jscode)
        self.view.show()

def clear_cache():
    # 获取默认配置
    profile = QWebEngineProfile.defaultProfile()

    # 禁用缓存
    profile.setHttpCacheType(QWebEngineProfile.NoCache)
    profile.setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)

    # 获取缓存路径并删除
    cache_path = QStandardPaths.writableLocation(QStandardPaths.CacheLocation) + "/QtWebEngine/Default/Cache"
    try:
        shutil.rmtree(cache_path)
    except:
        pass

