import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout

def window():
  app = QApplication(sys.argv)
  w = QWidget()
  w.setWindowTitle('Teste')
  w.setGeometry(100, 100, 300, 200)

  lbl = QLabel('Nome:', w)
  lbl.move(20, 20)

  edt = QLineEdit(w)
  edt.move(20, 40)

  btn = QPushButton('Ok', w)
  btn.move(20, 80)

  w.show()
  sys.exit(app.exec_())

if __name__ == '__main__':
  window()