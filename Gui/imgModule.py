
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QFrame
from imgModule_ui import ImgModuleUi
import random

class ImgModule(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = ImgModuleUi()
        self.ui.setupUi(self)
        self.count = 0
        self.imgLabel = self.ui.label
        self.fpsLabel = self.ui.label_2
        self.button = self.ui.pushButton

    # fps无实际意义，为随机给值
    def set_fps(self, value):
        self.count = self.count + 1
        if self.count == 10:
            if random.random() > 0.5:
                value = 20
            else:
                value = 19
            self.fpsLabel.setText(str(value))
            self.count = 0


