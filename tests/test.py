import pytest
import sys
import os
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from email_sender import enviar_email

@patch('smtplib.SMTP')  # Mock do SMTP
@patch('builtins.open', new_callable=MagicMock)  # Mock do open
def test_enviar_email(mock_open, mock_smtp):
    usuario = "teste@exemplo.com"
    senha = "senha"
    destinatario = "destinatario@exemplo.com"
    assunto = "Assunto"
    texto = "Olá!\nEste e-mail foi enviado por um robô Python...\n"
    
    # Simule um arquivo válido, aqui usando um nome fictício
    arquivo = "caminho/para/o/arquivo.xlsx"  # Um caminho para um arquivo que você espera ler

    host = "smtp.exemplo.com"
    port = 587 

    mock_smtp_instance = MagicMock()
    mock_smtp.return_value = mock_smtp_instance

    # Simula o comportamento de open e read, retornando bytes
    mock_open.return_value.__enter__.return_value.read.return_value = b'Teste de anexo'  # Simulando bytes lidos de um arquivo

    enviar_email(usuario, senha, destinatario, assunto, texto, arquivo)

    mock_smtp.assert_called_once_with(host=host, port=port)
    mock_smtp_instance.starttls.assert_called_once()
    mock_smtp_instance.login.assert_called_once_with(usuario, senha)
    
    # Verifica se send_message foi chamado
    assert mock_smtp_instance.send_message.call_count == 1

    # Verifica se quit foi chamado
    assert mock_smtp_instance.quit.call_count == 1

    # Verifica se open foi chamado para ler o arquivo
    mock_open.assert_called_once_with(arquivo, "rb")
