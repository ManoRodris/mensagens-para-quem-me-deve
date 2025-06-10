import pywhatkit as kit
import time

# Mapeamento de contatos com arquivos .txt
contatos = {
    "75922225555": f"./Output/mensagem_para_Fulano.txt",
    "11922225555": f"./Output/mensagem_para_Beltrano.txt"
}

# Enviar mensagens
for numero, arquivo in contatos.items():
    with open(arquivo, "r", encoding="utf-8") as f:
        mensagem = f.read()

    # Envia mensagem via WhatsApp Web (espera 20 segundos)
    kit.sendwhatmsg_instantly(
        phone_no=numero,
        message=mensagem,
        wait_time=20,
        tab_close=True
    )

    time.sleep(10)  # Espera para o próximo envio
