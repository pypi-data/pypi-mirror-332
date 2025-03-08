import math
from typing import *
import builtins
import numpy as np
from numpy import sqrt, sin
from numpy.ma.core import arccos

from pryttier.tools import isDivisibleBy

PI = 2 * arccos(0)
Degrees = PI / 180


def summation(n: float | int, i: float | int, expr: Callable) -> float:
    total = 0
    for j in range(n, i + 1):
        total += expr(j)
    return total


def product(n: int, i: int, expr: Callable) -> float:
    total = 1
    for j in range(n, i):
        total *= expr(j)
    return total


def clamp(num: float, low: float, high: float) -> float:
    if num < low:
        return low
    if num > high:
        return high
    return num

def sign(num: float) -> int:
    return int(num / abs(num))

def factorial(num: int) -> int:
    if num == 0:
        return 1
    if num == 1:
        return 1
    return num * factorial(num - 1)

def mapRange(value: int | float,
             min1: float,
             max1: float,
             min2: float,
             max2: float) -> float:
    return (value - min1) / (max1 - min1) * (max2 - min2) + min2


def isPrime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def getFactors(num: int):
    factors = []
    for i in range(1, num + 1):
        if num | isDivisibleBy | i:
            factors.append(i)

    return factors


def radToDeg(num: float):
    return num * (180 / PI)


def degToRad(num: float):
    return num * (PI / 180)

def getDigits(num: int):
    return [int(i) for i in list(str(num))]

class Vector2:
    def __init__(self,
                 x: float | int,
                 y: float | int):
        self.xy = (x, y)
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other: Self) -> Self:
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | int) -> Self:
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other: float | int):
        return Vector2(self.x / other, self.y / other)

    def __iter__(self):
        return iter([self.x, self.y])

    def magnitude(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def normalize(self) -> Self:
        return Vector2(self.x / self.magnitude(), self.y / self.magnitude())

    def toInt(self):
        return Vector2(int(self.x), int(self.y))

    # ---Class Methods---
    @classmethod
    def zero(cls):
        return Vector2(0, 0)

    @classmethod
    def distance(cls, a: Self, b: Self):
        dx = b.x - a.x
        dy = b.y - a.y
        return math.sqrt(dx * dx + dy * dy)

    @classmethod
    def dot(cls, a: Self, b: Self):
        return Vector2(a.x * b.x, a.y * b.y)

    @classmethod
    def cross(cls, a: Self, b: Self):
        return a.x * b.y - a.y * b.x

    @classmethod
    def angleBetween(cls, a: Self, b: Self):
        dotProduct = cls.dot(a, b)
        magA = a.magnitude()
        magB = b.magnitude()
        return math.acos(dotProduct / (magA * magB))

    @classmethod
    def interpolate(cls, a: Self, b: Self, t: float):
        v = b - a
        pdx = a.x + v.x * t
        pdy = a.y + v.y * t
        return Vector2(pdx, pdy)

class Vector3:
    def __init__(self,
                 x: float | int,
                 y: float | int,
                 z: float | int):
        self.xyz = (x, y, z)
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other: Self) -> Self:
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Self) -> Self:
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: float | int) -> Self:
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other: float | int):
        return Vector3(self.x / other, self.y / other, self.z / other)

    def __iter__(self):
        return iter([self.x, self.y, self.z])

    def magnitude(self):
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def normalize(self) -> Self:
        return Vector3(self.x / self.magnitude(), self.y / self.magnitude(), self.z / self.magnitude())

    def toInt(self):
        return Vector3(int(self.x), int(self.y), int(self.z))

    # ---Class Methods---
    @classmethod
    def zero(cls):
        return Vector3(0, 0, 0)

    @classmethod
    def distance(cls, a: Self, b: Self):
        dx = b.x - a.x
        dy = b.y - a.y
        dz = b.z - a.z
        return math.sqrt(dx * dx + dy * dy + dz * dz)

    @classmethod
    def dot(cls, a: Self, b: Self):
        return Vector3(a.x * b.x, a.y * b.y, a.z * a.z)

    @classmethod
    def cross(cls, a: Self, b: Self) -> Self:
        i = a.y * b.z - a.z * b.y
        j = a.z * b.x - a.x * b.z
        k = a.x * b.y - a.y * b.x
        return Vector3(i, j, k)

    @classmethod
    def angleBetween(cls, a: Self, b: Self):
        dotProduct = cls.dot(a, b)
        magA = a.magnitude()
        magB = b.magnitude()
        return math.acos(dotProduct / (magA * magB))


    @classmethod
    def interpolate(cls, a: Self, b: Self, t: float):
        v = b - a
        pdx = a.x + v.x * t
        pdy = a.y + v.y * t
        pdz = a.z + v.z * t
        return Vector3(pdx, pdy, pdz)

def closestFromArrayNumber(arr: Sequence[float], num: float | int):
    def difference(a):
        return abs(a - num)

    return min(arr, key=difference)

def closestFromArrayVec2(arr: Sequence[Vector2], num: Vector2):
    def difference(a: Vector2):
        return Vector2(abs(a.x - num.x), abs(a.y - num.y)).magnitude

    return min(arr, key=difference)

def closestFromArrayVec3(arr: Sequence[Vector3], num: Vector3):
    def difference(a: Vector3):
        return Vector3(a.x - num.x, a.y - num.y, a.z - num.z).magnitude

    return min(arr, key=difference)

def arrayToVec2array(arr: Sequence[Sequence[int]]):
    result = []
    for i in arr:
        if len(i) != 2:
            raise Exception("length has to be 2")
        else:
            result.append(Vector2(*i))
    return result

def arrayToVec3array(arr: Sequence[Sequence[int]]):
    result = []
    for i in arr:
        if len(i) != 3:
            raise Exception("length has to be 3")
        else:
            result.append(Vector3(*i))
    return result


class Matrix:
    def __init__(self, r, c):
        self.rows = r
        self.cols = c
        self.matrix = np.zeros([r, c])

    def set(self, mat: np.ndarray | list[list[int | float]]):
        matRows = len(mat)
        matCols = len(mat[0])
        if matRows == self.rows and matCols == self.cols:
            self.matrix = mat
        else:
            raise ValueError(f"Expected matrix of dimensions ({self.rows}, {self.cols}) but got ({matRows}, {matCols})")

    def __repr__(self):
        txt = [""] #┌┘└┐
        for i in range(self.rows):
            row = f"|{[int(self.matrix[i][j]) for j in range(self.cols)]}|\n"
            row = row.replace("[","").replace("]","").replace(",","")
            txt.append(row)
        return "".join(txt)

    def __getitem__(self, item: tuple[int, int] | int):
        if type(item) == int:
            return self.matrix[item]
        elif type(item) == tuple:
            return self.matrix[item[0]][item[1]]

    def __setitem__(self, key: tuple[int, int], value: int | float):
        self.matrix[key[0]][key[1]] = value

    def __invert__(self):
        newMat = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                newMat[j][i] = self.matrix[i][j]
        return newMat

    def __matmul__(self, other: Self):
        if self.cols != other.rows:
            raise TypeError("Number of columns of the first matrix must be equal to number of rows of the second matrix")
        mat = Matrix(self.rows, other.cols)
        mat.matrix = np.dot(self.matrix, other.matrix)
        return mat

    # Class Methods
    @classmethod
    def identity(cls, r, c):
        mat = Matrix(r, c)
        for i in range(r):
            for j in range(c):
                if i == j: mat.matrix[i][j] = 1
        return mat


def matToVec(m: Matrix):
    if m.cols == 2:
        return Vector2(float(m[0, 0]), float(m[0, 1]))
    elif m.cols == 3:
        return Vector3(float(m[0, 0]), float(m[0, 1]), float(m[0, 2]))

def vecToMat(v: Vector2 | Vector3):
    if type(v) == Vector2:
        mat = Matrix(1, 2)
        mat.set([[v.x, v.y]])
    elif type(v) == Vector3:
        mat = Matrix(1, 3)
        mat.set([[v.x, v.y, v.z]])
    else:
        return None
    return mat