import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def enviar_email(usuario, senha, destinatario, assunto, texto, arquivo):
    # Substitua "smtp.exemplo.com" e 587 pelo seu servidor SMTP e porta
    servidor = smtplib.SMTP(host="smtp.exemplo.com", port=587)  
    servidor.starttls()

    servidor.login(usuario, senha)

    msg = MIMEMultipart()
    msg["From"] = usuario
    msg["To"] = destinatario
    msg["Subject"] = assunto

    msg.attach(MIMEText(texto, "plain"))

    with open(arquivo, "rb") as file:
        dados = file.read()

    # Use o nome do arquivo para o anexo
    anexo = MIMEApplication(dados, _subtype="xlsx")
    anexo.add_header("Content-Disposition", "attachment", filename=arquivo.split(r"C:\Users\lucas\OneDrive\Área de Trabalho\automatizacao_gmail\Horas complementares.xlsx")[-1])  # Use apenas o nome do arquivo
    msg.attach(anexo)

    servidor.send_message(msg)
    servidor.quit()
