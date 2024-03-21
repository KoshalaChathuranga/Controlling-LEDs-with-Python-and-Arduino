import sys
import time
import serial
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

class MyWindow(QDialog):
    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi('Main window.ui', self)  
        self.setWindowTitle('My GUI App')
            
        self.B1.clicked.connect(lambda: self.B_clicked(14))
        self.B2.clicked.connect(lambda: self.B_clicked(15))
        self.B3.clicked.connect(lambda: self.B_clicked(16))
        self.B4.clicked.connect(lambda: self.B_clicked(17))
        self.B5.clicked.connect(lambda: self.B_clicked(18))
        self.B6.clicked.connect(lambda: self.B_clicked(19))

        self.current_pin = None
        
        self.arduino = serial.Serial(port='COM4', timeout=0)
        time.sleep(2)
        
    def B_clicked(self, pin):
        if self.current_pin is not None:
            self.arduino.write(bytes([self.current_pin]))  
            print(f"Turning off LED on pin {self.current_pin}")
            time.sleep(0.1)  
            
        self.current_pin = pin
        self.arduino.write(bytes([pin]))  
        print(f"Turning on LED on pin {bytes([pin])}")
        time.sleep(0.1)  
        
    def closeEvent(self, event):
        self.arduino.write(b'0')  
        self.arduino.close()  
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
