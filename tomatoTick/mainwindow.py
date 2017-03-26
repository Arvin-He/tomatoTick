from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
import sys

class TomatoTickWindow(QMainWindow):

  def __init__(self):
    super(TomatoTickWindow, self).__init__()
    self.initUI()
    self.show()
    
  def initUI(self):
    pass

  
if __name__ == "__main__":
  app = QApplication(sys.argv)
  tomatoTick = TomatoTickWindow()
  sys.exit(app.exec_())