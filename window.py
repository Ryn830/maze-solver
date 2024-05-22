from tkinter import Tk, BOTH, Canvas

from line import Line


class Window:
    def __init__(self, width, height) -> None:
        self.root_widget = Tk()
        self.root_widget.title = "Maze Solver"
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.root_widget, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)

        self.status_running = False

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.status_running = True
        while self.status_running:
            self.redraw()

    def close(self):
        self.status_running = False

    def draw_line(self, line: Line, color="black"):
        line.draw(self.canvas, color)
