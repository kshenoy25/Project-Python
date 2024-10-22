import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout,)

from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        # in case argument is sent to the parent
        super().__init__()
        # adding label to weather app project
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)

        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)


        # apply styles based on object name
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size: 30px;
                font-style: italic;
                
            }
            QLineEdit#city_input{
                font-size: 20px;
            
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }     
        
        """)
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        # api key from the open weather web application
        api_key = "09d220bc3723fee24b13ba2c02a5521b"
        # accessing the city
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            # raise an exception if there are any HTTPErrors
            response.raise_for_status()
            data = response.json()


            # status code testing
            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError:
            pass
        except requests.exceptions.RequestException:
            pass

    def display_error(self, error):
        pass
    def display_weather(self, data):
        print(data)


if __name__ == '__main__':
    # creating an app project
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()

    # clean exit
    sys.exit(app.exec_())




