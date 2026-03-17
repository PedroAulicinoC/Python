# Variáveis para formatação do texto
negrito = "\033[1m"
sublinhado = "\033[4m"
texto_normal = "\033[0m"

# Variáveis para o código
valor = input("Digite o valor da viagem: R$")
assento = input(f"Você está viajando na classe {sublinhado}Econômica{texto_normal}, {sublinhado}Executiva{texto_normal} ou {sublinhado}Primeira Classe{texto_normal}? ")
numero_viajantes = input("Digite o número de viajantes: ")

# Verifica se os inputs podem ser convertidos para float antes de executar o código
try:
    valor = float(valor)
    numero_viajantes = int(numero_viajantes)
except ValueError:
    print(f"{negrito}Erro! O valor digitado não é um número!{texto_normal}")
    exit()

if numero_viajantes <= 0:
    print(f"{negrito}Número de viajantes invalido!{texto_normal}")
    exit()

if valor <= 0:
    print(f"{negrito}Valor de viagem invalido!{texto_normal}")
    exit()

if assento.upper() == "ECONÔMICA" or assento.upper() == "ECONOMICA":
    if numero_viajantes == 2:
        valor = valor * 0.97
        print(f"O valor da sua viagem é de {negrito}R${valor:.2f}{texto_normal}!")
    elif numero_viajantes == 3:
        valor = valor * 0.96
        print(f"O valor da sua viagem é de R${negrito}{valor:.2f}{texto_normal}!")
    elif numero_viajantes >= 4:
        valor = valor * 0.95
        print(f"O valor da sua viagem é de R${negrito}{valor:.2f}{texto_normal}!")
    else:
        print(f"Sem descontos para uma pessoa, o valor da sua viagem continua R${valor:.2f}.")

elif assento.upper() == "EXECUTIVA":
    if numero_viajantes == 2:
        valor = valor * 0.95
        print(f"O valor da sua viagem é de R${negrito}{valor:.2f}{texto_normal}!")
    elif numero_viajantes == 3:
        valor = valor * 0.93
        print(f"O valor da sua viagem é de R${negrito}{valor:.2f}{texto_normal}!")
    elif numero_viajantes >= 4:
        valor = valor * 0.92
        print(f"O valor da sua viagem é de R${negrito}{valor:.2f}{texto_normal}!")
    else:
        print(f"Sem descontos para uma pessoa, o valor da sua viagem continua R${valor:.2f}.")

elif assento.upper() == "PRIMEIRA CLASSE" or assento.upper() == "PRIMEIRACLASSE":
    if numero_viajantes == 2:
        valor = valor * 0.9
        print(f"O valor da sua viagem é de R${valor:.2f}!")
    elif numero_viajantes == 3:
        valor = valor * 0.85
        print(f"O valor da sua viagem é de R${valor:.2f}!")
    elif numero_viajantes >= 4:
        valor = valor * 0.8
        print(f"O valor da sua viagem é de R${valor:.2f}!")
    else:
        print(f"Sem descontos para uma pessoa, o valor da sua viagem continua R${valor:.2f}.")

else:
    print(f"{negrito}Categoria de assento não encontrada!{texto_normal}")