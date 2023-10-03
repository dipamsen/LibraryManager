import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

def on_button_click():
    label.setText("Button Clicked!")

app = QApplication(sys.argv)
main_window = QMainWindow()
main_window.setWindowTitle("PyQt5 Application")
main_window.setGeometry(100, 100, 400, 300)

label = QLabel("Hello, PyQt5!", parent=main_window)
label.move(150, 50)

button = QPushButton("Click me!", parent=main_window)
button.move(150, 100)
button.clicked.connect(on_button_click)

main_window.show()
sys.exit(app.exec_())
