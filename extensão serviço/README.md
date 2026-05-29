# Extensão do Serviço de Notificações

Este projeto implementa um sistema de notificações multi-canal em Python, incluindo:

- serviço de e-mail simulado (`servico.py`)
- serviço de SMS simulado (`sms.py`)
- templates de mensagem reutilizáveis (`templates.py`)
- gerenciador de notificações com histórico (`gerenciador.py`)

## Como usar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute os testes:

```bash
python -m pytest notificacoes/tests -v
```

## Estrutura

- `notificacoes/src/notificacoes/`
  - `servico.py`
  - `sms.py`
  - `templates.py`
  - `gerenciador.py`
- `notificacoes/tests/`
  - `test_notificacoes.py`
  - `test_sms.py`
  - `test_templates.py`
  - `test_gerenciador.py`
