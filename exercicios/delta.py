import math

# Variáveis para formatação do texto
negrito = "\033[1m"
texto_normal = "\033[0m"

# Variáveis para o cálculo
a = input("Informe o valor de A: ")
b = input("Informe o valor de B: ")
c = input("Informe o valor de C: ")

# Verifica se os inputs podem ser convertidos para float antes de executar o código
try:
    a = float(a)
    b = float(b)
    c = float(c)
except ValueError:
    print(f"{negrito}Erro! O valor digitado não é um número!{texto_normal}")
    exit()

#Verifica se o valor de A é maior do que zero
if a == 0:
    print(f"{negrito}Erro! O valor de A não pode ser zero!{texto_normal}")
    exit()

delta = b * b - 4 * a * c

if delta > 0.0:
    x1= (-b + math.sqrt(delta)) / (2 * a)
    x2= (-b - math.sqrt(delta)) / (2 * a)

    print(f"Para a equação {a}x² + {b}x + {c} = 0, obtivemos os seguintes valores: x1 = {negrito}{x1}{texto_normal} e x2 = {negrito}{x2}{texto_normal}.")

elif delta == 0:
    x = (-b + math.sqrt(delta)) / (2 * a)
    print(f"Para a equação {a}x² + {b}x + {c} = 0, obtivemos o seguinte valor: x = {negrito}{x}{texto_normal}.")

else:
    print(f"Para a equação {a}x² + {b}x + {c} = 0, {negrito}não existem valores reais para x{texto_normal}.")