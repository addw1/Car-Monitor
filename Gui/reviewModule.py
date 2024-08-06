from reviewModule_ui import ReviewModuleUi
from PyQt5.QtWidgets import QFrame, QStackedLayout
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QStandardPaths
from PyQt5.QtWebEngineWidgets import QWebEngineProfile

import shutil
import cv2

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

class ReviewModule(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = ReviewModuleUi()
        self.ui.setupUi(self)
        self.frame = self.ui.frame
        self.pathBtn = self.ui.pushButton
        self.videoBtn = self.ui.pushButton_2
        self.loadBtn = self.ui.pushButton_3
        self.videoBtn.setVisible(False)
        self.qv = QStackedLayout()
        # clear your browser
        clear_cache()
        # set your view
        self.view = QWebEngineView(self)
        self.view.setStyleSheet("background-color:rgba(236,236,236,0.6);\n"
                                "border-radius: 20px;")
        with open('./Gui/html/pathVisual.html', 'r') as file:
            file_content = file.read()
        self.qv.addWidget(self.view)
        self.frame.setLayout(self.qv)
        self.view.setHtml(file_content)


