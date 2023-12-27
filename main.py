import sys
from PyQt5.QtWidgets import (
    QApplication,
)
from ui import FileDialog


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileDialog()
    ex.show()
    sys.exit(app.exec_())

