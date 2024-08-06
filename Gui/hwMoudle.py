
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QFrame, QStackedLayout
from hwModule_ui import HwModuleUi
import vtk, os
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class HwModule(QFrame):
    def __init__(self):
        # 加载UI界面
        super().__init__()
        self.ui = HwModuleUi()
        self.ui.setupUi(self)

        # 初始化组件
        self.modelFrame = self.ui.frame
        self.modelLayout = QStackedLayout()
        self.modelFrame.setLayout(self.modelLayout)
        self.text = self.ui.textBrowser
        self.carBtn = self.ui.pushButton_4
        self.wheelBtn = self.ui.pushButton_6
        self.radarBtn = self.ui.pushButton_3
        self.jetsonBtn =self.ui.pushButton_5

        # 设置界面切换
        self.carBtn.clicked.connect(self.to_car)
        self.wheelBtn.clicked.connect(self.to_wheel)
        self.radarBtn.clicked.connect(self.to_radar)
        self.jetsonBtn.clicked.connect(self.to_jetson)

        # 设置 3d模型
        self.frame =QFrame()
        self.modelLayout.addWidget(self.frame)
        filename = os.path.abspath("./Gui/stl/base_link.STL")
        self.add_model(filename, self.frame)
        self.frame_1 = QFrame()
        self.modelLayout.addWidget(self.frame_1)
        filename = os.path.abspath("./Gui/stl/right_rear_link.STL")
        self.add_model(filename, self.frame_1)
        self.frame_2 = QFrame()
        self.modelLayout.addWidget(self.frame_2)
        filename = os.path.abspath("./Gui/stl/radar.STL")
        self.add_model(filename, self.frame_2)
        self.frame_3 = QFrame()
        self.modelLayout.addWidget(self.frame_3)
        filename = os.path.abspath("./Gui/stl/jetson.STL")
        self.add_model(filename, self.frame_3)
        # 显示汽车模型
        self.to_car()

    # 添加模型
    def add_model(self, filename, frame):
        vl = QVBoxLayout()
        vtkWidget = QVTKRenderWindowInteractor(frame)
        vl.addWidget(vtkWidget)
        ren = vtk.vtkRenderer()
        ren.SetBackground(0.94, 0.94, 0.94)
        vtkWidget.GetRenderWindow().AddRenderer(ren)
        iren = vtkWidget.GetRenderWindow().GetInteractor()
        reader = vtk.vtkSTLReader()
        reader.SetFileName(filename)
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(reader.GetOutputPort())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        ren.AddActor(actor)
        ren.ResetCamera()
        frame.setLayout(vl)
        iren.Initialize()

    # 切换到汽车介绍
    def to_car(self):
        self.modelLayout.setCurrentIndex(0)
        self.text.setText("HUNTERSE是一款阿克曼模型可编程UGV（ UNMANNED GROUND VEHICLE ），它是一款采用阿克曼转向设"
                        "计的底盘，具有和汽车类似的特征，在普通水泥、柏油路上优势明显。相对于四轮差速底盘，HUNTERSE具有更高"
                        "的载重能力，能达到更高的运动速度，同时对结构和轮胎的磨损更小，适合长时间的工作。")

    # 切换到车轮介绍
    def to_wheel(self):
        self.modelLayout.setCurrentIndex(1)
        self.text.setText("轮胎气压定期检查，轮胎气压保持在0.8BAR左右。\n"
                        "轮胎磨损严重或者爆胎，请及时更换。\n"
                        "如果长时间不使用电池，需要按照2到3个月对电池进行周期性充电。")

    # 切换到雷达介绍
    def to_radar(self):
        self.modelLayout.setCurrentIndex(2)
        self.text.setText("16线")

    # 切换到jetson介绍
    def to_jetson(self):
        self.modelLayout.setCurrentIndex(3)
        self.text.setText("jetson")