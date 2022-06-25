import PySimpleGUI as sg


def noPlate():
    import noplate


def carVio():
    import car


def speedVio():
    import Speed



def seatVio():
    import Seat
    Seat.main()


layout = [[sg.Text('Traffic Violation System')],
          [sg.Button('Number Plate Extractor'), sg.Button('Traffic Light Violation'), sg.Button('Speed Violation'), sg.Button('Seat Belt Violation')]]

window = sg.Window('Traffic Violation System', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Number Plate Extractor':
        noPlate()
    elif event == 'Traffic Light Violation':
        carVio()
    elif event == 'Speed Violation':
        speedVio()
    elif event == 'Seat Belt Violation':
        seatVio()

window.close()
