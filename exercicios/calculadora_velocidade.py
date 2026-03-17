# Variáveis para formatação do texto
negrito = "\033[1m"
sublinhado = "\033[4m"
texto_normal = "\033[0m"

print(f"{negrito}Esse programa calcula a velocidade média de um objeto!{texto_normal}")

# Variáveis para o cálculo
distancia = input(f"Qual foi a {sublinhado}distância em metros{texto_normal} percorrida pelo objeto? ")
tempo = input(f"{sublinhado}Quantos minutos{texto_normal} o objeto demorou para percorrer essa distância? ")

# Verifica se os inputs podem ser convertidos para float antes de executar o código
try:
    distancia = float(distancia)
    tempo = float(tempo)
except ValueError:
    print(f"{negrito}Erro! O valor digitado não é um número!{texto_normal}")
    exit()

#Verifica se os valores são maiores do que zero
if distancia and tempo > 0:
    velocidade_media = distancia / tempo
else:
    print(f"{negrito}Valores inválidos!{texto_normal}")
    exit()

print(f"O objeto atingiu uma velocidade de {negrito}{velocidade_media:.2f}{texto_normal} m/min!")