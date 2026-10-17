# Variáveis para formatação do texto
negrito = "\033[1m"
sublinhado = "\033[4m"
texto_normal = "\033[0m"

# Variáveis para o cálculo
bpm = input("Informe o seu número de batimentos por minuto: ")
idade = input("Informe a sua idade: ")

# Verifica se os inputs podem ser convertidos para int antes de executar o código
try:
    bpm = int(bpm)
    idade = int(idade)
except ValueError:
    print(f"{negrito}Erro! O valor digitado não é um número!{texto_normal}")
    exit()

if idade >= 0 and idade <= 2:
    faixa = "120 a 140"

    if bpm > 140:
        print(f"BPM {sublinhado}acima{texto_normal} da faixa adequada de {negrito}{faixa}{texto_normal}!")
    elif bpm < 120:
        print(f"BPM {sublinhado}abaixo{texto_normal} da faixa adequada de {negrito}{faixa}{texto_normal}!")
    else:
        print(f"BPM {sublinhado}dentro{texto_normal} da faixa adequada de {negrito}{faixa}{texto_normal}!")

if idade >= 3 and idade <= 7:
    faixa = "80 a 120"

    if bpm > 120:
        print(f"BPM {sublinhado}acima{texto_normal} da faixa adequada de {negrito}{faixa}{texto_normal}!")
    elif bpm < 80:
        print(f"BPM {sublinhado}abaixo{texto_normal} da faixa adequada de {negrito}{faixa}{texto_normal}!")
    else:
        print(f"BPM {sublinhado}dentro{texto_normal} da faixa adequada de {negrito}{faixa}{texto_normal}!")

if idade >= 8 and idade <= 17:
    faixa = "75 a 100"

    if bpm > 100:
        print(f"BPM {sublinhado}acima{texto_normal} da faixa adequada de {negrito}{faixa}{texto_normal}!")
    elif bpm < 75:
        print(f"BPM {sublinhado}abaixo{texto_normal} da faixa adequada de {negrito}{faixa}{texto_normal}!")
    else:
        print(f"BPM {sublinhado}dentro{texto_normal} da faixa adequada de {negrito}{faixa}{texto_normal}!")

if idade >= 18 and idade <= 59:
    faixa = "70 a 80"

    if bpm > 80:
        print(f"BPM {sublinhado}acima{texto_normal} da faixa adequada de {negrito}{faixa}{texto_normal}!")
    elif bpm < 70:
        print(f"BPM {sublinhado}abaixo{texto_normal} da faixa adequada de {negrito}{faixa}{texto_normal}!")
    else:
        print(f"BPM {sublinhado}dentro{texto_normal} da faixa adequada de {negrito}{faixa}{texto_normal}!")

if idade >= 60:
    faixa = "50 a 60"

    if bpm > 60:
        print(f"BPM {sublinhado}acima{texto_normal} da faixa adequada de {negrito}{faixa}{texto_normal}!")
    elif bpm < 50:
        print(f"BPM {sublinhado}abaixo{texto_normal} da faixa adequada de {negrito}{faixa}{texto_normal}!")
    else:
        print(f"BPM {sublinhado}dentro{texto_normal} da faixa adequada de {negrito}{faixa}{texto_normal}!")
