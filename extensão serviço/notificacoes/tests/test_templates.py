from notificacoes.templates import boas_vindas, recuperacao_senha, confirmacao_pedido


def test_boas_vindas_retorna_assunto_e_corpo():
    resultado = boas_vindas("Maria")
    assert "assunto" in resultado
    assert "corpo" in resultado
    assert "Maria" in resultado["corpo"]


def test_recuperacao_senha_contem_link():
    link = "https://example.com/reset"
    resultado = recuperacao_senha("Maria", link)
    assert link in resultado["corpo"]


def test_confirmacao_pedido_contem_valor():
    resultado = confirmacao_pedido("Maria", "ABC123", 259.90)
    assert "ABC123" in resultado["corpo"]
    assert "259.90" in resultado["corpo"]
