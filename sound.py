import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class SoundPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Reproducir Sonido')

        self.play_button = QPushButton('Reproducir Sonido', self)
        self.play_button.setGeometry(50, 50, 200, 50)
        self.play_button.clicked.connect(self.play_sound)

        self.media_player = QMediaPlayer()
        self.media_player.setVolume(50)  # Ajusta el volumen (0-100)

        # Ruta del archivo de sonido que deseas reproducir
        sound_file_path = 'micho.wav'  # Reemplaza con la ruta de tu archivo de sonido
        self.media_content = QMediaContent(QUrl.fromLocalFile(sound_file_path))

    def play_sound(self):
        self.media_player.setMedia(self.media_content)
        self.media_player.play()

def main():
    app = QApplication(sys.argv)
    window = SoundPlayer()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
