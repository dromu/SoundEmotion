import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import csv

def draw_circle(event):
    x, y = event.x, event.y
    if img_inside_area[0] <= x <= img_inside_area[2] and img_inside_area[1] <= y <= img_inside_area[3]:
        normalized_x = round((x - img_offset_x) / img_width * 2 - 1, 3)
        normalized_y = round(1 - (y - img_offset_y) / img_height * 2, 3)

        canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill='red', outline='red')
        canvas.create_text(x, y - 15, text=f'({normalized_x}, {normalized_y})', fill='red')

        save_coordinates(normalized_x, normalized_y)

def save_coordinates(x, y):
    with open('coordinates.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([x, y])

root = tk.Tk()
root.title("Coordinate Axes and Drawing")

# Load the background image
background_path = 'EmojiGrid_outside.jpeg'
background_image = Image.open(background_path)
background_tk = ImageTk.PhotoImage(background_image)

canvas = tk.Canvas(root, width=background_tk.width(), height=background_tk.height())
canvas.pack()

canvas.create_image(0, 0, anchor='nw', image=background_tk)

# Load the inside image
inside_path = 'EmojiGrid_inside.jpeg'
img_inside = Image.open(inside_path)
img_inside_tk = ImageTk.PhotoImage(img_inside)

img_offset_x = (background_tk.width() - img_inside_tk.width()) / 2
img_offset_y = (background_tk.height() - img_inside_tk.height()) / 2
img_width = img_inside_tk.width()
img_height = img_inside_tk.height()
img_inside_area = (img_offset_x, img_offset_y, img_offset_x + img_width, img_offset_y + img_height)

canvas.create_image(img_offset_x, img_offset_y, anchor='nw', image=img_inside_tk)

canvas.bind("<Button-1>", draw_circle)

root.mainloop()