import PySimpleGUI as gui
import config
from utils import utils
import os
from logic import scan_folder

#Setup
utils.buatFolderJikaTidakAda("Hasil")

#Set Theme
gui.theme("SystemDefault")

#Create Window Content
layout = [
    [gui.Text("Scan folder"), gui.Input(key="-FOLDER-", size=[52]), gui.FolderBrowse()],
    [gui.Checkbox("Membaca semua nama file dalam folder dan menyimpan nya", key="-READ-FILE-", default=True)],
    [gui.Checkbox("Copy folder Ke Folder Hasil", key="-OPSI-COPY-FOLDER-", default=True)],
    [gui.Checkbox("Mendeteksi file epub dan memisahkannya", key="-DETECT-EPUB-FILE-", default=True)],
    [gui.Checkbox("Mengubah dan menambahkan angka pada nama file", key="-CHANGE-NAME-FILE-", default=True)],
    [gui.Output(size=(70, 10), key='-OUTPUT-')],
    [gui.Button("Scan Folder", size=(30)), gui.Button("Buka Folder Hasil", size=(31))]
]

#Create Window
window =  gui.Window(config.appName + " - " + config.appVersion, layout)

# Display and interact with the Window
while True:
    event, values = window.read()
    
    folder_yang_discan = values["-FOLDER-"]
    read_file = values["-READ-FILE-"]
    copy_folder = values["-OPSI-COPY-FOLDER-"]
    detect_epub = values["-DETECT-EPUB-FILE-"]
    change_name_file = values["-CHANGE-NAME-FILE-"]

    if event == gui.WIN_CLOSED:
        break
    if event == "Scan Folder":
        if os.path.exists(folder_yang_discan):
            scan_folder.ScanFolder(folder_yang_discan, read_file, copy_folder, detect_epub, change_name_file)
        else:
            print("Folder Tidak Ada")
    if event == "Buka Folder Hasil":
        utils.bukaFolder("Hasil")
    

window.close()