import tkinter as tk
import tkinter.ttk as ttk
import pyperclip


Core = tk.Tk()
Core.title("ClipboardCommander")
Core.geometry("400x600")
Core.grid_columnconfigure(0, weight=1)
Core.grid_rowconfigure(0, weight=1)
Core.grid_rowconfigure(1, weight=1)
Core.configure(background="#31353D")


Boards = []


class Board:

    def __init__(self):
        self.Content = tk.StringVar()
        self.Content.set("")
        self.BoardFrame = ttk.LabelFrame(Core, text="Board", relief="groove")
        self.BoardContent = ttk.Label(self.BoardFrame, textvariable=self.Content, anchor="center")
        self.BoardClearButton = ttk.Button(self.BoardFrame, text="Clear", command=lambda: Board.Clear(self))
        self.BoardSwapButton = ttk.Button(self.BoardFrame, text="Swap", command=lambda: Board.Swap(self, Content))
        Boards.append(self)
        self.Display()

    def Display(self):
        self.BoardFrame.grid(sticky="S")
        self.BoardContent.grid()
        self.BoardClearButton.grid(row=1, column=0, sticky="W")
        self.BoardSwapButton.grid(row=1, column=1, sticky="E")

    def Clear(self):
        self.BoardFrame.grid_forget()
        Boards.remove(self)

    def Swap(self, content):
        dummy = self.Content.get()
        self.Content.set(content.get())
        content.set(dummy)
        pyperclip.copy(content.get())
        if self.Content.get() == " ":
            self.Clear()


def CreateNewBoard():
    if Content.get() == "" or Content.get() == " ":
        return
    new_board = Board()
    new_board.Swap(Content)


def ClipboardClear():
    pyperclip.copy(" ")


Content = tk.StringVar()
Content.set("")
MainBoardFrame = ttk.LabelFrame(Core, text="Clipboard Contents", relief="groove")
MainBoardContent = ttk.Label(MainBoardFrame, textvariable=Content, anchor="center")
MainBoardClearButton = ttk.Button(MainBoardFrame, text="Clear", command=lambda: ClipboardClear())
MainBoardSwapButton = ttk.Button(MainBoardFrame, text="Swap", command=lambda: CreateNewBoard())

MainBoardFrame.grid(sticky="N")
MainBoardContent.grid()
MainBoardClearButton.grid(row=1, column=0, sticky="W")
MainBoardSwapButton.grid(row=1, column=1, sticky="E")


def refresh():
    temp = pyperclip.paste()
    Content.set(temp)
    Core.after(250, refresh)


refresh()
Core.mainloop()
