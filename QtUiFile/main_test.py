from PyQt5.QtCore import QObject, pyqtSlot, QUrl
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
import sys


class MyPage(QWebEnginePage):
    def __init__(self, view):
        super().__init__(view)
        self.loaded = False

    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceID):
        print('javaScriptConsoleMessage:', level, message, lineNumber, sourceID)

    def start(self):
        if not self.loaded:
            self.loaded = True
            self.loadFinished.connect(self.onLoadFinished)
            self.load(QUrl('https://www.baidu.com'))

    def onLoadFinished(self, ok):
        if ok:
            self.runJavaScript('''
            (function() {
                var button = document.createElement("button");
                button.innerHTML = "发消息";
                button.type = "button";
                button.addEventListener("click", function() {
                    window.callFromJS("JS调用Python方法");
                });
                var body = document.getElementsByTagName("body")[0];
                body.appendChild(button);
            })();
            ''')

    @pyqtSlot(str)
    def callFromJS(self, message):
        print("JS调用Python方法", message)
        QMessageBox.information(None, "提示", message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = QWebEngineView()
    page = MyPage(view)
    view.show()
    page.start()

    page.addToJavaScriptWindowObject('page', page)
    view.setPage(page)
    sys.exit(app.exec_())