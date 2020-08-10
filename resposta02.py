def imprima(num):
    parada = num + 1
    resposta = ''
    for i in range (1, parada):
        parada_j = i + 1
        for j in range(1, parada_j):
            resposta += str(j) + ' '
        resposta += '\n'
    return resposta

numero = int(input("Informe o numero de respetições: "))

print(imprima(numero))