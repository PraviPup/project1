from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QTextEdit, QListWidget, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QInputDialog

app = QApplication([])

import json





main = QWidget()
main.resize(900,600)

text = QTextEdit()
button0 = QPushButton('Створити замітку')
button1 = QPushButton()
button2 = QPushButton()
button3 = QPushButton()
button4 = QPushButton()
button5 = QPushButton()
line = QLineEdit()
list0 = QListWidget()
list1 = QListWidget()
label0 = QLabel()
label1 = QLabel()


v1 = QVBoxLayout()
v1.addWidget(text)

h1 = QHBoxLayout()
h2 = QHBoxLayout()

h1.addWidget(button0)
h1.addWidget(button1)

h2.addWidget(button3)
h2.addWidget(button4)

v2 = QVBoxLayout()
v2.addWidget(label0)
v2.addWidget(list0)
v2.addLayout(h1)
v2.addWidget(button2)
v2.addWidget(label1)
v2.addWidget(list1)
v2.addWidget(label1)
v2.addWidget(list1)
v2.addWidget(line)
v2.addLayout(h2)
v2.addWidget(button5)

h3 = QHBoxLayout()
h3.addLayout(v1)
h3.addLayout(v2)
main.setLayout(h3)

def show_notes():
    key = list0.selectedItems()[0].text()
    text.setText(notes[key]["текст"])

def add_notes():
    dialog, ok = QInputDialog.getText(main,'додати замітку','назва замітки:')
    if dialog and ok != "":
        notes[dialog] = {'текст':"","теги":[]}
        list0.addItem(dialog)




list0.itemClicked.connect(show_notes)
button0.clicked.connect(add_notes)

with open("f.json", "r") as file:
    notes = json.load(file)
list0.addItems(notes)




main.show()
app.exec_()
