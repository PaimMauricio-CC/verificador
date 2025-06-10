# Verificador de Chave e Cidade

Este repositório contém um pequeno servidor em Python que verifica se uma chave e
uma cidade correspondem. Ele pode ser utilizado por outros programas para
validar essas informações antes de prosseguir com a execução.

## Instalação

1. Recomenda-se utilizar um ambiente virtual (opcional):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Execução

Inicie o servidor executando:

```bash
python verifier.py
```

Por padrão o servidor será iniciado em `http://localhost:5000`.

## Uso

Envie uma requisição `POST` para `/verify` com um corpo JSON contendo as chaves
`key` e `city`:

```bash
curl -X POST http://localhost:5000/verify \
  -H "Content-Type: application/json" \
  -d '{"key": "12345", "city": "Sao Paulo"}'
```

A resposta será um JSON indicando se a combinação é válida:

```json
{"verified": true}
```

Se a chave ou a cidade estiver incorreta, o campo `verified` será `false`.
