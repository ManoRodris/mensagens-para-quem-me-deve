# 🤖 Automação de Cobrança via WhatsApp com Python e Google Sheets

Este projeto é uma automação pessoal que envia mensagens de cobrança via WhatsApp com base nos dados de uma planilha no Google Sheets. A ideia surgiu da minha necessidade de organizar cobranças recorrentes de valores emprestados ou pagos por mim a terceiros, de forma rápida, personalizada e sem estresse.

## 💡 O que esse projeto faz?

1. Acessa uma planilha no Google Sheets onde registro as dívidas que terceiros têm comigo.
2. Lê os dados da aba específica com informações como: nome, descrições das dívidas, valores e formas de pagamento.
3. Organiza esses dados e monta mensagens de cobrança personalizadas contendo:
   - Nome da pessoa
   - Lista de dívidas
   - Valor total da dívida
   - Minha chave Pix para pagamento
4. Salva essas mensagens em arquivos `.txt`.
5. Envia as mensagens automaticamente pelo WhatsApp usando a biblioteca `pywhatkit`.

---

## 🛠️ Tecnologias utilizadas

- **Python 3.13.1**
- **Google Sheets API** – Para ler os dados da planilha
- **PyWhatKit** – Para envio das mensagens no WhatsApp
- **dotenv (opcional)** – Para gerenciar variáveis de ambiente de forma segura

---

## 🚀 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2. Copie os arquivos de exemplo e insira suas credenciais reais:

```bash
cp credentials_example.json credentials.json
cp token_example.json token.json
```


