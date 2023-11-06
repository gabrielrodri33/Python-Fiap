import smtplib
from email.mime.text import MIMEText

def verificacaoEmail():
    server_smtp = "smtp.gmail.com"
    smtp_port = 587

    sender = "gabrielrodri333@gmail.com"
    receiver = "gabrielkeeper2@gmail.com"
    topic = "Verificação de email"
    body = "Código"

    message = MIMEText(body)
    message['Subject'] = topic
    message['From'] = sender
    message['To'] = receiver

    server = smtplib.SMTP(server_smtp, smtp_port)
    server.starttls()
    username = "gabrielrodri333@gmail.com"
    password = "Fiap2023"
    server.login(username, password)

    server.sendmail(sender, receiver, message.as_string())

    server.quit()

    print('Email enviado!')

verificacaoEmail()