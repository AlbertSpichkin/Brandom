from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QRadioButton, QButtonGroup
from PyQt5.QtCore import Qt
from random import randint

app = QApplication([])

vert = QVBoxLayout()
volt = QVBoxLayout()
walt = QVBoxLayout()
hori = QHBoxLayout()
hary = QHBoxLayout()
gary = QHBoxLayout()
lary = QHBoxLayout()
mary = QHBoxLayout()

window = QWidget()
window.resize(550, 300)
window.setWindowTitle('My own DnD engine')
window.show()

class Hero():
    def __init__(self, name, health=0, defence=0, damage=0, friend=0):
        self.name = name
        self.health = health
        self.defence = defence
        self.damage = damage
        self.friend = friend
        self.radio = QRadioButton(f'{name}: {health} HP, {defence} DEF, {damage} DMG, {friend} FSP')
    def update_radio(self):
        self.radio.setText(f'{self.name}: {self.health} HP, {self.defence} DEF, {self.damage} DMG, {self.friend} FSP')
    def change_name(self):
        self.name = name.text()
        self.update_radio()
        name.clear()
    def changeHP(self):
        self.health += int(health.text())
        self.update_radio()
        health.clear()
    def changeDEF(self):
        self.defence += int(defence.text())
        self.update_radio()
        defence.clear()
    def changeDMG(self):
        self.damage += int(damage.text())
        self.update_radio()
        damage.clear()
    def changeFSP(self):
        self.friend += int(friend.text())
        self.update_radio()
        friend.clear()

chars = QButtonGroup()
cinnamin = Hero('Циннамин', 60, 10, 40, 85)
redacted = Hero('[REDACTED]', 70, 25, 100, 10)
medic = Hero('Медик', 150, 0, 30, 50)
enemy = Hero('Враг')
cinnamin.radio.setChecked(True)
chars.addButton(cinnamin.radio, 0)
chars.addButton(redacted.radio, 1)
chars.addButton(medic.radio, 2)
chars.addButton(enemy.radio, 3)
roller = QButtonGroup()
custom = QLineEdit('5')
custom.setPlaceholderText('Макс число')
roll = QRadioButton()
roll_10 = QRadioButton('Бросить 10')
roll_20 = QRadioButton('Бросить 20')
roll_30 = QRadioButton('Бросить 30')
roll.setChecked(True)
roller.addButton(roll, int(custom.text()))
roller.addButton(roll_10, 10)
roller.addButton(roll_20, 20)
roller.addButton(roll_30, 30)
name = QLineEdit()
health = QLineEdit()
defence = QLineEdit()
damage = QLineEdit()
friend = QLineEdit()
name.setPlaceholderText('Имя')
health.setPlaceholderText('Здоровье')
defence.setPlaceholderText('Защита')
damage.setPlaceholderText('Урон')
friend.setPlaceholderText('Дружба')
text = QLabel('Рандомное число:')
number = QLabel('0')
add_name = QPushButton('Изменить имя')
addHP = QPushButton('Прибавить к HP')
addDEF = QPushButton('Прибавить к DEF')
addDMG = QPushButton('Прибавить к DMG')
addFSP = QPushButton('Прибавить к FSP')
reroll = QPushButton('Бросить кубик')
result = QLabel('Тут будет результат')

lary.addWidget(text, alignment=Qt.AlignCenter)
lary.addWidget(number, alignment=Qt.AlignCenter)
volt.addWidget(cinnamin.radio)
volt.addWidget(redacted.radio)
volt.addWidget(medic.radio)
volt.addWidget(enemy.radio)
mary.addWidget(roll)
mary.addWidget(custom)
walt.addLayout(mary)
walt.addWidget(roll_10)
walt.addWidget(roll_20)
walt.addWidget(roll_30)
hary.addWidget(name)
hary.addWidget(health)
hary.addWidget(defence)
hary.addWidget(damage)
hary.addWidget(friend)
gary.addWidget(add_name)
gary.addWidget(addHP)
gary.addWidget(addDEF)
gary.addWidget(addDMG)
gary.addWidget(addFSP)
hori.addLayout(volt)
hori.addLayout(walt)
vert.addWidget(result, alignment=Qt.AlignCenter)
vert.addLayout(lary)
vert.addLayout(hori)
vert.addLayout(hary)
vert.addLayout(gary)
vert.addWidget(reroll)

def randomize():
    try:
        roller.setId(roll, int(custom.text()))
        number.setText(str(randint(1, roller.checkedId())))

        if roller.checkedId() == 10:
            if int(number.text()) > 5:
                result.setText('Хорошо')
            else:
                result.setText('Мимо')
                
        elif roller.checkedId() == 20:
            if int(number.text()) > 15:
                result.setText('Отлично!')
            elif int(number.text()) > 10:
                result.setText('Хорошо')
            elif int(number.text()) > 5:
                result.setText('Мимо')
            else:
                result.setText('Плохо!')
                
        elif roller.checkedId() == 30:
            if int(number.text()) > 25:
                result.setText('ИДЕАЛЬНО!!!')
            elif int(number.text()) > 20:
                result.setText('Отлично!')
            elif int(number.text()) > 15:
                result.setText('Хорошо')
            elif int(number.text()) > 10:
                result.setText('Мимо')
            elif int(number.text()) > 5:
                result.setText('Плохо')
            else:
                result.setText('Ужасно!')

        else:
            result.setText('Результат')
    except:
        result.setText('НЕЛЬЗЯ!')

def changeHP():
    try:
        if chars.checkedId() == 0:
            cinnamin.changeHP()
        if chars.checkedId() == 1:
            redacted.changeHP()
        if chars.checkedId() == 2:
            medic.changeHP()
        if chars.checkedId() == 3:
            enemy.changeHP()
        health.clear()
    except:
        pass

def changeDEF():
    try:
        if chars.checkedId() == 0:
            cinnamin.changeDEF()
        if chars.checkedId() == 1:
            redacted.changeDEF()
        if chars.checkedId() == 2:
            medic.changeDEF()
        if chars.checkedId() == 3:
            enemy.changeDEF()
    except:
        pass

def changeDMG():
    try:
        if chars.checkedId() == 0:
            cinnamin.changeDMG()
        if chars.checkedId() == 1:
            redacted.changeDMG()
        if chars.checkedId() == 2:
            medic.changeDMG()
        if chars.checkedId() == 3:
            enemy.changeDMG()
    except:
        pass

def changeFSP():
    try:
        if chars.checkedId() == 0:
            cinnamin.changeFSP()
        if chars.checkedId() == 1:
            redacted.changeFSP()
        if chars.checkedId() == 2:
            medic.changeFSP()
        if chars.checkedId() == 3:
            enemy.changeFSP()
    except:
        pass

def change_name():
    try:
        if chars.checkedId() == 0:
            cinnamin.change_name()
        if chars.checkedId() == 1:
            redacted.change_name()
        if chars.checkedId() == 2:
            medic.change_name()
        if chars.checkedId() == 3:
            enemy.change_name()
    except:
        pass

reroll.clicked.connect(randomize)
addHP.clicked.connect(changeHP)
addDEF.clicked.connect(changeDEF)
addDMG.clicked.connect(changeDMG)
addFSP.clicked.connect(changeFSP)
add_name.clicked.connect(change_name)

window.setLayout(vert)

app.exec()

#alskjdlkasd
#ijkljdalkjsd
#hjklajsdj
#alksjdlkasd