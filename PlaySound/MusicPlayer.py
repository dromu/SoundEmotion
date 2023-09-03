import os
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.uic import loadUi
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import QMovie, QPalette, QColor
import pandas as pd
import csv

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        # SE carga el archivo ui 
        self.ventana = loadUi(r"PlaySound\Reproductor.ui", self)
        self.setWindowTitle("Music Player")

        # Crear una instancia de QMovie y asociarla con el QLabel
        self.gif_movie = QMovie(r"PlaySound\sound.gif")
        self.gif_label.setMovie(self.gif_movie)

        # Iniciar la reproducción del GIF
        self.gif_movie.start()
        self.gif_movie.stop()

        self.player = QMediaPlayer()
        self.playlist = []
        self.current_track_index = -1
        
        self.ventana.play_button.clicked.connect(self.play_music)
        self.player.stateChanged.connect(self.check_player_state)
        self.toolButton.clicked.connect(self.salto)
        self.toolButton.setEnabled(False)  # Deshabilitar siguiente
        
    def play_music(self):

        # Lectura del .CSV de los audios
        df = pd.read_csv(r"Input\MVP1_2019.csv")

        # se elige un valor aleatorio 
       

        # Obtener una lista de índices que tengan el valor 0
        indices_disponibles = [i for i, valor in enumerate(df['selected']) if valor == 0]

        # Verificar si hay índices disponibles
        if not indices_disponibles:
            self.Texto.setText("No hay ceros en la columna.")
        else:
            # Elegir aleatoriamente un índice de la lista de índices disponibles
            indice_aleatorio = random.choice(indices_disponibles)

        # Cambiar el valor en el índice aleatorio de 0 a 1
        df.at[indice_aleatorio, 'selected'] = 1


        # Guardamos ese indice
        nombre_archivo = 'Output/indice.csv'
        with open(nombre_archivo, 'w', newline='') as archivo_csv:
            # Crea un objeto escritor de CSV
            escritor_csv = csv.writer(archivo_csv)
            # Escribe el número en el archivo CSV
            escritor_csv.writerow([indice_aleatorio])


        # Imprimir el dataframe resultante
        print("indice aleatorio: ", indice_aleatorio)
        name = df.iloc[indice_aleatorio][1]

        nombre_archivo = 'Output/MVP1_2019_answer.csv'
        df.to_csv(nombre_archivo, index=False)

         # Iniciar la reproducción del GIF
        self.gif_movie.start()

        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.stop()

        folder_path = r"Input\MVP1_2019"
    
        track = os.path.join(folder_path, name)
        print(track)
        content = QMediaContent(QUrl.fromLocalFile(track))
    
        try:
            self.player.setMedia(content)
            self.player.play()
            
        except Exception as e:
            print(f"Error al reproducir la canción: {str(e)}")
            self.Texto.setText(f"Error al reproducir la canción: {str(e)}")

        self.play_button.setEnabled(False) 
    
    def check_player_state(self, new_state):
        if new_state == QMediaPlayer.StoppedState:
            self.toolButton.setEnabled(True)  # Habilitar el botón al finalizar la reproducción
            self.gif_movie.stop()

    def salto(self):
        self.ventana.hide()  # Oculta la ventana al hacer clic en el botón
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MusicPlayer()
    window.show()
    sys.exit(app.exec_())