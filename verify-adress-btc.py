import requests
from bitcoinlib.keys import Address

def verificar_endereco_btc(endereco):
    try:
        addr = Address(endereco)
        return f"Endereço válido: {addr.address}"
    except Exception as e:
        return f"Endereço inválido: {e}"

def verificar_saldo_btc(endereco):
    url = f"https://blockchain.info/balance?active={endereco}"
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        saldo_satoshis = dados[endereco]['final_balance']
        saldo_btc = saldo_satoshis / 100000000  
        return f"Saldo do endereço {endereco}: {saldo_btc} BTC"
    except Exception as e:
        return f"Erro ao buscar saldo: {e}"


endereco = input("Digite um endereço de Bitcoin: ")
resultado = verificar_endereco_btc(endereco)
print(resultado)

if "Endereço válido" in resultado:
    saldo = verificar_saldo_btc(endereco)
    print(saldo)
