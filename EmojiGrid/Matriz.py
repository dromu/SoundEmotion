import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import csv

def draw_circle(event):
    x, y = event.x, event.y
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

# Load the image
image_path = 'EmojiGrid_inside.jpeg'
img_inside = Image.open(image_path)
img_tk = ImageTk.PhotoImage(img_inside)

canvas = tk.Canvas(root, width=img_tk.width(), height=img_tk.height())
canvas.pack()

canvas.create_image(0, 0, anchor='nw', image=img_tk)

img_offset_x = canvas.winfo_reqwidth() / 2 - img_tk.width() / 2
img_offset_y = canvas.winfo_reqheight() / 2 - img_tk.height() / 2
img_width = img_tk.width()
img_height = img_tk.height()

canvas.bind("<Button-1>", draw_circle)

root.mainloop()