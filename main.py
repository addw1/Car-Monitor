
# 如果执行成功，没有任何错误提示，则表明环境搭建成功

from PyQt5.QtWidgets import QApplication


import sys
from mainWindow import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()

    main_window.show()

    app.exec()
