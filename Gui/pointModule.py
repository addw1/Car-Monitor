from PyQt5.QtWidgets import QLabel, QVBoxLayout, QFrame, QStackedLayout
from pointModule_ui import PointModuleUi
import vtk, numpy, os
from vtk.util.numpy_support import numpy_to_vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class PointModule(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = PointModuleUi()
        self.ui.setupUi(self)

        self.frame = self.ui.frame
        self.box = self.ui.comboBox
        self.box.currentIndexChanged.connect(self.change_point)
        self.vtkWidget = None
        filename = os.path.abspath("./Gui/point/bunny.txt")
        self.show_point(filename, self.frame, 1)

    def change_point(self):
        print(1111)
        filename = os.path.abspath("./Gui/point/point3D.txt")
        self.show_point(filename, self.frame, 0)

    def show_point(self, filename, frame, flag):
        if flag == 1:
            vl = QVBoxLayout()
            self.vtkWidget = QVTKRenderWindowInteractor(frame)
            vl.addWidget(self.vtkWidget)
            frame.setLayout(vl)

        ren = vtk.vtkRenderer()
        ren.SetBackground(0.94, 0.94, 0.94)
        self.vtkWidget.GetRenderWindow().AddRenderer(ren)
        iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        source_data = numpy.loadtxt(filename)
        points = vtk.vtkPoints()
        points.SetData(numpy_to_vtk(source_data))
        polydata = vtk.vtkPolyData()
        polydata.SetPoints(points)
        # 顶点相关的 filter
        vertex = vtk.vtkVertexGlyphFilter()
        vertex.SetInputData(polydata)
        # mapper 实例
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(vertex.GetOutputPort())
        # actor 实例
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # 红色点显示

        actor.GetProperty().SetColor(0, 0, 0)

        ren.AddActor(actor)
        ren.ResetCamera()


        iren.Initialize()