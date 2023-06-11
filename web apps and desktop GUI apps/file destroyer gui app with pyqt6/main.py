from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtWidgets import QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path

def oepn_files():
  global filenames
  filenames, _ = QFileDialog.getOpenFileNames(window, 'Select files')
  message.setText('\n'.join(filenames))
  
def destroy_files():
  for filename in filenames:
    path = Path(filename)
    with open(path, 'wb') as file:
      file.write(b'')
    path.unlink()
  message.setText('Destruction Successful!')
  
app = QApplication([])
window = QWidget()
window.setWindowTitle('File Destroyer')
layout = QVBoxLayout()

output_label = QLabel('Select the files you want to destroy. The files will be <font color="red">permanently</font> deleted')
layout.addWidget(description)

btn = QPushButton('Open Files')
open_btn.setToolTip('Open File')
open_btn.setFixedWidth(100)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(open_files)

btn = QPushButton('Destroy Files')
open_btn.setToolTip('Open File')
open_btn.setFixedWidth(100)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(destroy_files)

message = QLabel('')
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.show()
app.exec










layout1 = QHBoxLayout()
layout.addLayout(layout1)

output_label = QLabel('')
layout.addWidget(output_label)

layout2 = QVBoxLayout()
layout1.addLayout(layout2)

layout3 = QVBoxLayout()
layout1.addLayout(layout3)

in_combo = QComboBox()
currencies = ['USD', 'EUR', 'INR']
in_combo.addItems(currencies)
layout.addWidget(in_combo)

target_combo = QComboBox()
target_combo.addItems(currencies)
layout.addWidget(target_combo)

text = QLineEdit()
layout.addWidget(text)

