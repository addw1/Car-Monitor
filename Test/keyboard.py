import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from publisher import MqttPublisher
# QMainWindow Window类
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(50, 50, 300, 200)
        self.setWindowTitle("Press any key")

    # 读取键盘输入值的响应函数
    def keyPressEvent(self, event):
        # 获取键盘按键值
        key = event.key()
        # 将按键值转换为字符串
        key = chr(Qt.Key(key))
        # 在控制台中输出键盘输入值
        key = key.lower()
        print(key)
        p.publish('user/cmd/control', key)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    p = MqttPublisher()
    while not p.connected:
        pass
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

