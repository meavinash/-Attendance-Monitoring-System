import os
import smtplib
from email.message import EmailMessage

EMAIL_A = os.environ.get('EMAIL_ADDRESS')
EMAIL_P = os.environ.get('EMAIL_PASSWORD')

msg = EmailMessage()
msg['Subject'] = 'Attendance'
msg['From'] = EMAIL_A
msg['To'] = 'emeraldtula@gmail.com'
msg.set_content('Attendance attached.')

files = ['FinalAttendance.csv']

for file in files:
    with open('FinalAttendance.csv', 'rb') as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_A, EMAIL_P)
    smtp.send_message(msg)
