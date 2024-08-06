
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFileDialog,QPushButton
import os


class CloudWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.qv = QVBoxLayout()
        self.btn = QPushButton()
        self.btn.setText("Test")
        self.qv.addWidget(self.btn)
        self.btn.clicked.connect(self.open_file)
        self.setLayout(self.qv)
    def open_file(self):
        fileName, fileType = QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(),
                                                                   "All Files(*);;Text Files(*.txt)")
        print(fileName)
        print(fileType)


