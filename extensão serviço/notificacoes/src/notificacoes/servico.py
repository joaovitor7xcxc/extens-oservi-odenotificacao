import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .templates import boas_vindas

logger = logging.getLogger(__name__)


def enviar_email(destinatario: str, assunto: str, corpo: str, html: str = None) -> bool:
    logger.info("Enviando e-mail para %s", destinatario)

    mensagem = MIMEMultipart("alternative")
    mensagem["To"] = destinatario
    mensagem["Subject"] = assunto
    mensagem.attach(MIMEText(corpo, "plain"))
    if html is not None:
        mensagem.attach(MIMEText(html, "html"))

    print(f"[EMAIL] Para: {destinatario} | Assunto: {assunto} | Corpo: {corpo}")
    if html is not None:
        print(f"[EMAIL] HTML: {html}")

    return True


def enviar_boas_vindas(nome: str, email: str) -> bool:
    template = boas_vindas(nome)
    return enviar_email(email, template["assunto"], template["corpo"])
