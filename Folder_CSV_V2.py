import os
import csv
from PyQt5 import QtWidgets, QtGui, QtCore

app = QtWidgets.QApplication([])

folder_dialog = QtWidgets.QFileDialog()
folder_dialog.setFileMode(QtWidgets.QFileDialog.Directory)
folder_dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly)

#user set folder to list
if folder_dialog.exec_():
    folder_path = folder_dialog.selectedFiles()[0]
else:
    exit()

folder_name = os.path.basename(folder_path)

#user set destination
csv_dialog = QtWidgets.QFileDialog()
csv_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
csv_dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
csv_dialog.setDefaultSuffix('csv')
csv_dialog.setNameFilter('CSV Files (*.csv)')

if csv_dialog.exec_():
    csv_file = csv_dialog.selectedFiles()[0]
else:
    exit()

with open(csv_file, 'w') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['File Name', 'Size (bytes)'])

    for filename in os.listdir(folder_path):
        #Get file size
        file_size = os.stat(os.path.join(folder_path, filename)).st_size

        writer.writerow([filename, file_size])

msg = QtWidgets.QMessageBox()
msg.setText('The CSV file has been created.')
msg.setWindowTitle('Success')
msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
msg.exec_()

msg.information(None, 'Success', 'The CSV file has been created.', QtWidgets.QMessageBox.Ok)


