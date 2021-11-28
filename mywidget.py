import sys
from PyQt5.QtWidgets import *

class MyWidget(QWidget):
  def __init__(self, mainWindow):
    super(MyWidget, self).__init__()
    self.mainWindow = mainWindow
    self.setGeometry(100, 100, 200, 150)
    self.setWindowTitle('Definir Grid')
    self.r1 = QLabel('SubDivisões Horizontais:')
    self.r2 = QLabel('SubDivisões Verticais:')
    self.t1 = QLineEdit()
    self.t2 = QLineEdit()
    self.b1 = QPushButton('Ok')
    self.box = QVBoxLayout()
    self.box.addWidget(self.r1)
    self.box.addWidget(self.t1)
    self.box.addWidget(self.r2)
    self.box.addWidget(self.t2)
    self.box.addWidget(self.b1)
    self.setLayout(self.box)
    self.b1.clicked.connect(self.submit)
    self.submitted = False

  def submit(self):
    self.submitted = True
    print(self.t1.text())
    print(self.t2.text())
    if not (self.t1.text().isnumeric() and self.t2.text().isnumeric()):
      QMessageBox.about(self, 'Erro', 'Preencha os campos')
    else:
      self.close()

  def show(self):
    return super().show()

  def close(self):
    return super().close()
