Este projeto permite o envio de e-mails automatizados com anexos em formato Excel utilizando a biblioteca smtplib do Python. Ele é ideal para automatizar tarefas como envio de documentos, relatórios ou mensagens personalizadas.

# Objetivo

Automatizar o envio de e-mails com:

Mensagens personalizadas.

Arquivos anexados (como planilhas ou documentos).

# Tecnologias Utilizadas

Python

smtplib: Para envio de e-mails via protocolo SMTP.

email.mime: Para criar e formatar mensagens com texto e anexos.

# Como Funciona

O script se conecta a um servidor SMTP utilizando as credenciais do remetente.

Uma mensagem de e-mail é criada com:

Remetente

Destinatário

Assunto

Texto do corpo do e-mail

Anexo (arquivo Excel)

A mensagem é enviada para o destinatário informado.

# Pré-requisitos

Python 3.9 ou superior instalado.

Acesso a um servidor SMTP válido (como Gmail, Outlook, etc.).

Certifique-se de que o servidor SMTP permite conexões de aplicativos externos.

Para Gmail, ative a opção "Permitir apps menos seguros" ou crie uma senha de aplicativo.

Biblioteca necessária:

'''bash
Copiar código
pip install secure-smtplib
'''
