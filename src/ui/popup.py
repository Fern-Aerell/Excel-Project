def creditspopup():
    import PySimpleGUI as gui
    import config
    import os

    #Create Window Content
    column = [
        [gui.Text("     Versi : " + config.appVersion + "       ")],
        [gui.Text("     Create By : AerellDev       ")],
        [gui.Text("")],
        [gui.Button("Kembali")]
    ]

    layout = [[gui.Column(column, element_justification='center')]]

    #Create Window
    window =  gui.Window("Credits", layout, grab_anywhere=True)

    # Display and interact with the Window
    while True:
        event, values = window.read()

        if event == gui.WIN_CLOSED:
            break
        if event == "Kembali":
            break
        

    window.close()