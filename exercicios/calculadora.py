# Variáveis para formatação do texto
negrito = "\033[1m"
sublinhado = "\033[4m"
texto_normal = "\033[0m"

# Variáveis para o cálculo
primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

# Verifica se os inputs podem ser convertidos para float antes de executar o código
try:
    primeiro_valor = float(primeiro_valor)
    segundo_valor = float(segundo_valor)
except ValueError:
    print(f"{negrito}Erro! O valor digitado não é um número!{texto_normal}")
    exit()

soma = primeiro_valor + segundo_valor
print(f"A {sublinhado}soma{texto_normal} desses dois valores é {negrito}{soma:.2f}{texto_normal}")

subtracao = primeiro_valor - segundo_valor
print(f"A {sublinhado}subtração{texto_normal} entre os valores é {negrito}{subtracao:.2f}{texto_normal}")

if segundo_valor != 0:
    divisao = primeiro_valor / segundo_valor
    print(f"A {sublinhado}divisão{texto_normal} entre os valores é {negrito}{divisao:.2f}{texto_normal}")
else:
    print(f"{negrito}Não é possível dividir por zero!{texto_normal}")

multiplicacao = primeiro_valor * segundo_valor
print(f"A {sublinhado}multiplicação{texto_normal} entre os valores é {negrito}{multiplicacao:.2f}{texto_normal}")
