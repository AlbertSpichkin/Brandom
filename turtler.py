import turtle
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QPushButton, QSlider, QDial
from PyQt5.QtCore import Qt

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

# --- окно тёти моти ---

# m_window = turtle.Screen()

# m_window.setup(
#     width=880,
#     height=950,
#     startx=510,
#     starty=30
# )

# ===========
# = ОБЬЕКТЫ =
# ===========

l_vert = QVBoxLayout() # левая направляющая

verticies = QSlider(Qt.Horizontal)
verticies.setMinimum(0)
verticies.setMaximum(10)
verticies.setTickPosition(QSlider.TicksBelow)

thiccness = QDial()
thiccness.setRange(1, 20)

# --- размещение ---

l_vert.addWidget(verticies)
l_vert.addWidget(thiccness)

l_window.setLayout(l_vert)

# ===========
# = ФУНКЦИИ =
# ===========

# turtle.mainloop()

app.exec()