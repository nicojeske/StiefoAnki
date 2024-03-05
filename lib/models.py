from typing import List


class Curve():
    start: tuple[float, float]
    control1: tuple[float, float]
    control2: tuple[float, float]
    end: tuple[float, float]

    def scale(self, factor: float):
        self.start = (self.start[0] * factor, self.start[1] * factor)
        self.control1 = (self.control1[0] * factor, self.control1[1] * factor)
        self.control2 = (self.control2[0] * factor, self.control2[1] * factor)
        self.end = (self.end[0] * factor, self.end[1] * factor)

    def translate(self, x: float, y: float):
        self.start = (self.start[0] + x, self.start[1] + y)
        self.control1 = (self.control1[0] + x, self.control1[1] + y)
        self.control2 = (self.control2[0] + x, self.control2[1] + y)
        self.end = (self.end[0] + x, self.end[1] + y)

    def __init__(self, start, control1, control2, end):
        self.start = start
        self.control1 = control1
        self.control2 = control2
        self.end = end

    def __str__(self):
        return f"Curve({self.start}, {self.control1}, {self.control2}, {self.end})"
    
class Word():
    text: str
    curves: List[Curve]

    width: float

    def scale(self, factor: float):
        for curve in self.curves:
            curve.scale(factor)

    def translate(self, x: float, y: float):
        for curve in self.curves:
            curve.translate(x, y)

    def __init__(self, text: str, curves: List[Curve], width: float):
        self.text = text
        self.curves = curves
        self.width = width

    def __str__(self):
        return f"Word({self.text}, {self.curves})"