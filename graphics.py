from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title("Mazerunner")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="dim grey", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        
        while self.__running == True:
            self.redraw()
        print("Window closed. Goodbye.")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="red"):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y) -> None:
        # Setting intial coordinates, x = left y = top of screen
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2 ) -> None:
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="grey"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )


