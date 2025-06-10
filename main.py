import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Define o escopo a ser usado para acessar o documento, nesse caso esta configurado para leitura apenas
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

def gerador_de_mensagens(dividas_de_fulano):
    # Lê o conteúdo original do template 
    with open("./template.txt", "r", encoding='utf-8') as mensagem:
        template = mensagem.read()

        nome_novo = dividas_de_fulano[0]['Dividido com']
        template = template.replace("[nome]", nome_novo)
        dividas_e_valores = []
        total_dividas = 0
        
    # Para cada dívida, gera um novo arquivo, substituindo com as informações de cada pessoa
    for cada_divida in dividas_de_fulano:
      dividas = cada_divida['Dívida']
      valores = cada_divida['Valor (R$)']
      total_dividas += float(valores.replace(',', '.'))
      dividas_e_valores.append(dividas)
      dividas_e_valores.append(valores)

    template = template.replace("[lista_dividas]", "\n".join(dividas_e_valores))
    template = template.replace("[total]", str(total_dividas))
        
    with open(f"./Output/mensagem_para_{nome_novo}.txt", "w", encoding='utf-8') as novas_mensagens:
        novas_mensagens.write(template)
    
def main():
  # Validação da API do Google Sheets para primeiro acesso
  creds = None
  
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Chama a API do Google Sheets, define qual planilha acessar e qual o intervalo
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId="1-vIDZPtQryaBwpI2lUmwVCDNXbFU2jC0WaAmxdUtuNQ", range="Quem me deve!A1:E25")
        .execute()
    )
    # Armazena os valores da planilha para manipulação
    values = result.get("values", [])
    
    chaves = values[0]
    lista_de_devedores = []

    # Criação de um dicionário relacionando os dados com suas respectivas colunas
    for linha in values[1:]:
        d = {}
        for i, chave in enumerate(chaves):
            d[chave] = linha[i]
        lista_de_devedores.append(d)

    bia_dividas = [divida for divida in lista_de_devedores if divida['Dividido com'] == 'Bia']
    pedro_dividas   = [divida for divida in lista_de_devedores if divida['Dividido com'] == 'Pedro']
    tony_dividas    = [divida for divida in lista_de_devedores if divida['Dividido com'] == 'Tony']
    sophia_dividas  = [divida for divida in lista_de_devedores if divida['Dividido com'] == 'Sophia']
    gabriel_dividas = [divida for divida in lista_de_devedores if divida['Dividido com'] == 'Gabriel']
    zeca_dividas    = [divida for divida in lista_de_devedores if divida['Dividido com'] == 'Zeca']

    # Chamando a função que cria a mensagem a ser enviada com base em um template
    gerador_de_mensagens(bia_dividas)
    gerador_de_mensagens(pedro_dividas)
    gerador_de_mensagens(tony_dividas)
    gerador_de_mensagens(sophia_dividas)
    gerador_de_mensagens(gabriel_dividas)
    gerador_de_mensagens(zeca_dividas)
    
  except HttpError as err:
    print(err)

if __name__ == "__main__":
  main()