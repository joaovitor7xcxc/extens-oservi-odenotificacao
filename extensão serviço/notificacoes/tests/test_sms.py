import pytest
from unittest.mock import patch
from notificacoes.sms import enviar_sms, enviar_codigo_verificacao


def test_enviar_sms_sucesso(monkeypatch):
    monkeypatch.setenv("SMS_REMETENTE", "+5511000000000")
    assert enviar_sms("+5521888880000", "Teste de SMS") is True


def test_sem_remetente_levanta_erro(monkeypatch):
    monkeypatch.delenv("SMS_REMETENTE", raising=False)
    with pytest.raises(EnvironmentError, match="SMS_REMETENTE"):
        enviar_sms("+5521888880000", "Teste de SMS")


def test_enviar_codigo_verificacao(monkeypatch):
    monkeypatch.setenv("SMS_REMETENTE", "+5511000000000")
    with patch("notificacoes.sms.enviar_sms", return_value=True) as mocked:
        assert enviar_codigo_verificacao("+5521888880000", "123456") is True
        mocked.assert_called_once_with(
            "+5521888880000", "Seu código de verificação é: 123456"
        )
