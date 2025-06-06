# Validador de bandeira de cartão de crédito

def identificar_bandeira(numero_cartao):
    numero_cartao = str(numero_cartao)  # Convertendo para string
    if numero_cartao.startswith('4'):
        return "Visa"
    elif numero_cartao.startswith(('51', '52', '53', '54', '55')):
        return "MasterCard"
    elif numero_cartao.startswith(('34', '37')):
        return "American Express"
    else:
        return "Bandeira desconhecida"

# Exemplo de uso
numero = input("Digite o número do cartão: ")
print("Bandeira detectada:", identificar_bandeira(numero))
