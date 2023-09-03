import os
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.uic import loadUi
from PyQt5.QtGui import QMovie

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        # SE carga el archivo ui 
        self.ventana = loadUi(r"PlaySound\Reproductor.ui", self)
        self.setWindowTitle("Music Player")

        # Crear una instancia de QMovie y asociarla con el QLabel
        self.gif_movie = QMovie(r"PlaySound\Reproductor.gif")
        self.gif_label.setMovie(self.gif_movie)

        # Iniciar la reproducción del GIF
        # self.gif_movie.start()

        self.player = QMediaPlayer()
        self.playlist = []
        self.current_track_index = -1
        
        self.ventana.play_button.clicked.connect(self.play_music)
        self.player.stateChanged.connect(self.check_player_state)
        self.toolButton.clicked.connect(self.salto)
        self.toolButton.setEnabled(False)  # Deshabilitar el botón al inicio
        
    def play_music(self):

         # Iniciar la reproducción del GIF
        self.gif_movie.start()
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.stop()

        folder_path = r"Input\MVP1_2019"
        self.playlist = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith((".mp3", ".wav"))]
    
        if not self.playlist:
            self.Texto.setText("No se encontraron canciones en la carpeta.")
            return
    
        random.shuffle(self.playlist)
        self.current_track_index = 0  # Empieza desde la primera pista
    
        track = self.playlist[self.current_track_index]
        content = QMediaContent(QUrl.fromLocalFile(track))
    
        try:
            self.player.setMedia(content)
            self.player.play()
            self.Texto.setText(os.path.basename(track))
        except Exception as e:
            print(f"Error al reproducir la canción: {str(e)}")
            self.Texto.setText(f"Error al reproducir la canción: {str(e)}")
    
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