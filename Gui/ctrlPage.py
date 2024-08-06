from ctrlPage_ui import CtrlPageUi
from PyQt5.QtWidgets import QFrame


class CtrlPage(QFrame):
    def __init__(self):
        super().__init__()
        # 加载UI文件
        self.ui = CtrlPageUi()
        self.ui.setupUi(self)

