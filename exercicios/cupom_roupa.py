# Variáveis para formatação do texto
negrito = "\033[1m"
sublinhado = "\033[4m"
texto_normal = "\033[0m"

# Variável para o cálculo
valor_compra = input("Informe o valor da compra realizada: R$")

# Verifica se os inputs podem ser convertidos para float antes de executar o código
try:
    valor_compra = float(valor_compra)
except ValueError:
    print(f"{negrito}Erro! O valor digitado não é um número!{texto_normal}")
    exit()

cupom = input(f"Digite '{sublinhado}NIVER10{texto_normal}' para ganhar 10% de desconto: ")

if cupom.upper() == "NIVER10":
    print(f"O valor de sua compra ficou {negrito}R${valor_compra * 0.9:.2f}{texto_normal}!")
else:
    print(f"{negrito}Erro! Cupom inválido!{texto_normal}")