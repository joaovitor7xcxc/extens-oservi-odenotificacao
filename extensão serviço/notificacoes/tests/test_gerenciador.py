from unittest.mock import patch
from notificacoes.gerenciador import GerenciadorDeNotificacoes


def test_notificar_usuario_retorna_dict_com_campos_corretos():
    with patch("notificacoes.gerenciador.servico.enviar_email", return_value=True), patch(
        "notificacoes.gerenciador.sms.enviar_codigo_verificacao", return_value=True
    ):
        gerenciador = GerenciadorDeNotificacoes()
        resultado = gerenciador.notificar_usuario(
            "Maria", "maria@email.com", "+552199999999"
        )

    assert resultado["nome"] == "Maria"
    assert resultado["email"] == "maria@email.com"
    assert resultado["telefone"] == "+552199999999"
    assert resultado["email_enviado"] is True
    assert resultado["sms_enviado"] is True


def test_notificar_usuario_chama_email_e_sms():
    with patch("notificacoes.gerenciador.servico.enviar_email", return_value=True) as mocked_email, patch(
        "notificacoes.gerenciador.sms.enviar_codigo_verificacao", return_value=True
    ) as mocked_sms:
        gerenciador = GerenciadorDeNotificacoes()
        gerenciador.notificar_usuario("Maria", "maria@email.com", "+552199999999")

    mocked_email.assert_called_once()
    mocked_sms.assert_called_once()


def test_historico_e_atualizado_apos_notificacao():
    with patch("notificacoes.gerenciador.servico.enviar_email", return_value=True), patch(
        "notificacoes.gerenciador.sms.enviar_codigo_verificacao", return_value=True
    ):
        gerenciador = GerenciadorDeNotificacoes()
        gerenciador.notificar_usuario("Maria", "maria@email.com", "+552199999999")

    assert len(gerenciador.historico) == 1


def test_resumo_conta_envios_corretamente():
    with patch("notificacoes.gerenciador.servico.enviar_email", return_value=True), patch(
        "notificacoes.gerenciador.sms.enviar_codigo_verificacao", return_value=True
    ):
        gerenciador = GerenciadorDeNotificacoes()
        for _ in range(3):
            gerenciador.notificar_usuario("Maria", "maria@email.com", "+552199999999")

    resumo = gerenciador.resumo()
    assert resumo["total"] == 3
    assert resumo["emails_enviados"] == 3
    assert resumo["sms_enviados"] == 3
    assert resumo["falhas_email"] == 0
    assert resumo["falhas_sms"] == 0


def test_reenviar_falhas_reenvia_canais_falhos():
    with patch("notificacoes.gerenciador.servico.enviar_email", side_effect=[False, True]) as mocked_email, patch(
        "notificacoes.gerenciador.sms.enviar_codigo_verificacao", side_effect=[False, True]
    ) as mocked_sms:
        gerenciador = GerenciadorDeNotificacoes()
        gerenciador.notificar_usuario("Maria", "maria@email.com", "+552199999999")
        reenviados = gerenciador.reenviar_falhas()

    assert reenviados == 2
    assert gerenciador.historico[0]["email_enviado"] is True
    assert gerenciador.historico[0]["sms_enviado"] is True
    assert mocked_email.call_count == 2
    assert mocked_sms.call_count == 2


def test_exportar_historico_salva_json_corretamente(tmp_path):
    with patch("notificacoes.gerenciador.servico.enviar_email", return_value=True), patch(
        "notificacoes.gerenciador.sms.enviar_codigo_verificacao", return_value=True
    ):
        gerenciador = GerenciadorDeNotificacoes()
        gerenciador.notificar_usuario("Maria", "maria@email.com", "+552199999999")

    arquivo = tmp_path / "historico.json"
    gerenciador.exportar_historico(str(arquivo))

    conteudo = arquivo.read_text(encoding="utf-8")
    assert "Maria" in conteudo
    assert "+552199999999" in conteudo
    assert "email_enviado" in conteudo
    assert "sms_enviado" in conteudo
