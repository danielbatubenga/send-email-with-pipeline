import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email(subject, body, to_address, from_address, smtp_server, smtp_port, username, password):
    # Cria a mensagem de email
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Anexa o corpo do email
    msg.attach(MIMEText(body, 'html'))

    # Conecta ao servidor SMTP e envia o email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        print("Email enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

if __name__ == "__main__":
    subject = "Assunto do Email"
    body = "Corpo do email. Pode incluir <b>HTML</b> se necessário."
    to_address = os.getenv('TO_EMAIL')
    from_address = os.getenv('FROM_EMAIL')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')
    username = os.getenv('SMTP_USERNAME')
    password = os.getenv('SMTP_PASSWORD')

    send_email(subject, body, to_address, from_address, smtp_server, smtp_port, username, password)
