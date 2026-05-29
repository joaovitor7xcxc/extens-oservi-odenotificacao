import json
import random

from . import servico, sms, templates


class GerenciadorDeNotificacoes:
    def __init__(self):
        self.historico: list[dict] = []

    def notificar_usuario(self, nome: str, email: str, telefone: str) -> dict:
        conteudo = templates.boas_vindas(nome)
        email_enviado = servico.enviar_email(email, conteudo["assunto"], conteudo["corpo"])
        codigo = str(random.randint(100000, 999999))
        sms_enviado = sms.enviar_codigo_verificacao(telefone, codigo)

        registro = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "email_enviado": email_enviado,
            "sms_enviado": sms_enviado,
        }
        self.historico.append(registro)
        return registro

    def reenviar_falhas(self) -> int:
        reenviados = 0
        for registro in self.historico:
            if not registro["email_enviado"]:
                conteudo = templates.boas_vindas(registro["nome"])
                registro["email_enviado"] = servico.enviar_email(
                    registro["email"], conteudo["assunto"], conteudo["corpo"]
                )
                reenviados += 1

            if not registro["sms_enviado"]:
                codigo = str(random.randint(100000, 999999))
                registro["sms_enviado"] = sms.enviar_codigo_verificacao(registro["telefone"], codigo)
                reenviados += 1

        return reenviados

    def resumo(self) -> dict:
        total = len(self.historico)
        emails_enviados = sum(1 for registro in self.historico if registro["email_enviado"])
        sms_enviados = sum(1 for registro in self.historico if registro["sms_enviado"])
        falhas_email = sum(1 for registro in self.historico if not registro["email_enviado"])
        falhas_sms = sum(1 for registro in self.historico if not registro["sms_enviado"])

        return {
            "total": total,
            "emails_enviados": emails_enviados,
            "sms_enviados": sms_enviados,
            "falhas_email": falhas_email,
            "falhas_sms": falhas_sms,
        }

    def exportar_historico(self, caminho: str) -> None:
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(self.historico, arquivo, ensure_ascii=False, indent=2)
