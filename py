import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLabel

from ui import Ui_MainWindow

SCREEN_SIZE = [600, 450]


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button.clicked.connect(self.getImage)

    def getImage(self):
        self.x = self.coord1.text()
        self.y = self.coord2.text()
        self.scalex = self.scale.text()
        map_request = f'http://static-maps.yandex.ru/1.x/?ll={self.x},{self.y}&spn={self.scalex},0.002&l=map'
        # map_request = "http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn=0.5,0.002&l=map"
        print(map_request)
        response = requests.get(map_request)
        # http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn=0.002,0.002&l=map
        # http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn=0.002,0.002&l=map

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")

            self.label.setText('Ошибка выполнения запроса')

            # sys.exit(1)
        else:

            # Запишем полученное изображение в файл.
            self.map_file = "map.png"
            with open(self.map_file, "wb") as file:
                file.write(response.content)
            self.pixmap = QPixmap(self.map_file)
            self.label.setPixmap(self.pixmap)

    def closeEvent(self, event):
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

