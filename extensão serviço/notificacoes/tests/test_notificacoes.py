from notificacoes.servico import enviar_boas_vindas, enviar_email


def test_enviar_boas_vindas_retorna_true():
    assert enviar_boas_vindas("Maria", "maria@email.com") is True


def test_enviar_email_html_anexa_html(capsys):
    enviar_email("maria@email.com", "Boas-vindas", "Texto simples", "<p>Olá</p>")
    captured = capsys.readouterr()
    assert "[EMAIL] HTML: <p>Olá</p>" in captured.out
