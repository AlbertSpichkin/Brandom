from turtle import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication([])

# window = QWidget()

# window.setGeometry(0, 0, 0, 0)
# window.setWindowTitle('PyQt5 window example')
# window.show()

btn = QPushButton('впеерееед')
btn.setGeometry(0,0,100,100)
btn.show()



def forward_t():
    forward(100)

btn.clicked.connect(forward_t)

exitonclick()

app.exec()