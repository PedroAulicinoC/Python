# Variáveis para formatação do texto
negrito = "\033[1m"
texto_normal = "\033[0m"

# Variáveis para o código
email_aluno = input("E-mail do aluno: ")
nota_aluno = input("Nota do aluno: ")

# Verifica se os inputs podem ser convertidos para float antes de executar o código
try:
    nota_aluno = float(nota_aluno)
except ValueError:
    print(f"{negrito}Erro! O valor digitado não é um número!{texto_normal}")
    exit()

if nota_aluno > 10 or nota_aluno < 0:
    print("Porfavor digitar um valor entre 0 e 10.")
    exit()
else:
    if(nota_aluno > 8.5):
        print(f"Enviando convite para {email_aluno}...")

    else:
        print(f"O aluno com o e-mail {email_aluno} não atingiu a nota mínima de 8.5 para receber o convite.")
