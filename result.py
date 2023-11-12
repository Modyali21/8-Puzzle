import tkinter as tk
from tkinter.font import Font
from AStar import aStar, getHeuristic
from Node import Node
from steps import StepsFrame
from mybutton import MyButton, ButtonStyle, Borders


class ResultsFrame(tk.Frame):
    title: tk.Label
    back: MyButton
    showStepsBtn: MyButton
    results: tk.Text
    previousScreen: tk.Frame
    goalNode: Node

    def __init__(
        self,
        parent,
        expanded: int,
        goalDepth: int,
        maxDepth: int,
        time: float,
        goalNode: Node = None,
        previousScreen: tk.Frame = None,
    ):
        super().__init__(master=parent, padx=10, pady=10, background="#30475E")
        self.previousScreen = previousScreen
        self.goalNode = goalNode
        self.title = tk.Label(
            self,
            text="Result",
            font=Font(family="Small Fonts", size=40),
            background="#30475E",
            foreground="white",
        )
        self.back = MyButton(
            master=self,
            txt="< Go back",
            font=Font(family="Small Fonts", size=20),
            buttonColor="#30475E",
            textColor="white",
            hover=True,
            hoverStyle={"textColor": "#F05454"},
            width=10,
            height=10,
            command=self.goBack,
        )
        self.results = tk.Text(
            self,
            font=Font(family="@Yu Gothic UI Semibold", size=20),
            background="#DDDDDD",
            foreground="#222831",
            width=25,
            height=8,
            relief="flat",
            highlightthickness=5,
            highlightcolor="#222831",
            highlightbackground="#222831",
            selectbackground="#F05454",
        )
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
        self.showStepsBtn = MyButton(
            master=self,
            txt="Show steps",
            **btnStyle,
            command=self.showSteps
        )
        self.results.insert("end", "number of expanded nodes:\n", "title")
        self.results.insert("end", f"{expanded}\n", "number")

        self.results.insert("end", "Depth of the goal:\n", "title")
        self.results.insert("end", f"{goalDepth}\n", "number")

        self.results.insert("end", "Max depth of the search:\n", "title")
        self.results.insert("end", f"{maxDepth}\n", "number")

        self.results.insert("end", "Time taken:\n", "title")
        self.results.insert("end", f"{time:.10f}", "number")

        self.results.configure(state="disabled")
        self.results.tag_config(
            "number", justify="center", background="#DDDDDD", selectbackground="#F05454"
        )
        self.results.tag_config(
            "title",
            justify="center",
            background="#222831",
            foreground="white",
            selectbackground="#F05454",
        )

        self.back.pack(side="top", anchor=("nw"), pady=5)
        self.title.pack(side="top", anchor="center", expand=True, padx=10, pady=10)
        self.results.pack(side="top", anchor="center", expand=True, pady=10, padx=10)
        self.showStepsBtn.pack(side="top", anchor="center", expand=True)

    def goBack(self):
        if self.previousScreen is not None:
            self.destroy()
            self.previousScreen.pack(fill="both", expand=True, anchor="center")
            self.master.update()
            self.master.minsize(
                self.previousScreen.winfo_reqwidth(),
                self.previousScreen.winfo_reqheight(),
            )

    def showSteps(self):
        step = StepsFrame(
            parent=self.master,
            path=self.goalNode.formPath(),
            depth=self.goalNode.depth,
            previousScreen=self,
        )
        self.pack_forget()
        step.pack(anchor="center", expand=True, fill="both")
        self.master.update()
        self.master.minsize(step.winfo_reqwidth(), step.winfo_reqheight())


if __name__ == "__main__":
    x = tk.Tk()
    x.title("AI assignment 1")
    ResultsFrame(x, 181440, 31, 31, 0.123456789222).pack(
        anchor="center", expand=True, fill="both"
    )
    x.update()
    x.minsize(width=x.winfo_width(), height=x.winfo_height())
    x.mainloop()
