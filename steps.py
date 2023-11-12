from queue import LifoQueue
import tkinter as tk
from tkinter.font import Font
from mybutton import MyButton, ButtonStyle, Borders


class StepsFrame(tk.Frame):
    stateLabels: list[tk.Label]
    labelsFrame: tk.Frame
    back: MyButton
    nextBtn: MyButton
    prevBtn: MyButton
    bottomBarFrame: tk.Frame
    bottomLabel: tk.Label
    prevStack: LifoQueue
    current: list[int]
    nextStack: LifoQueue
    step: int
    numberOfSteps: int
    previousScreen: tk.Frame

    def __init__(
        self, parent, path: LifoQueue, depth: int, previousScreen: tk.Frame = None
    ):
        super().__init__(master=parent, padx=10, pady=10, background="#30475E")
        self.stateLabels = []
        self.previousScreen = previousScreen
        self.nextStack = path
        self.current = self.nextStack.get()
        self.prevStack = LifoQueue()
        self.numberOfSteps = depth
        self.step = 0
        # labelsFrame Preparation
        self.labelsFrame = tk.Frame(
            self, width=300, height=300, background="#222831", padx=3, pady=3
        )

        self.labelsFrame.grid_propagate(0)
        self.labelsFrame.rowconfigure([0, 1, 2], weight=1)
        self.labelsFrame.columnconfigure([0, 1, 2], weight=1)
        for i in range(9):
            tmp = tk.Label(
                self.labelsFrame,
                background="#DDDDDD" if self.current[i] != 0 else "#222831",
                foreground="#222831" if self.current[i] != 0 else "#222831",
                text=self.current[i],
                relief="flat",
                justify="center",
                font=Font(family="Small Fonts", size=30),
            )
            self.stateLabels.append(tmp)
            tmp.grid(row=i // 3, column=i % 3, sticky="NSEW", padx=3, pady=3)

        # bottom bar Frame
        self.bottomBarFrame = tk.Frame(self, background="#30475E")
        self.bottomLabel = tk.Label(
            self.bottomBarFrame,
            text=f"Step {self.step} of {self.numberOfSteps}",
            justify="center",
            anchor="center",
            font=Font(family="Small Fonts", size=30),
            foreground="white",
            background="#30475E",
            width=len(f"Step {self.numberOfSteps} of {self.numberOfSteps}"),
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
        self.nextBtn = MyButton(
            master=self.bottomBarFrame, txt="next >", **btnStyle, command=self.nextClick
        )
        self.prevBtn = MyButton(
            master=self.bottomBarFrame, txt="< prev", **btnStyle, command=self.prevClick
        )
        self.back = MyButton(
            master=self,
            txt="< Go back",
            font=btnStyle["font"],
            buttonColor="#30475E",
            textColor="white",
            hover=True,
            hoverStyle={"textColor": "#F05454"},
            width=10,
            height=10,
            command=self.goBack,
        )

        self.back.pack(side="top", anchor=("nw"), pady=5)
        self.labelsFrame.pack(anchor="center", expand=True, side="top")
        self.bottomBarFrame.pack(expand=True, anchor="center", side="top", pady=10)
        self.prevBtn.pack(padx=20, side="left", anchor="center")
        self.bottomLabel.pack(side="left")
        self.nextBtn.pack(padx=20, side="left", anchor="center")

        self.prevBtn.disable()
        if self.nextStack.empty():
            self.nextBtn.disable()

    def updatestateLabels(self, state: list[int]):
        i = 0
        for item in state:
            self.stateLabels[i].configure(text=item)
            if item == 0:
                self.stateLabels[i].configure(
                    foreground="#222831", background="#222831"
                )
            else:
                self.stateLabels[i].configure(
                    foreground="#222831", background="#DDDDDD"
                )
            i += 1
        self.bottomLabel.configure(text=f"Step {self.step} of {self.numberOfSteps}")

    def nextClick(self):
        self.step += 1
        if self.prevStack.empty():
            self.prevBtn.enable()
        self.prevStack.put(self.current)
        self.current = self.nextStack.get()
        if self.nextStack.empty():
            self.nextBtn.disable()
        self.updatestateLabels(self.current)

    def prevClick(self):
        self.step -= 1
        if self.nextStack.empty():
            self.nextBtn.enable()
        self.nextStack.put(self.current)
        self.current = self.prevStack.get()
        if self.prevStack.empty():
            self.prevBtn.disable()
        self.updatestateLabels(self.current)

    def goBack(self):
        if self.previousScreen is not None:
            self.previousScreen.pack(fill="both", expand=True, anchor="center")
            self.pack_forget()
            self.master.update()
            self.master.minsize(
                self.previousScreen.winfo_reqwidth(),
                self.previousScreen.winfo_reqheight(),
            )


if __name__ == "__main__":
    x = tk.Tk()
    x.title("Enter initial state")
    test = LifoQueue()
    test.put([1, 2, 3, 4, 5, 6, 7, 8, 0])
    StepsFrame(x, test, 1).pack(anchor="center", expand=True, fill="both")
    x.update()
    x.minsize(width=x.winfo_width(), height=x.winfo_height())
    print(x.winfo_width(), x.winfo_height())
    print(x.winfo_width(), x.winfo_height())
    x.mainloop()
