import io
import os
import PySimpleGUI as sg
from PIL import Image
import mail
import cv2


def main():
    layout = [[sg.Text(font=("Helvetica", 25), size=(20,1), key='-OUTPUT-')],
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(),
            sg.Button("Load Image"),
        ],
    ]
    window = sg.Window("Image Viewer", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
                filename = str(values["-FILE-"])
                if 'no' in filename:
                    char = 'Seat Belt Not Detected'
                    imgg = cv2.imread(filename)
                    cv2.imwrite("image1.jpg", imgg)
                    data = ['1', 'Speed', 'Seat Belt Violation']
                    mail.sendEmail(data)
                else:
                    char = 'Seat Belt Detected'
                window['-OUTPUT-'].update(char)
    window.close()


if __name__ == "__main__":
    main()
