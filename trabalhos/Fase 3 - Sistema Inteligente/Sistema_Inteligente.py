# 2. Organização dos dados #
colonia = {
    "energia": {
        "solar": {"geracao": 40},
        "eolica": {"geracao": 30},
        "consumo": 70,
        "reserva": 20
    },
    "clima": {
        "temperatura_externa": -20,
        "temperatura_interna": 22,
        "sol": True,
        "vento": 11
    },
    "sistemas": {
        "habitacao": {"ativo": True, "critico": True},
        "laboratorio": {"ativo": True, "critico": False},
        "logistica_medica": {"ativo": True, "critico": True},
        "agricultura": {"ativo": True, "critico": False},
        "reciclagem": {"ativo": True, "critico": False},
        "agua_oxigenio": {"ativo": True, "critico": True},
        "comunicacao": {"ativo": True, "critico": True},
        "transporte": {"ativo": True, "critico": False},
        "armazenamento_extra": {"ativo": False, "critico": False}
    }
}

# 3. Analise de energia e tomada de decisão#
def gerenciar_sistemas(energia, consumo, reserva, sistemas):
    if reserva < 10:
        return "ALERTA: Bateria reserva com pouca energia!"

    elif energia < 50 and consumo > energia:
        for nome, dados in sistemas.items():
            if not dados["critico"]:
                dados["ativo"] = False
        return "ALERTA: Modo de economia ativado, sistemas não críticos desligados!"

    elif energia > consumo:
        for nome, dados in sistemas.items():
            dados["ativo"] = True
        return "AVISO: Energia excedente detectada, armazenamento extra de energia ativado."

    else:
        for nome, dados in sistemas.items():
            if nome == "armazenamento_extra":
                dados["ativo"] = False
            else:
                dados["ativo"] = True
        return "SISTEMA ESTÁVEL"

# 4. Previsão de comportamento (Geração de Energia) #
def previsao_linear(x, dados_x, dados_y):
    # Número de pontos de dados:
    n = len(dados_x)

    # Calcula a média dos valores de entrada (x) e saída (y)
    media_x = sum(dados_x) / n
    media_y = sum(dados_y) / n

    # Calcula o numerador da fórmula da inclinação (a):
    numerador = sum((dados_x[i] - media_x) * (dados_y[i] - media_y) for i in range(n))

    # Calcula o denominador da fórmula da inclinação (a):
    denominador = sum((dados_x[i] - media_x) ** 2 for i in range(n))

    # Inclinação da reta (y cresce quando x aumenta):
    a = numerador / denominador

    # Intercepto da reta (valor de y quando x = 0):
    b = media_y - a * media_x

    # Retorna o valor previsto:
    return a * x + b


#### Demonstração ####

# Entradas #

# Dados atuais de energia:
energia_total = colonia["energia"]["solar"]["geracao"] + colonia["energia"]["eolica"]["geracao"]
consumo = colonia["energia"]["consumo"]
reserva = colonia["energia"]["reserva"]

# Previsões de geração de energia:
previsao_eolica = previsao_linear(colonia["clima"]["vento"], [8, 10, 12], [20, 25, 30])
previsao_solar = previsao_linear(11, [8, 10, 12, 14], [15, 30, 45, 40])
energia_prevista_total = previsao_eolica + previsao_solar

# Decisão lógica e analise (Gerenciamento dos sistemas):
mensagem = gerenciar_sistemas(energia_total, consumo, reserva, colonia["sistemas"])

# Saídas #

print("Energia atual:", energia_total)
print("Consumo atual:", consumo)
print("Reserva atual:", reserva)
print("Previsão eólica:", round(previsao_eolica, 2))
print("Previsão solar:", round(previsao_solar, 2))
print("Energia prevista total:", round(energia_prevista_total, 2))
print("Decisão:", mensagem)

print("\nEstado dos sistemas:")
for nome, dados in colonia["sistemas"].items():
    print(f"{nome} -> {'Ativo' if dados['ativo'] else 'Desligado'}")