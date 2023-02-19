import os

def buatFolderJikaTidakAda(folder_nama):
    if not os.path.exists(folder_nama):
        os.makedirs(folder_nama)

def bukaFolder(folder_nama):
    os.startfile(folder_nama)