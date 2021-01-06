from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import turtle
import random

# Color values
RED = '#EF476F'         # Color While Comparing
GREEN = '#06D6A0'       # Color After Sorted
BLUE = '#118AB2'        # Initial Color

bars = []
values = list(range(10))
random.shuffle(values)
algorithms = ['Bubble Sort', 'Insertion Sort', 'Selection Sort']

# Tkinter Window
root = Tk()
root.title("Sorting Algorithm Visualizer")
root.geometry("400x300")
root.resizable(0, 0)

# Main canvas
canvas = Canvas(root, width=400, height=580, bg="white")
canvas.grid(row=1, columnspan=66, padx=0, pady=0)

#Base class for bars
class Bar(turtle.RawTurtle):
    def __init__(self, canvas, val, color=BLUE):
        turtle.RawTurtle.__init__(self, canvas=canvas, visible=TRUE)
        self.val = val
        self.shape('square')
        self.shapesize(val*1.5+3, 1)
        self.fillcolor(color)
        self.pencolor(color)
        self.penup()

# Create 10 bars
for i in range(10):
    bar = Bar(canvas, values[i])
    bar.setx((i-5)*30)
    bar.sety(20)
    bars.append(bar)

#Helper Functions
def changeColor(bs, color):
    bs[0].fillcolor(color)
    bs[0].color(color)
    bs[1].fillcolor(color)
    bs[1].color(color)

def completed():
    for i in range(len(bars)):
        bars[i].fillcolor(GREEN)
        bars[i].color(GREEN)
    start_btn["state"] = NORMAL
    random_btn["state"] = NORMAL

def swap(a: int, b: int):
    posA = bars[a].pos()
    posB = bars[b].pos()
    bars[b].setposition(posA)
    bars[a].setposition(posB)
    bars[a].fillcolor(BLUE)
    bars[a].color(BLUE)
    bars[b].fillcolor(BLUE)
    bars[b].color(BLUE)
    bars[a], bars[b] = bars[b], bars[a]

#Algorithms
def bubbleSort():
    for i in range(len(bars)-1, 0, -1):
        for j in range(i):
            changeColor([bars[j],bars[j+1]],RED)
            if bars[j].val > bars[j+1].val:
                swap(j, j+1)
            changeColor([bars[j],bars[j+1]],BLUE)
    completed()

def insertionSort():
    for i in range(1,len(bars)):
        val = bars[i].val
        j = i
        while  j > 0 and bars[j-1].val > bars[j].val:
            changeColor([bars[j],bars[j-1]],RED)
            swap(j, j-1)
            changeColor([bars[j],bars[j-1]],BLUE)
            j -= 1
    completed()

def selectionSort():
    for i in range(len(bars)):
        for j in range(i+1, len(bars)):
            changeColor([bars[j],bars[j-1]],RED)
            if bars[i].val > bars[j].val:
                swap(i,j)
            changeColor([bars[j],bars[j-1]],BLUE)
    completed()

#Randomizing
def randomize():
    random_btn["state"] = DISABLED
    start_btn["state"] = DISABLED
    random.shuffle(values)
    for i in range(len(bars)):
        bars[i].fillcolor(BLUE)
        bars[i].color(BLUE)
        swap(i, values[i])
    random_btn["state"] = NORMAL
    start_btn["state"] = NORMAL

#Combobox for algorithm selection
algo_box = ttk.Combobox(root, values=algorithms)
algo_box.current(0)

#Start sorting with selected algorithm
def startSort():
    start_btn["state"] = DISABLED
    random_btn["state"] = DISABLED
    algo = algo_box.get()
    if algo == 'Bubble Sort':
        bubbleSort()
    elif algo == 'Insertion Sort':
        insertionSort()
    elif algo == 'Selection Sort':
        selectionSort()

#Buttons
start_btn = Button(root, text="Start", style="W.TButton", command=startSort)
random_btn = Button(root, text="Randomize", style="W.TButton", command=randomize)

# Arrenging the widgets on the windows
algo_box.grid(row=0, column=1)
random_btn.grid(row=0, column=2)
start_btn.grid(row=0, column=3)

root.mainloop()
