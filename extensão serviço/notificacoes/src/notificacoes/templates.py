def boas_vindas(nome: str) -> dict:
    assunto = "Bem-vindo ao nosso serviço de notificações"
    corpo = (
        f"Olá {nome},\n\n"
        "Seja muito bem-vindo! Estamos felizes em tê-lo conosco. "
        "A partir de agora você receberá notificações importantes por e-mail e SMS.\n\n"
        "Um abraço,\nEquipe de Notificações"
    )
    return {"assunto": assunto, "corpo": corpo}


def recuperacao_senha(nome: str, link: str) -> dict:
    assunto = "Recuperação de senha"
    corpo = (
        f"Olá {nome},\n\n"
        "Recebemos uma solicitação para redefinir sua senha. "
        f"Clique no link abaixo para continuar:\n{link}\n\n"
        "Se você não solicitou a recuperação, ignore esta mensagem.\n\n"
        "Atenciosamente,\nEquipe de Suporte"
    )
    return {"assunto": assunto, "corpo": corpo}


def confirmacao_pedido(nome: str, numero_pedido: str, valor: float) -> dict:
    assunto = "Confirmação de pedido"
    corpo = (
        f"Olá {nome},\n\n"
        f"Seu pedido {numero_pedido} foi confirmado com sucesso. "
        f"O valor total foi de R$ {valor:.2f}.\n\n"
        "Agradecemos a preferência e em breve enviaremos novidades sobre o envio.\n\n"
        "Atenciosamente,\nEquipe de Vendas"
    )
    return {"assunto": assunto, "corpo": corpo}
