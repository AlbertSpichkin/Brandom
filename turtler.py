import turtle
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication([])

# --- окно приняло Л ---

l_window = QWidget()

l_window.setGeometry(20, 60, 500, 950)
l_window.setWindowTitle('Left main window')
l_window.show()

# --- окно было право ---

r_window = QWidget()

r_window.setGeometry(1400, 60, 500, 950)
r_window.setWindowTitle('Right main window')
#r_window.show()

btn = QPushButton('впеерееед')
btn.setGeometry(0,0,100,100)
# btn.show()

# --- окно тёти моти ---

# m_window = turtle.Screen()

# m_window.setup(
#     width=880,
#     height=950,
#     startx=510,
#     starty=30
# )

#===========
#= ФУНКЦИИ =
#===========

def forward_t():
    turtle.forward(100)

btn.clicked.connect(forward_t)

# turtle.mainloop()

app.exec()