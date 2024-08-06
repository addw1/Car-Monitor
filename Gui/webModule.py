from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QStandardPaths
from PyQt5.QtWebEngineWidgets import QWebEngineProfile
import shutil
from PyQt5.QtWidgets import QWidget, QVBoxLayout


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


class LocationModule(QWidget):
    def __init__(self):
        super().__init__()
        self.qv = QVBoxLayout()
        # clear your browser
        clear_cache()
        # set your view
        self.view = QWebEngineView(self)
        self.view .setStyleSheet("background-color:rgba(236,236,236,0.6);\n"
                            "border-radius: 20px;" )
        with open('./Gui/html/map.html', 'r') as file:
            file_content = file.read()
        self.qv.addWidget(self.view)
        self.setLayout(self.qv)
        self.view.setHtml(file_content)

    def js_run(self, str1, str2):
        js_code = "upgrade(" + str1 + "," + str2 + ");"
        self.view.page().runJavaScript(js_code)
        self.view.show()