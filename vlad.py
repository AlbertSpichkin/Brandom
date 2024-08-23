import turtle
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSlider, QVBoxLayout, QDial
from PyQt5.QtCore import Qt

app = QApplication([])

# =====================================================
# =                     ВИЗУАЛ                        =
# =====================================================

# --- левое окно ---
window_left = QWidget()

window_left.setGeometry(0, 0, 500, 1100)
window_left.setWindowTitle('PyQt5 window example')
window_left.show()

# --- правое окно ---
window_right = QWidget()

window_right.setGeometry(1420, 0, 500, 1100)
window_right.setWindowTitle('PyQt5 window example')
# window_right.show()

# среднее окно
# window_turtle = turtle.Screen()

# window_turtle.setup(
#     width=920,
#     height=1100,
#     startx=500,
#     starty=0
# )

# -----------------------------------------------------
# -               ВИДЖЕТЫ ЛЕВОГО ОКНА                 -
# -----------------------------------------------------

window_left_axis = QVBoxLayout() # направляющая

# --- слайдер смены углов ---
change_angle_slider = QSlider(Qt.Horizontal)
change_angle_slider.setMinimum(0)
change_angle_slider.setMaximum(10)
change_angle_slider.setTickPosition(QSlider.TicksBelow)

# --- изменение толщины кисти ---
thiccness = QDial()
thiccness.setRange(0, 20)
thiccness.setSingleStep(10)




# --- размещение ---
window_left_axis.addWidget(change_angle_slider)
window_left_axis.addWidget(thiccness)

window_left.setLayout(window_left_axis)

# --- запуск ---
# turtle.mainloop()
app.exec()