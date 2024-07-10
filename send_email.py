import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import requests

def get_commit_author_email(repo, commit_sha, github_token):
    url = f"https://api.github.com/repos/{repo}/commits/{commit_sha}"
    headers = {
        "Authorization": f"token {github_token}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    commit_data = response.json()
    email = commit_data['commit']['author']['email']
    print(f"Author email: {email}")
    return email

def send_email(subject, body, to_address, from_address, smtp_server, smtp_port, username, password):
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username, password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        print("Email enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

if __name__ == "__main__":
    repo = os.getenv('GITHUB_REPOSITORY')
    commit_sha = os.getenv('GITHUB_SHA')
    github_token = os.getenv('GITHUB_TOKEN')

    subject = "Assunto do Email"
    body = "Corpo do email. Pode incluir <b>HTML</b> se necessário."
    from_address = os.getenv('FROM_EMAIL')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT'))
    username = os.getenv('SMTP_USERNAME')
    password = os.getenv('SMTP_PASSWORD')

    print(f"Repo: {repo}")
    print(f"Commit SHA: {commit_sha}")
    print(f"From address: {from_address}")
    print(f"SMTP server: {smtp_server}")
    print(f"SMTP port: {smtp_port}")
    print(f"SMTP username: {username}")

    to_address = get_commit_author_email(repo, commit_sha, github_token)

    send_email(subject, body, to_address, from_address, smtp_server, smtp_port, username, password)
