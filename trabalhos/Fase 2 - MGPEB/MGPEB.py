#### Módulo de Gerenciamento de Pouso e Estabilização de Base (MGPEB) ####

# Estruturas principais
fila_pouso = []       # Fila inicial (FIFO)
pousados = []         # Lista de módulos que pousaram com sucesso
alerta = []           # Lista de módulos em alerta (não pousaram)

# Função para cadastrar módulo
def cadastrar_modulo (nome, prioridade, massa, combustivel, sensores, ETA):
    return \
    {
        "nome": nome,
        "prioridade": prioridade,
        "massa": massa,
        "combustivel": combustivel,
        "sensores": sensores,
        "ETA": ETA
    }

# Cadastro dos módulos
modulos = \
[
    cadastrar_modulo("Transporte e Mobilidade", 5, 13000, 90, True, "16:30"),
    cadastrar_modulo("Energia", 2, 12000, 65, False, "14:30"),
    cadastrar_modulo("Habitação", 1, 18000, 70, True, "14:00"),
    cadastrar_modulo("Comunicação e Controle", 3, 8000, 85, False, "16:15"),
    cadastrar_modulo("Laboratório Científico", 4, 10500, 80, True, "15:00"),
    cadastrar_modulo("Produção de Água e Oxigênio", 1, 11000, 68, True, "16:00"),
    cadastrar_modulo("Agricultura", 3, 14000, 75, True, "15:30"),
    cadastrar_modulo("Armazenamento e Manutenção", 4, 10000, 80, False, "16:45"),
    cadastrar_modulo("Logística e Médico", 2, 15000, 60, False, "15:15"),
    cadastrar_modulo("Reciclagem e Reuso", 3, 9500, 70, True, "15:45")
]

# Inserindo todos os módulos na fila de pouso
for m in modulos:
    fila_pouso.append(m)

## Funções de Busca ##
def buscar_menor_combustivel(lista):
    return min(lista, key=lambda m: m["combustivel"]) # Achar o módulo com menor combustível

def buscar_maior_prioridade(lista):
    return min(lista, key=lambda m: m["prioridade"]) # Achar o módulo com maior prioridade

## Ordenação (por ETA) ##
def ordenar_por_eta(lista):
    return sorted(lista, key=lambda m: m["ETA"])

## Lógica de Autorização de Pouso ##
def autorizar_pouso(modulo, vento):
    if modulo["combustivel"] >= 70 and modulo["sensores"] and vento <= 60:
        pousados.append(modulo) # Se o módulo bater com as condições acima, ele entra na lista de pousados
        # Mostramos o resultado:
        print(f"POUSO AUTORIZADO: {modulo['nome']}")
    else:
        alerta.append(modulo) # Caso não, é adicionado na lista de alerta
        # Mostramos o resultado:
        print(f"ALERTA: Pouso negado para {modulo['nome']}")

#### Demonstração ####

# Primeiro, organizamos os módulos em ordem de chegada:
print("\nFila inicial em ordem de chegada:")
for m in ordenar_por_eta(list(modulos)):
    print(m["nome"], "-", m["ETA"])

# Depois, achamos o módulo com o menor nível de combustível:
print("\nMódulo com menor combustível:", buscar_menor_combustivel(modulos)["nome"])
# E o que tem maior prioridade:
print("Módulo de maior prioridade:", buscar_maior_prioridade(modulos)["nome"])

vento_atual = 55 # Aqui, colocamos um valor qualquer para o vento

print("\nProcessando fila de pouso...")
while fila_pouso:  # FIFO
    m = fila_pouso.pop(0)  # Remove o primeiro da fila
    autorizar_pouso(m, vento_atual) # Faz o check de autorização de pouso

# Mostramos os módulos que pousaram:
print("\nMódulos pousados:", [m["nome"] for m in pousados])
# E os que não pousaram:
print("Módulos em alerta:", [m["nome"] for m in alerta])
