import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase
class DigitalClock(QWidget):

    def __init__(self):
        super().__init__()
        self.time_label =QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        # set title for the window
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)

        # layout manager
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        # aligns the given text in the center of the layout
        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 150px;"
                                      #"font-family: Ariel;"
                                                "color: hsl(136, 92%, 50%);")
        self.setStyleSheet("background-color: black;")

        ########################################################################################################################
        # using a custom font
        #font_id = QFontDatabase.addApplicationFont("../PythonDigitalClockDemo/digital-7.ttf")
        # returns a list of font names and using an index as we are working with a list
        #font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        #my_font = QFont(font_family, 150)
        #self.time_label.setFont(my_font)
        ########################################################################################################################

        # timer to keep track of the current time
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()

    clock.show()
    sys.exit(app.exec_())