import smtplib
from email.mime.multipart import MIMEMultipart
from string import Template


def email_sent():
    print("sending email ")
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('sportnowapi@gmail.com', 'vsjttrxislofsmot')
    msg = MIMEMultipart()
    message_template = read_template('webapp/message.html')
    message = message_template.substitute(Message="Test")
    msg['From'] = 'SportNow'
    msg['To'] = 'andre2inggs@gmail.com'
    msg['Cc'] = 'sportsowapi@gmail.com'
    msg['Subject'] = 'Join Sport Event Link'
    msg.attach(message, 'html')
    server.send_message(msg)
    server.quit()
    print('Email sent ')


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


if __name__ == '__main__':
    email_sent()