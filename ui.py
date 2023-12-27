from PyQt5.QtWidgets import (
    QMainWindow, 
    QPushButton, 
    QFileDialog, 
    QMessageBox
)
from photo_handler import remove_background_from_file


class FileDialog(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 100)
        self.setWindowTitle('Remove background from photo')

        # Calculate the x-coordinate and y-coordinate to center the button
        button_width = 200
        button_height = 30
        x_coordinate = (self.width() - button_width) // 2
        y_coordinate = (self.height() - button_height) // 2

        self.button = QPushButton('Choose file', self)
        self.button.setGeometry(x_coordinate, y_coordinate, button_width, button_height)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fname, _ = QFileDialog.getOpenFileName(
            self,
            'Open file',
            '/home', 'Image Files (*.png *.jpg *.jpeg);;All Files (*)',
            options=options
            )
        
        if fname:
            output_filename:str = remove_background_from_file(fname)
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Output Filename")
            msg_box.setText(f"The output filename is:\n{output_filename}")
            msg_box.setIcon(QMessageBox.Information)
            msg_box.addButton(QMessageBox.Ok)
            msg_box.exec_()

