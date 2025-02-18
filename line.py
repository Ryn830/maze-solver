from tkinter import Canvas
from point import Point


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f"{self.start} to {self.end}"

    def draw(self, canvas: Canvas, color: str):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=color, width=2
        )
