import pytest
import sys
import os
from unittest.mock import patch, MagicMock

# Adiciona o diretório src ao caminho do sistema
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from email_sender import enviar_email

@patch('smtplib.SMTP')  # Mock do SMTP
def test_enviar_email(mock_smtp):
    # Arrange
    usuario = "teste@exemplo.com"
    senha = "senha"
    destinatario = "destinatario@exemplo.com"
    assunto = "Assunto"
    texto = "Olá!\nEste e-mail foi enviado por um robô Python...\n"
    arquivo = r"C:\Users\lucas\OneDrive\Área de Trabalho\automatizacao_gmail\Horas complementares.xlsx"
    host = "smtp.exemplo.com"  # Substitua pelo seu host SMTP
    port = 587  # Substitua pela porta correta

    mock_smtp_instance = MagicMock()
    mock_smtp.return_value = mock_smtp_instance

    # Act
    enviar_email(usuario, senha, destinatario, assunto, texto, arquivo)

    # Assert
    mock_smtp.assert_called_once_with(host=host, port=port)
    mock_smtp_instance.starttls.assert_called_once()
    mock_smtp_instance.login.assert_called_once_with(usuario, senha)
    assert mock_smtp_instance.send_message.call_count == 1
    assert mock_smtp_instance.quit.call_count == 1
