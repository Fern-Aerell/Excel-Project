import PySimpleGUI as gui
import config
from utils import utils
import os
from logic import scan_folder
from ui import popup

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
    [gui.Button("Scan Folder", size=(27)), gui.Button("Buka Folder Hasil", size=(26)), gui.Button("Credits")]
]

#Create Window
window =  gui.Window(config.appName, layout)

# Display and interact with the Window
while True:
    event, values = window.read()

    if event == gui.WIN_CLOSED:
        break
    if event == "Scan Folder":
        folder_yang_discan = values["-FOLDER-"]
        if os.path.exists(folder_yang_discan):
            read_file = values["-READ-FILE-"]
            copy_folder = values["-OPSI-COPY-FOLDER-"]
            detect_epub = values["-DETECT-EPUB-FILE-"]
            change_name_file = values["-CHANGE-NAME-FILE-"]
            scan_folder.ScanFolder(folder_yang_discan, read_file, copy_folder, detect_epub, change_name_file)
        else:
            print("Folder Tidak Ada")
    if event == "Buka Folder Hasil":
        utils.bukaFolder("Hasil")
    if event == "Credits":
        popup.creditspopup()
    

window.close()