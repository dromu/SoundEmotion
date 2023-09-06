import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QPointF
from PyQt5.uic import loadUi

class CoordinateApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Coordinate Axes and Drawing")

        self.ventana = loadUi("emojigrid\Emojigrid.ui", self)  # Load the UI design

        self.view = self.findChild(QGraphicsView, 'view')  # Find the QGraphicsView widget by name
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)

        self.img_inside = QPixmap("emojigrid\EmojiGrid_inside.jpeg")
        self.img_inside = self.img_inside.scaled(500, 500, Qt.KeepAspectRatio)  # Resize image to 500x500 while maintaining aspect ratio
        self.scene.addPixmap(self.img_inside)

        self.img_offset_x = self.view.width() / 2 - self.img_inside.width() / 2
        self.img_offset_y = self.view.height() / 2 - self.img_inside.height() / 2
        self.img_width = self.img_inside.width()
        self.img_height = self.img_inside.height()

        self.view.setSceneRect(0, 0, self.img_inside.width(), self.img_inside.height())
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.mousePressEvent = self.draw_circle

        self.coordinates_file = 'coordinates.csv'
        self.clicked = False  # Track if a click has been made

        self.toolButton.clicked.connect(self.salto)

    def draw_circle(self, event):
        if not self.clicked:  # Only allow one click
            x, y = event.pos().x(), event.pos().y()

            # print("x: ", self.img_width ,"y: ",self.img_height)
            normalized_x = round((x - self.img_offset_x) / self.img_width * 2 - 1, 3)
            normalized_y = round(1 - (y - self.img_offset_y) / self.img_height * 2, 3)

            ellipse = QGraphicsEllipseItem(x - 10, y - 10, 20, 20)
            ellipse.setBrush(Qt.red)
            self.scene.addItem(ellipse)

            self.save_coordinates(normalized_x, normalized_y)
            self.clicked = True  # Mark that a click has been made3
            

    def salto(self):
        if self.clicked == True:
            self.ventana.hide()

        

        
    
    def save_coordinates(self, x, y):
    # Append new coordinate to the existing file
        with open(self.coordinates_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([x, y])   

# def run():
#     window = CoordinateApp()
#     window.showFullScreen()
  

# if __name__ == '__main__':
#     run()
    