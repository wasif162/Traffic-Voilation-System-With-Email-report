import numpy as np
import cv2
import PySimpleGUI as sg
import pytesseract
import mail

file = ""
layout = [[sg.Text("Choose a Image: "), sg.Input(key='-IMAGE_LOCATION-'), sg.FileBrowse(), sg.Button('Check')]]
window = sg.Window('Number Plate Extractor', layout, element_justification='center', finalize=True, resizable=True)

while True:
    event, values = window.read(timeout=1000)  # run with a timeout so that current location can be updated
    if event == sg.WIN_CLOSED:
        break
    if event == 'Check':
        if values['-IMAGE_LOCATION-'] and not 'Video URL' in values['-IMAGE_LOCATION-']:
            file = values['-IMAGE_LOCATION-']
            break

window.close()

def numberPlate(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray, 170, 200)
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
    NumberPlateCnt = None
    count = 0
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            NumberPlateCnt = approx
            break

    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [NumberPlateCnt], 0, 255, -1)
    new_image = cv2.bitwise_and(image, image, mask=mask)
    cv2.namedWindow("Final_image", cv2.WINDOW_NORMAL)
    cv2.imshow("Final_image", new_image)
    # cv2.imshow("Final_image", image)
    config = '-l eng --oem 1 --psm 3'
    text = pytesseract.image_to_string(new_image, config=config)
    cv2.waitKey(0)
    dcnt = 1
    label = text
    lat = 'Number Plate'
    data = [dcnt, label, lat]
    mail.sendEmail(data)
    return text

# numberPlate(image)

image = cv2.imread(file)

print(numberPlate(image))
