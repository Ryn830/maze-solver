from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height) -> None:
        self.root_widget = Tk()
        self.root_widget.title = "Title"
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas()
        self.canvas.pack()

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


def main():
    win = Window(800, 600)
    win.wait_for_close()


main()
