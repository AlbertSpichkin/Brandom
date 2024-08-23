import sys
import turtle
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QColorDialog, QLabel, QSpinBox
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFrame, QGridLayout
from PyQt5.Qt import QWindow
import tkinter as tk


class TurtleWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Создаем окно Tk
        self.tk_root = tk.Tk()
        self.tk_root.withdraw()  # Скрываем главное окно Tkinter
        
        # Создаем холст для рисования Turtle
        self.canvas = turtle.ScrolledCanvas(self.tk_root)
        self.canvas.pack(fill="both", expand=True)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.turtle = turtle.RawTurtle(self.screen)
        self.turtle.speed(0)
        self.color = 'black'
        
        # Интеграция Canvas в PyQt
        self.tk_root.update_idletasks()
        window_id = self.canvas.winfo_id()
        window = QWindow.fromWinId(window_id)
        window_container = self.createWindowContainer(window, self)
        layout = QVBoxLayout(self)
        layout.addWidget(window_container)

    def set_color(self, color):
        self.color = color
        self.turtle.pencolor(color)

    def draw_shape(self, sides, length):
        self.turtle.begin_fill()
        for _ in range(sides):
            self.turtle.forward(length)
            self.turtle.left(360 / sides)
        self.turtle.end_fill()

    def clear(self):
        self.turtle.clear()

    def save_image(self, filename='drawing.eps'):
        self.screen.getcanvas().postscript(file=filename)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Центральная часть окна для Turtle
        self.turtle_widget = TurtleWidget(self)

        # Левая панель управления
        self.left_panel = QWidget(self)
        self.left_layout = QVBoxLayout(self.left_panel)
        
        # Ввод углов
        self.sides_label = QLabel('Углы:', self)
        self.sides_input = QSpinBox(self)
        self.sides_input.setRange(3, 12)
        self.sides_input.setValue(3)

        # Ввод длины стороны
        self.length_label = QLabel('Сторона:', self)
        self.length_input = QSpinBox(self)
        self.length_input.setRange(10, 200)
        self.length_input.setValue(50)

        # Кнопка выбора цвета
        self.color_button = QPushButton('Выбрать цвет', self)
        self.color_button.clicked.connect(self.choose_color)

        # Кнопка рисования
        self.draw_button = QPushButton('Нарисовать', self)
        self.draw_button.clicked.connect(self.draw_shape)

        # Кнопка очистки
        self.clear_button = QPushButton('Очистить', self)
        self.clear_button.clicked.connect(self.turtle_widget.clear)

        # Добавляем элементы на левую панель
        self.left_layout.addWidget(self.sides_label)
        self.left_layout.addWidget(self.sides_input)
        self.left_layout.addWidget(self.length_label)
        self.left_layout.addWidget(self.length_input)
        self.left_layout.addWidget(self.color_button)
        self.left_layout.addWidget(self.draw_button)
        self.left_layout.addWidget(self.clear_button)

        # Правая панель (выбор предустановленных фигур и сохранение)
        self.right_panel = QWidget(self)
        self.right_layout = QVBoxLayout(self.right_panel)

        # Кнопка сохранения
        self.save_button = QPushButton('Сохранить', self)
        self.save_button.clicked.connect(lambda: self.turtle_widget.save_image('drawing.eps'))

        # Добавляем кнопку сохранения на правую панель
        self.right_layout.addWidget(self.save_button)

        # Основная компоновка
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.left_panel)
        self.main_layout.addWidget(self.turtle_widget, 1)
        self.main_layout.addWidget(self.right_panel)

        # Устанавливаем основную компоновку в главном виджете
        self.central_widget = QWidget(self)
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.turtle_widget.set_color(color.name())

    def draw_shape(self):
        sides = self.sides_input.value()
        length = self.length_input.value()
        self.turtle_widget.draw_shape(sides, length)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
