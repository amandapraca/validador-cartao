# Validador de Bandeiras de Cartão de Crédito

def identificar_bandeira(numero_cartao):
    numero_cartao = str(numero_cartao)  # Convertendo para string
    
    # Verifica a bandeira do cartão
    if numero_cartao.startswith('4'):
        return "Visa"
    elif numero_cartao.startswith(('51', '52', '53', '54', '55')):
        return "MasterCard"
    elif numero_cartao.startswith(('34', '37')):
        return "American Express"
    else:
        return "Bandeira desconhecida"

# Testes com números fictícios
cartoes_teste = [
    ("4111111111111111", "Visa"),
    ("5555555555554444", "MasterCard"),
    ("371449635398431", "American Express"),
    ("6011111111111117", "Bandeira desconhecida")  # Exemplo sem mapeamento
]

# Executa os testes
for numero, esperado in cartoes_teste:
    resultado = identificar_bandeira(numero)
    print(f"Número: {numero} | Detectado: {resultado} | Esperado: {esperado}")

