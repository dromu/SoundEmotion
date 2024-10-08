from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,  QButtonGroup,QLabel,QVBoxLayout
from PyQt5.QtCore import Qt
import csv
import matplotlib.pyplot as plt
import unicodedata
from PyQt5.QtGui import QPixmap
import sys
import time
from emojigrid import CoordinateApp
from PlaySound import MusicPlayer
from PyQt5.QtMultimedia import QSound
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QUrl
import pandas as pd

# Modificar esta variable que contiene el numero de ciclos
total_sonidos = 10

cantidad_sonidos = 0
#inciar la app

EndSound = False

app = QtWidgets.QApplication([])

pathWindows = "GuiWindows/"
Winicio      = uic.loadUi(pathWindows + "veninicio.ui")
# Wsound      = uic.loadUi(pathWindows + "venSonido.ui")
Wsound      = uic.loadUi(r"PlaySound\Reproductor.ui")
# Wemocion    = uic.loadUi(pathWindows + "venemoc.ui")
Wemocion    = uic.loadUi(r"emojigrid\Emojigrid.ui")
Wquestions  = uic.loadUi(pathWindows + "venpreg.ui")
Wquestions2  = uic.loadUi(pathWindows + "venpreg2.ui")
Wquestions3  = uic.loadUi(pathWindows + "venpreg3.ui")
Wfinal       = uic.loadUi(pathWindows + "venfinal.ui")
Wpruebfin    = uic.loadUi(pathWindows + "venfinprueba.ui")


# Agreganos en grupo las primeras respuestas 
button_group1A = QButtonGroup()
for i in range(1,7):
        button = getattr(Wquestions, f"R{i}")
        button_group1A.addButton(button)
        button.setChecked(False) 

button_group1B = QButtonGroup()
for i in range(1,7):
        button = getattr(Wquestions, f"R{i}_2")
        button_group1B.addButton(button)
        button.setChecked(False) 

button_group1C = QButtonGroup()
for i in range(1,7):
        button = getattr(Wquestions, f"R{i}_3")
        button_group1C.addButton(button)
        button.setChecked(False) 

button_group1D = QButtonGroup()
for i in range(1,7):
        button = getattr(Wquestions, f"R{i}_4")
        button_group1D.addButton(button)
        button.setChecked(False) 

button_group1E = QButtonGroup()
for i in range(1,7):
        button = getattr(Wquestions, f"R{i}_5")
        button_group1E.addButton(button)
        button.setChecked(False) 

button_group1F = QButtonGroup()
for i in range(1,7):
        button = getattr(Wquestions, f"R{i}_6")
        button_group1F.addButton(button)
        button.setChecked(False) 

button_group1G = QButtonGroup()
for i in range(1,7):
        button = getattr(Wquestions, f"R{i}_7")
        button_group1G.addButton(button)
        button.setChecked(False) 


# SE agrega a un grupo la segundas respuestas 
button_group2 = QButtonGroup()
for i in range(1,7):
        button = getattr(Wquestions2, f"R{i}{i}")
        button_group2.addButton(button)
        button.setChecked(False) 


# SE agrega a un grupo la terceras respuestas 
button_group3 = QButtonGroup()
for i in range(1,7):
        button = getattr(Wquestions3, f"R{i}{i}{i}")
        button_group3.addButton(button)
        button.setChecked(False) 

#Ventana de reproduccion del sonido


def gui_inicio():
    global cantidad_sonidos
    global total_sonidos

    if cantidad_sonidos == total_sonidos:
        Wfinal.hide()
        Wpruebfin.showFullScreen()

    else:     
        Wfinal.hide()
        Winicio.hide()

        Wquestions.showFullScreen()

        a = CoordinateApp.CoordinateApp()
        a.showFullScreen()
        
        b = MusicPlayer.MusicPlayer()
        b.showFullScreen()
        

def gui_sound():  
    Winicio.hide()
    b = MusicPlayer.MusicPlayer()
    b.showFullScreen()
    # Wsound.showFullScreen()
    
    
def gui_emocion():
    Winicio.hide()
    Wsound.hide()
    Wquestions.showFullScreen()
    # Wemocion.showFullScreen()
    a = CoordinateApp.CoordinateApp()
    a.showFullScreen()
    
    
# Ventana de las primeras seis preguntas 
def gui_questions():
    Wemocion.hide()
    # Wquestions.show()
    Wquestions.showFullScreen()
    # Wquestions.toolButton.setEnabled(False)

    
#Ventana de la segunda
def gui_questions2():
    Wquestions.hide()
    Wquestions2.showFullScreen()

# Ventana de la tercer pregunta
def gui_questions3():
    Wquestions2.hide()
    Wquestions3.showFullScreen()

# Ventana de agradecimiento 
def gui_final():
    global cantidad_sonidos
    global total_sonidos

    Wquestions3.hide()
    Wfinal.showFullScreen()

    df = pd.read_csv("Input\data_completa.csv")
    cantidad = len(df[df["selected"] == 0])
    
    TotalCant = cantidad - 1 

    Wfinal.contador.setText(str(TotalCant))
    
    #Se verifican todas las respuestas y se guardan

    Sbutton1A = button_group1A.checkedButton()
    Sbutton1B = button_group1B.checkedButton()
    Sbutton1C = button_group1C.checkedButton()
    Sbutton1D = button_group1D.checkedButton()
    Sbutton1E = button_group1E.checkedButton()
    Sbutton1F = button_group1F.checkedButton()
    Sbutton1G = button_group1G.checkedButton()
    Sbutton2  = button_group2.checkedButton()
    Sbutton3  = button_group3.checkedButton()

    
    # Se limpian las respuestas para que no tengan simbolos extraños
    respuestas = [limpiar_cadena(Sbutton1A.text()), limpiar_cadena(Sbutton1B.text()), limpiar_cadena(Sbutton1C.text()),
                  limpiar_cadena(Sbutton1D.text()), limpiar_cadena(Sbutton1E.text()), limpiar_cadena(Sbutton1F.text()),
                  limpiar_cadena(Sbutton1G.text()), limpiar_cadena(Sbutton2.text()), limpiar_cadena(Sbutton3.text())]
     
    # print(respuestas)

    # Se guarda en un csv
    to_csv(respuestas)

    cantidad_sonidos = cantidad_sonidos + 1 

    # print(cantidad_sonidos)

    
def play_sound():
    media_player = QMediaPlayer()
    media_player.setVolume(50)
    sound_file_path = 'micho.wav'  # Reemplaza "sound_file.wav" con la ubicación de tu archivo de sonido
    media_content = QMediaContent(QUrl.fromLocalFile(sound_file_path))

    
    def play_sound():
        print("media_content")
        media_player.setMedia(media_content)
        media_player.play()
    

def limpiar_cadena(cadena):
    # Convertir a minúsculas y reemplazar tildes por caracteres sin tilde
    cadena_limpia = cadena.lower()
    cadena_limpia = unicodedata.normalize('NFKD', cadena_limpia).encode('ASCII', 'ignore').decode('utf-8')
    
    # Quitar espacios en blanco y saltos de línea
    cadena_limpia = cadena_limpia.replace(" ", "").replace("\n", "")
    
    return cadena_limpia


def on_button_clicked(button):
    print("Radio button seleccionado:", button.text())


def clear_selection():
    
    button_group1A.setExclusive(False)
    button_group1A.checkedButton().setChecked(False)
    button_group1A.setExclusive(True)      
    
    button_group1B.setExclusive(False)
    button_group1B.checkedButton().setChecked(False)
    button_group1B.setExclusive(True) 

    button_group1C.setExclusive(False)
    button_group1C.checkedButton().setChecked(False)
    button_group1C.setExclusive(True)      
    
    button_group1D.setExclusive(False)
    button_group1D.checkedButton().setChecked(False)
    button_group1D.setExclusive(True)    

    button_group1E.setExclusive(False)
    button_group1E.checkedButton().setChecked(False)
    button_group1E.setExclusive(True)      
    
    button_group1F.setExclusive(False)
    button_group1F.checkedButton().setChecked(False)
    button_group1F.setExclusive(True)

    button_group1G.setExclusive(False)
    button_group1G.checkedButton().setChecked(False)
    button_group1G.setExclusive(True)
    
    button_group2.setExclusive(False)
    button_group2.checkedButton().setChecked(False)
    button_group2.setExclusive(True)  

    button_group3.setExclusive(False)
    button_group3.checkedButton().setChecked(False)
    button_group3.setExclusive(True)  

def verQuestion1():
    A1 = button_group1A.checkedButton()
    B1 = button_group1B.checkedButton()
    C1 = button_group1C.checkedButton()
    D1 = button_group1D.checkedButton()
    E1 = button_group1E.checkedButton()
    F1 = button_group1F.checkedButton()
    G1 = button_group1G.checkedButton()

    #Si todos los grupos tienen un respuesta, se puede cambiar a la siguiente pregunta 
    if (A1 and B1 and C1 and D1 and E1 and F1 and G1):
        Wquestions.toolButton.setEnabled(True)
        gui_questions2()

def verQuestion2():
    if button_group2.checkedButton():
        gui_questions3()

def verQuestion3():
    if button_group3.checkedButton():
        gui_final()

def verSound():
    if EndSound:
        gui_emocion()

def to_csv( nuevos_datos):
    with open("Output/data.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(nuevos_datos)

    data = pd.read_csv("Output/data.csv")
    coordinates = pd.read_csv("Output/coordinates.csv")
    indice = pd.read_csv("Output/indice.csv",header=None)
    mvp1 = pd.read_csv("Input\data_completa.csv",index_col=False)

    # mvp1.at[int(indice.iloc[0]), 'selected'] = 1
    mvp1['selected'].iloc[indice.iloc[0]] = 1

    # Se transforman los datos en un serie
    dato = data.iloc[-1][:]         #Se lee el ultimo dato
    coord = coordinates.iloc[-1]    # SE lee las ultimas coordenas 
    mvp1_ = mvp1.iloc[indice.iloc[0][0]][:2]

    res = pd.concat((mvp1_, dato,coord),axis= 0)

    mvp1.iloc[indice.iloc[0]] = res
    mvp1.to_csv("Input\data_completa.csv",index=False)
    mvp1.to_csv("Output\data_completa.csv",index=False)

def cerrar():
     sys.exit()


# Boton siguiente "toolButton"
Winicio.toolButton.clicked.connect(gui_inicio)        # me dirige a la primer pregunta

# Boton siguiente "toolButton"
Wsound.toolButton.clicked.connect(gui_emocion)        # me dirige a la primer pregunta
Wsound.play_button.clicked.connect(play_sound)

Wemocion.toolButton.clicked.connect(gui_questions) 

# REalizamos una verificacion los groups radio button fueron rellenados
Wquestions.toolButton.clicked.connect(verQuestion1)# dirige a la segunda pregunta

# REalizamos una verificacion los groups radio button fueron rellenados
Wquestions2.toolButton.clicked.connect(verQuestion2)# dirige a la segunda pregunta

# Verificacion de los radio button de la tercer pregunta 
Wquestions3.toolButton.clicked.connect(verQuestion3)# dirige a la segunda pregunta

# Al presionar el boton se devuelve a la pantalal de inicio 
Wfinal.toolButton.clicked.connect(gui_inicio)# incio

# SE limpia todas las selecciones de la primer pregunta
Wfinal.toolButton.clicked.connect(clear_selection)

# PAra cerrar la prueba
Wpruebfin.toolButton.clicked.connect(cerrar)

Winicio.showFullScreen()

app.exec()