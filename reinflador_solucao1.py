import time

ARQUIVO = "casos_30/t30_01.txt"

regras = {}

with open(ARQUIVO, "r") as f:
    for linha in f:
        linha = linha.strip()
        if linha == "":
            continue
        
        partes = linha.split()
        
        if len(partes) == 1:
            regras[partes[0]] = ""
        else:
            regras[partes[0]] = partes[1]

letras_definidas = set(regras.keys())
letras_usadas = set()

for sub in regras.values():
    for c in sub:
        letras_usadas.add(c)

letra_inicial = list(letras_definidas - letras_usadas)[0]

memo = {}

def tamanho(letra):
    if letra in memo:
        return memo[letra]
    
    sub = regras[letra]
    
    if sub == "":
        memo[letra] = 1
        return 1
    
    lista = []
    for c in sub:
        lista.append(tamanho(c))
    
    total = sum(lista)
    
    memo[letra] = total
    return total

inicio = time.time()

resultado = tamanho(letra_inicial)

fim = time.time()

print("Letra inicial:", letra_inicial)
print("Tamanho final:", resultado)
print("Tempo de execução:", (fim - inicio) * 1000, "milisegundos")