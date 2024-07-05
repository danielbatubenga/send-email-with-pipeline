import smtplib
import subprocess

# Função para obter o email do autor do último commit
def get_last_commit_author_email():
    result = subprocess.run(['git', 'log', '-1', '--pretty=format:%ae'], capture_output=True, text=True)
    return result.stdout.strip()

# Credenciais de e-mail
smtp_server = 'smtp.office365.com'
smtp_port = 587
username = 'danielbatubenga@outlook.com'
password = 'pa$$w0rd@@12'

# Verificação das credenciais
if not username or not password:
    raise ValueError('Credenciais de e-mail não configuradas corretamente.')

# Informações de remetente e destinatário
from_email = username
try:
    to_email = get_last_commit_author_email()
except Exception as e:
    raise ValueError('Não foi possível obter o e-mail do autor do último commit.')

subject = 'Notificação do Commit'
body = f'O commit mais recente foi feito por {to_email}'

# Configuração do servidor SMTP
smtp_obj = smtplib.SMTP(smtp_server, smtp_port)
smtp_obj.starttls()  # Iniciar conexão TLS

# Login no servidor SMTP com tratamento de erros
try:
    smtp_obj.login(username, password)
except smtplib.SMTPAuthenticationError as e:
    print(f'Falha ao autenticar: {e}')
    smtp_obj.quit()
    exit(1)
except Exception as e:
    print(f'Erro ao conectar ao servidor SMTP: {e}')
    smtp_obj.quit()
    exit(1)

# Criar mensagem de e-mail
msg = f'From: {from_email}\nTo: {to_email}\nSubject: {subject}\n\n{body}'

# Envio do e-mail com tratamento de erros
try:
    smtp_obj.sendmail(from_email, to_email, msg)
    print(f'E-mail enviado com sucesso para: {to_email}')
except Exception as e:
    print(f'Falha ao enviar o e-mail: {e}')

# Encerrar conexão SMTP
smtp_obj.quit()
