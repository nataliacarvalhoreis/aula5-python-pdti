# Faça um programa que converta da notação de 24 horas para a notação
# de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
# A entrada é dada em dois inteiros. Deve haver pelo menos duas funções:
# uma para fazer a conversão e uma para a saída. Registre a informação
# A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para
# efetuar as conversões terá um parâmetro formal para registrar se é A.M.
# ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para
# novos valores de entrada todas as vezes que desejar

def converter(hora, minuto):
    if hora>12:
        fuso = 'PM'
        nova_hora = hora - 12
    else:
        fuso = 'AM'
        nova_hora = hora
    return str(str(nova_hora) + ':' + str(minuto)+fuso)

print("Informe 0 para as horas quando desejar parar!")
hora = int(input("Informe as horas: "))
while hora != 0:
    minuto = int(input("Informe os minutos: "))
    if hora > 0 and hora < 25 and minuto>0 and minuto < 60:
        print(converter(hora, minuto))
    else:
        print("Informe uma hora válida!")
    hora = int(input("Informe as horas: "))