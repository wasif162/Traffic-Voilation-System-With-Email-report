import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime

fromEmail = 'du.rana.internet@gmail.com'
fromEmailPassword = 'duinternet'
toEmail = 'du.rana.internet@gmail.com'
now = datetime.now()


def sendEmail(data):
    vno = "Violation No.: " + str(data[0])
    label = data[1]
    name = "Violation Name: " + data[2]
    dt_string = now.strftime("%B %d, %Y %H:%M:%S")

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Security Update'
    msgRoot['From'] = fromEmail
    msgRoot['To'] = toEmail
    msgRoot.preamble = 'Violation Detected Camera Update'

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    msgText = MIMEText('Violation Detected ')
    msgAlternative.attach(msgText)

    msgText = MIMEText(
        '<br><h1>Violation Detected <h1><br> ' + vno + '<br> ' + label + '<br> ' + name + '<br> ' + dt_string + '<br><br><img src="cid:image1">',
        'html')
    msgAlternative.attach(msgText)

    fp = open('image1.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(fromEmail, fromEmailPassword)
    smtp.sendmail(fromEmail, toEmail, msgRoot.as_string())
    smtp.quit()
