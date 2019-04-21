# coding: utf-8

from typing import Dict, Callable

from PyQt5 import QtCore, QtWidgets, QtGui


class BasePlaneSystem:
    def __init__(self, widget: QtWidgets.QWidget) -> None:
        self.widget: QtWidgets.QWidget = widget
        self.widget.paintEvent: Callable = self.paint_event
        self.widget.resizeEvent: Callable = self.resize_event

        # Радиус точки
        self.point_radius: int = 3

        # Ширина линии
        self.line_width: int = 2

        self.label_color = QtGui.QColor("black")
        self.label_pen = QtGui.QPen(
            self.label_color, self.line_width
        )

        # Координаты центра
        self.xhalf: int = 0
        self.yhalf: int = 0

        # Отступ надписи от линии (в пикселях)
        self.label_offset_x: int = 10
        self.label_offset_y: int = 15

        self.points: Dict[str, QtCore.QPointF] = {}

        self.pixmap: QtGui.QPixmap = QtGui.QPixmap(self.widget.size())

    @staticmethod
    def get_axis_line(
            start: QtCore.QPointF, end: QtCore.QPointF
    ) -> QtCore.QLineF:
        return QtCore.QLineF(start.x(), start.y(), end.x(), end.y())

    @staticmethod
    def draw_axis(
        painter: QtGui.QPainter, axis: QtCore.QLineF, pen, dash_pen
    ) -> None:
        painter.setPen(pen)
        painter.drawLine(0, 0, int(axis.x1()), int(axis.y1()))
        painter.setPen(dash_pen)
        painter.drawLine(0, 0, int(axis.x2()), int(axis.y2()))

    def draw_with_points(self, points: Dict[str, QtCore.QPointF]) -> None:
        self.points = points
        self.widget.repaint()

    def paint_event(self, event: QtGui.QPaintEvent) -> None:
        self.update_pixmap()

        painter = QtGui.QPainter(self.widget)
        painter.begin(self.widget)
        painter.drawPixmap(0, 0, self.pixmap)
        painter.end()

        event.accept()

    def update_pixmap(self) -> None:
        """ Здесь идет основная отрисовка на `pixmap` """
        raise NotImplementedError

    def resize_event(self, event: QtGui.QResizeEvent) -> None:
        self.xhalf = self.widget.width() // 2
        self.yhalf = self.widget.height() // 2

        self.pixmap = QtGui.QPixmap(self.widget.size())

        event.accept()

    def draw_points(self, painter: QtGui.QPainter) -> None:
        painter.setBrush(QtGui.QBrush(QtCore.Qt.white))
        painter.setBackgroundMode(QtCore.Qt.OpaqueMode)

        # Рисуем точки
        for point_name, point in self.points.items():
            painter.drawEllipse(point, self.point_radius, self.point_radius)
            self.draw_label(painter, point, point_name)

    def draw_label(self, painter, point: QtCore.QPointF, label: str) -> None:
        painter.drawText(
            QtCore.QPointF(
                point.x() + self.label_offset_x,
                point.y() + self.label_offset_y
            ),
            label
        )
