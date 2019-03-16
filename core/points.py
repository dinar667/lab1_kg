# coding: utf-8


class Point2D(object):
    def __init__(self, x: float = 0, y: float = 0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def __str__(self):
        return f"Point2D ({self._x}, {self._y})"

    def __add__(self, point):
        return Point2D(self._x + point.x, self._y + point.y)

    def __sub__(self, point):
        return Point2D(self._x - point.x, self._y - point.y)


class Point3D(Point2D):
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        super().__init__(x, y)

        self._z: float = z

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

    def __str__(self):
        return f"Point3D ({self._x}; {self._y}; {self._z})"

    def to_2d_xy(self):
        return Point2D(self._x, self._y)

    # Скалярное произведение точек
    def get_prod(self, point):
        return self._x * point.x + self._y * point.y + self._z * point.z

    # def __mul__(self, matrix: Matrix):
    #
    #     v = np.array([self.x, self.y, self.z, 1])
    #     result_matrix = np.dot(v, matrix.values)
    #
    #     x = result_matrix[0]
    #     y = result_matrix[1]
    #     z = result_matrix[2]
    #
    #     return Point3D(x, y, z)

    def __bool__(self) -> bool:
        return any((self.x, self.y, self.z))
