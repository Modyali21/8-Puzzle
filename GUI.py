import time
import tkinter as tk
from tkinter.font import Font
from AStar import aStar, getHeuristic
from BFS import bfs
from Node import Node
from result import ResultsFrame
from steps import StepsFrame
from mybutton import MyButton, ButtonStyle, Borders
from DFS import dfs

class StartFrame(tk.Frame):
    title: tk.Label
    solutionsMethods: list[str]
    currentSelected: int
    entries: list[tk.Entry]
    inputFrame: tk.Frame
    inputButton: MyButton

    def __init__(self, parent):
        super().__init__(master=parent, padx=10, pady=10, background="#30475E")
        self.currentSelected = 0
        self.solutionsMethods = ["BFS", "DFS", "A*", "A*2"]
        self.entries = []
        self.title = tk.Label(
            self,
            text="Enter the initial state:",
            justify="center",
            anchor="center",
            font=Font(family="Small Fonts", size=30),
            foreground="white",
            background="#30475E",
        )

        # inputFrame Preparation
        self.inputFrame = tk.Frame(
            self, width=300, height=300, background="#222831", padx=3, pady=3
        )

        self.inputFrame.grid_propagate(0)
        self.inputFrame.rowconfigure([0, 1, 2], weight=1)
        self.inputFrame.columnconfigure([0, 1, 2], weight=1)

        valdiation = self.register(self.validateInput)

        for i in range(9):
            tmp = tk.Entry(
                self.inputFrame,
                background="#DDDDDD",
                foreground="#222831",
                text="",
                relief="flat",
                justify="center",
                font=Font(family="Small Fonts", size=30),
                validate="key",
                validatecommand=(valdiation, "%P", "%W"),
            )
            self.entries.append(tmp)
            tmp.grid(row=i // 3, column=i % 3, sticky="NSEW", padx=3, pady=3)

        # General Btn Style
        btnStyle: ButtonStyle = {
            "buttonColor": "#F05454",
            "shadowColor": "#F05454",
            "textColor": "white",
            "font": Font(family="Small Fonts", size=20),
            "cornerRadius": 30,
            "shadowLength": 7,
            "borders": {"bottom": 3, "left": 3, "right": 3, "top": 3},
            "width": 70,
            "height": 70,
            "padx": 15,
            "buttonBorderColor": "#222831",
            "shadowBorderColor": "#222831",
        }
        self.title.bind("<Button-1>", lambda x: self.title.configure(text="Hello :3"))
        self.title.bind(
            "<Button-3>",
            lambda x: self.title.configure(text="Enter the initial state:"),
        )
        # optionFrame
        self.optionBarFrame = tk.Frame(self, background="#30475E")
        self.optionLabel = tk.Label(
            self.optionBarFrame,
            text=self.solutionsMethods[self.currentSelected],
            justify="center",
            anchor="center",
            font=Font(family="Small Fonts", size=30),
            foreground="white",
            background="#30475E",
            width=max([len(i) for i in self.solutionsMethods]),
        )
        self.nextButton = MyButton(
            master=self.optionBarFrame, txt=">", **btnStyle, command=self.nextClick
        )
        self.previousButton = MyButton(
            master=self.optionBarFrame, txt="<", **btnStyle, command=self.prevClick
        )
        # solveGame button
        self.inputButton = MyButton(
            master=self, txt="Solve the game", **btnStyle, command=self.solveTheGame
        )
        self.title.pack(pady=10)
        self.inputFrame.pack(expand=True, anchor="center")
        self.optionBarFrame.pack(expand=True, anchor="center", side="top", pady=10)
        self.previousButton.pack(padx=20, side="left", anchor="center")
        self.optionLabel.pack(side="left")
        self.nextButton.pack(padx=20, side="left", anchor="center")
        self.inputButton.pack(pady=10, expand=True, anchor="center")

    def nextClick(self):
        if self.currentSelected + 1 >= len(self.solutionsMethods):
            self.currentSelected = 0
        else:
            self.currentSelected += 1
        self.optionLabel.configure(text=self.solutionsMethods[self.currentSelected])

    def prevClick(self):
        if self.currentSelected - 1 < 0:
            self.currentSelected = len(self.solutionsMethods) - 1
        else:
            self.currentSelected -= 1
        self.optionLabel.configure(text=self.solutionsMethods[self.currentSelected])

    def validateInput(self, newText: str, widget: str):
        if newText == "":
            return True
        if not newText.isdigit() or len(newText) > 1 or newText == "9":
            return False
        for i in self.entries:
            if i.get() == newText:
                return False
        tmp = self.nametowidget(widget)
        tmp.tk_focusNext().focus()
        tmp.configure(background="#DDDDDD")
        return True

    def solveTheGame(self):
        valid = True
        for i in self.entries:
            if i.get() == "":
                i.configure(background="#FF7F7F")
                valid = False
        if valid:
            initialState = Node([int(i.get()) for i in self.entries])
            start = time.time()
            out = bfs(initialState)
            end = time.time()
            result = ResultsFrame(
                parent=self.master,
                expanded=out[1],
                goalDepth=out[2].depth,
                goalNode=out[2],
                time=(end - start),
                previousScreen=self,
                maxDepth=out[3],
            )
            self.pack_forget()
            result.pack(anchor="center", expand=True, fill="both")
            self.master.update()
            self.master.minsize(result.winfo_reqwidth(), result.winfo_reqheight())


x = tk.Tk()
x.title("AI assignment 1")
StartFrame(x).pack(anchor="center", expand=True, fill="both")
x.update()
x.minsize(width=x.winfo_width(), height=x.winfo_height())
x.mainloop()
