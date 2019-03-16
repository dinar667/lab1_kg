# coding: utf-8

from math import cos, sin, radians
from typing import Dict

from PyQt5 import QtCore, QtWidgets

from core.points import Point2D, Point3D
from gui.axonometric_plane_system import AxonometricPlaneSystem
from gui.complex_plane_system import ComplexPlaneSystem
from gui.settings import *
from gui.ui_main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        self.axis_length: int = 150

        self._origin: Point2D = Point2D(0, 0)

        self.x: int = 0
        self.y: int = 0
        self.z: int = 0

        self.alpha: float = 0
        self.beta: float = 0
        self.gamma: float = 0

        # точки 3D
        self.points_3d: Dict[str, Point3D] = {}

        # точки для аксонометрического чертежа
        self.points_2d_ax: Dict[str, QtCore.QPointF] = {}

        # точки для комплексного чертежа
        self.points_2d_ep: Dict[str, QtCore.QPointF] = {}

        self.aps = AxonometricPlaneSystem(self.aWidget)
        self.cps = ComplexPlaneSystem(self.cWidget)

        self.xSlider.setValue(POINT_X)
        self.ySlider.setValue(POINT_Y)
        self.zSlider.setValue(POINT_Z)

        self.xAngleSlider.setValue(ANGLE_ALPHA)
        self.yAngleSlider.setValue(ANGLE_BETA)
        self.zAngleSlider.setValue(ANGLE_GAMMA)

    @QtCore.pyqtSlot(int, name="on_x_changed")
    def on_x_changed(self, value):
        self.xField.setText(f"{value}")
        self.x = value
        self.on_coordinate_changed()

    @QtCore.pyqtSlot(int, name="on_y_changed")
    def on_y_changed(self, value):
        self.yField.setText(f"{value}")
        self.y = value
        self.on_coordinate_changed()

    @QtCore.pyqtSlot(int, name="on_z_changed")
    def on_z_changed(self, value):
        self.zField.setText(f"{value}")
        self.z = value
        self.on_coordinate_changed()

    @QtCore.pyqtSlot(int, name="on_x_angle_changed")
    def on_x_angle_changed(self, value: int) -> None:
        self.xAngleField.setText(f"{value}")
        self.alpha = radians(value)
        self.on_angle_changed()

    @QtCore.pyqtSlot(int, name="on_y_angle_changed")
    def on_y_angle_changed(self, value: int) -> None:
        self.yAngleField.setText(f"{value}")
        self.beta = radians(value)
        self.on_angle_changed()

    @QtCore.pyqtSlot(int, name="on_z_angle_changed")
    def on_z_angle_changed(self, value: int) -> None:
        self.zAngleField.setText(f"{value}")
        self.gamma = radians(value)
        self.on_angle_changed()

    def on_coordinate_changed(self) -> None:
        # заполняем массив координат
        self.fill_3d_coordinates()

        # пересчитываем точки всех чертежей
        self.recalculate_all()

        # отрисовываем результат
        self.draw_result()

        # self.aWidget.grab().save("image.png")

    def on_angle_changed(self) -> None:
        # заполняем массив координат
        self.fill_3d_coordinates()

        # пересчитываем точки аксонометрического чертежа
        self.recalculate_ax_coordinates()

        # отрисовываем результат (только аксонометрический чертеж)
        self.draw_ax_plane()

    def fill_3d_coordinates(self) -> None:
        x, y, z = self.x, self.y, self.z

        self.points_3d["T"] = Point3D(x, y, z)
        self.points_3d["0"] = Point3D(0, 0, 0)

        self.points_3d["T1"] = Point3D(x, y, 0)
        self.points_3d["T2"] = Point3D(0, y, z)
        self.points_3d["T3"] = Point3D(x, 0, z)

        self.points_3d["TX"] = Point3D(x, 0, 0)
        self.points_3d["TY"] = Point3D(0, y, 0)
        self.points_3d["TZ"] = Point3D(0, 0, z)

        self.points_3d["-X"] = Point3D(-self.axis_length, 0, 0)
        self.points_3d["+X"] = Point3D(self.axis_length, 0, 0)

        self.points_3d["-Y"] = Point3D(0, -self.axis_length, 0)
        self.points_3d["+Y"] = Point3D(0, self.axis_length, 0)

        self.points_3d["-Z"] = Point3D(0, 0, -self.axis_length)
        self.points_3d["+Z"] = Point3D(0, 0, self.axis_length)

    def from_3d_to_ax_scene(self, point: Point3D) -> QtCore.QPointF:
        x: int = self._origin.x + (
                + point.x * cos(self.alpha)
                + point.y * cos(self.beta)
                + point.z * cos(self.gamma)
        )

        y: int = self._origin.y - (
                + point.x * sin(self.alpha)
                + point.y * sin(self.beta)
                + point.z * sin(self.gamma)
        )

        return QtCore.QPointF(x, y)

    def recalculate_all(self) -> None:
        self.recalculate_ax_coordinates()
        self.recalculate_ep_coordinates()

    def recalculate_ax_coordinates(self) -> None:
        """
        Пересчитываем из 3D в координаты экрана
        (для аксонометрического чертежа)
        """

        for pname, point in self.points_3d.items():
            self.points_2d_ax[pname] = self.from_3d_to_ax_scene(point)

    def recalculate_ep_coordinates(self) -> None:
        """ Пересчитываем из 3D в координаты чертежа """

        self.points_2d_ep["0"] = QtCore.QPointF(0, 0)
        self.points_2d_ep["+X -Y"] = QtCore.QPointF(-self.axis_length, 0)
        self.points_2d_ep["-X +Y"] = QtCore.QPointF(self.axis_length, 0)
        self.points_2d_ep["+Z -Y"] = QtCore.QPointF(0, -self.axis_length)
        self.points_2d_ep["-Z +Y"] = QtCore.QPointF(0, self.axis_length)

        self.points_2d_ep["T1"] = QtCore.QPointF(-self.x, self.y)
        self.points_2d_ep["T2"] = QtCore.QPointF(-self.x, -self.z)
        self.points_2d_ep["T3"] = QtCore.QPointF(self.y, -self.z)

        self.points_2d_ep["TX"] = QtCore.QPointF(-self.x, 0)
        self.points_2d_ep["TY1"] = QtCore.QPointF(0, self.y)
        self.points_2d_ep["TY3"] = QtCore.QPointF(self.y, 0)
        self.points_2d_ep["TZ"] = QtCore.QPointF(0, -self.z)

    def draw_result(self) -> None:
        self.draw_ax_plane()
        self.draw_ep_plane()

    def draw_ax_plane(self) -> None:
        self.aps.draw_with_points(self.points_2d_ax)

    def draw_ep_plane(self) -> None:
        self.cps.draw_with_points(self.points_2d_ep)
