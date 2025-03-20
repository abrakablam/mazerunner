from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title("Mazerunner")
        self.__canvas = Canvas(self.__root, bg="dim grey", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

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



def main():
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == "__main__":
    main()

