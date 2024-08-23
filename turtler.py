import turtle
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QPushButton, QSlider, QColorDialog
from PyQt5.QtCore import Qt

app = QApplication([])

# --- окно приняло Л ---

l_window = QWidget()

l_window.setGeometry(0, 60, 540, 950)
l_window.setWindowTitle('Left main window')
l_window.show()

# --- окно было право ---

r_window = QWidget()

r_window.setGeometry(1380, 60, 540, 950)
r_window.setWindowTitle('Right main window')
r_window.show()

# --- окно тёти моти ---

m_window = turtle.Screen()

m_window.setup(
    width=840,
    height=950,
    startx=530,
    starty=30
)

# ===================
# ===   ОБЬЕКТЫ   ===
# ===================

l_vert = QVBoxLayout() # левая направляющая

vertic_txt = QLabel('Количество углов:')
verticies = QSlider(Qt.Horizontal)
verticies.setMinimum(0)
verticies.setMaximum(11)
verticies.setTickPosition(QSlider.TicksBelow)

long_txt = QLabel('Длина сторон:')
longness = QSlider(Qt.Horizontal)
longness.setMinimum(50)
longness.setMaximum(100)
longness.setTickPosition(QSlider.TicksBelow)

thicc_txt = QLabel('Толщина кисти:')
thiccness = QSlider(Qt.Horizontal)
thiccness.setMinimum(0)
thiccness.setMaximum(30)
thiccness.setTickPosition(QSlider.TicksBelow)

color_changer = QColorDialog()

draw_figure = QPushButton('Нарисовать')

erase_all = QPushButton('Стереть всё')

# --- размещение ---

l_vert.addWidget(vertic_txt, 1)
l_vert.addWidget(verticies, 1)
l_vert.addWidget(long_txt, 1)
l_vert.addWidget(longness, 1)
l_vert.addWidget(thicc_txt, 1)
l_vert.addWidget(thiccness, 1)
l_vert.addWidget(color_changer, 5)
l_vert.addWidget(draw_figure, 2)
l_vert.addWidget(erase_all, 2)

l_window.setLayout(l_vert)

# --- черепудель ---
turtle.showturtle()
turtle.shape('circle')

# ===================
# ===   ФУНКЦИИ   ===
# ===================

def change_thicc():
    turtle.pensize(thiccness.value() + 10)

def draw_shape():
    for i in range(verticies.value()):
        turtle.forward(longness.value())
        turtle.left(360 / verticies.value())

thiccness.valueChanged.connect(change_thicc)
draw_figure.clicked.connect(draw_shape)

turtle.mainloop()

app.exec()