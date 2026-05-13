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

candidatas = sorted(letras_definidas - letras_usadas)

letra_inicial = None
for c in candidatas:
    if regras[c] != "":
        letra_inicial = c
        break

if letra_inicial is None:
    letra_inicial = candidatas[0]


memo = {}

for letra, sub in regras.items():
    if sub == "":
        memo[letra] = 1

inicio = time.time()

mudou = True
while mudou:
    mudou = False
    
    for letra, sub in regras.items():
        if letra in memo:
            continue
        pronto = True
        total = 0
        for c in sub:
            if c not in memo:
                pronto = False
                break
            total += memo[c]
        if pronto:
            memo[letra] = total
            mudou = True

resultado = memo[letra_inicial]

fim = time.time()

print("Letra inicial:", letra_inicial)
print("Tamanho final:", resultado)
print("Tempo de execução:", (fim - inicio) * 1000, "milisegundos")