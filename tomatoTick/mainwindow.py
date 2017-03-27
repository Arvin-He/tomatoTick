from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5.QtCore import QRect
import sys

class TomatoTickWindow(QMainWindow):

  def __init__(self):
    super(TomatoTickWindow, self).__init__()
    self.initUI()
    
    
  def initUI(self):
    self.setWindowTitle("TomatoClock")
    screen = QDesktopWidget().screenGeometry()
    self.setGeometry(QRect((screen.width()-self.geometry().width())/2, 
                           (screen.height()-self.geometry().height())/2, 600, 500))
    self.show()

  
if __name__ == "__main__":
  app = QApplication(sys.argv)
  tomatoTick = TomatoTickWindow()
  sys.exit(app.exec_())