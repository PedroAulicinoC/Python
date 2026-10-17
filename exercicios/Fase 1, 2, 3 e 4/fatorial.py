def fatorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

minutos = int(input("Digite os minutos atuais: "))

senha = "LIBERDADE" + str(fatorial(minutos))
print("A senha é: ", senha)