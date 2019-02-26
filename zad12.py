from tkinter import *
from PIL import Image, ImageTk
import math
import random


def used_place(list, x, y):
    if list[y][x]:
        return False
    else:
        return True


def change(p):
    global is_clicked, row1, column1, row2, column2, p2
    if is_clicked == False:
        p2 = p
        row1 = positions[p].grid_info()["row"]
        column1 = positions[p].grid_info()["column"]
        is_clicked = True
    else:
        row2 = positions[p].grid_info()["row"]
        column2 = positions[p].grid_info()["column"]
        positions[p2].grid(row=row2, column=column2)
        positions[p].grid(row=row1, column=column1)
        is_clicked = False
    complete = True
    for i in range(len(positions)):
        if i != positions[i].grid_info()["row"] * num_w_puzzles + positions[i].grid_info()["column"]:
            complete = False
    if complete == True:
        label.config(text="brawo!!!")


p2 = None
row1 = None
column1 = None
row2 = None
column2 = None
is_clicked = False
num_of_puzzles = 50
root = Tk()

photo = PhotoImage(file="img.png")
ph_width = photo.width()
ph_height = photo.height()

num_w_puzzles = int(math.sqrt(num_of_puzzles))
num_h_puzzles = int(num_of_puzzles / num_w_puzzles)
print(num_w_puzzles, ', ', num_h_puzzles)

im = Image.open("img.png")
w_puzzle = int(ph_width/num_w_puzzles)
h_puzzle = int(ph_height/num_h_puzzles)
puzzles = []
positions = []
p = 0

for y in range(num_h_puzzles):
    for x in range(num_w_puzzles):
        puzzle = im.crop((x * w_puzzle, y * h_puzzle, (x+1) * w_puzzle, (y+1) * h_puzzle))
        puzzles.append(ImageTk.PhotoImage(puzzle))
        positions.append(Button(root, image=puzzles[p], command=lambda p=p: change(p)))
        positions[p].grid(row=y, column=x)
        positions[0].focus_set()
        p += 1


occupied_list = []

for y in range(num_h_puzzles):
    occupied_list.append([])
    for x in range(num_w_puzzles):
        occupied_list[len(occupied_list)-1].append(False)

for position in positions:
    while True:
        x = random.randrange(0, num_w_puzzles)
        y = random.randrange(0, num_h_puzzles)
        if used_place(occupied_list, x, y):
            occupied_list[y][x] = True
            break
    position.grid(row=y, column=x)

label = Label(root, text="", font=("Helvetica", 16))
label.grid(row=num_h_puzzles+1, column=int(num_w_puzzles/2-1))

root.mainloop()