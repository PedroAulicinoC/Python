### Sistema Inteligente de Gerenciamento da Infraestrutura da Colônia - SIGIC ###
#################################################################################

from collections import deque
import heapq

# Estrutura dos módulos da colônia (Conexões em metros) #
#########################################################
modulos = {
    "Habitação": {
        "prioridade": 1, # ------------------------------------------------------> Nível de prioridade do módulo
        "consumo_energia": 60, # ------------------------------------------------> Consumo energético em kWh
        "capacidade_armazenamento": 200, # --------------------------------------> Capacidade de armazenamento em kWh
        "status": "Ativo", # ----------------------------------------------------> Estado atual do módulo
        "comunicacao": "Alta", # ------------------------------------------------> Nível de comunicação
        "conexoes": {"Energia": 10, "Agricultura": 15, "Logística e Médico": 10} # Conexões com outros módulos e distância em metros
    },
    "Energia": {
        "prioridade": 2,
        "consumo_energia": 90,
        "capacidade_armazenamento": 500,
        "status": "Ativo",
        "comunicacao": "Média",
        "conexoes": {"Habitação": 10, "Produção de Água e Oxigênio": 8, "Armazenamento e Manutenção": 12}
    },
    "Laboratório Científico": {
        "prioridade": 4,
        "consumo_energia": 50,
        "capacidade_armazenamento": 150,
        "status": "Ativo",
        "comunicacao": "Alta",
        "conexoes": {"Comunicação e Controle": 20}
    },
    "Logística e Médico": {
        "prioridade": 2,
        "consumo_energia": 70,
        "capacidade_armazenamento": 250,
        "status": "Em manutenção",
        "comunicacao": "Alta",
        "conexoes": {"Habitação": 10}
    },
    "Agricultura": {
        "prioridade": 3,
        "consumo_energia": 80,
        "capacidade_armazenamento": 300,
        "status": "Ativo",
        "comunicacao": "Média",
        "conexoes": {"Habitação": 15, "Reciclagem e Reuso": 7}
    },
    "Reciclagem e Reuso": {
        "prioridade": 3,
        "consumo_energia": 40,
        "capacidade_armazenamento": 180,
        "status": "Ativo",
        "comunicacao": "Baixa",
        "conexoes": {"Agricultura": 7}
    },
    "Produção de Água e Oxigênio": {
        "prioridade": 1,
        "consumo_energia": 100,
        "capacidade_armazenamento": 400,
        "status": "Ativo",
        "comunicacao": "Alta",
        "conexoes": {"Energia": 8}
    },
    "Comunicação e Controle": {
        "prioridade": 3,
        "consumo_energia": 30,
        "capacidade_armazenamento": 100,
        "status": "Em alerta",
        "comunicacao": "Muito Alta",
        "conexoes": {"Laboratório Científico": 20, "Transporte e Mobilidade": 25}
    },
    "Transporte e Mobilidade": {
        "prioridade": 5,
        "consumo_energia": 70,
        "capacidade_armazenamento": 220,
        "status": "Ativo",
        "comunicacao": "Média",
        "conexoes": {"Comunicação e Controle": 25, "Armazenamento e Manutenção": 18}
    },
    "Armazenamento e Manutenção": {
        "prioridade": 4,
        "consumo_energia": 60,
        "capacidade_armazenamento": 600,
        "status": "Em manutenção",
        "comunicacao": "Baixa",
        "conexoes": {"Energia": 12, "Transporte e Mobilidade": 18}
    }
}

# BFS - Busca em Largura #
##########################
def bfs(modulos, inicio):
    visitados = set() # ------------> Conjunto para marcar módulos já visitados
    fila = deque([inicio]) # -------> Fila para controlar a ordem de visita
    ordem = [] # -------------------> Lista para registrar a ordem de visita
    while fila:
        vertice = fila.popleft()    # Remove o primeiro da fila
        if vertice not in visitados:
            visitados.add(vertice)  # Marca como visitado
            ordem.append(vertice)   # Adiciona à ordem de visita
            for vizinho in modulos[vertice]["conexoes"]: # Percorre vizinhos
                if vizinho not in visitados:
                    fila.append(vizinho) # Adiciona vizinhos à fila
    return ordem

# DFS - Busca em Profundidade #
###############################
def dfs(modulos, inicio, visitados=None, ordem=None):
    if visitados is None:
        visitados = set() # -------> Conjunto de visitados
    if ordem is None:
        ordem = [] # --------------> Lista de ordem de visita
    visitados.add(inicio) # -------> Marca o módulo atual como visitado
    ordem.append(inicio) # --------> Adiciona à ordem de visita
    for vizinho in modulos[inicio]["conexoes"]: # Percorre vizinhos
        if vizinho not in visitados:
            dfs(modulos, vizinho, visitados, ordem) # Chama recursivamente
    return ordem

# Dijkstra - Caminho mínimo #
#############################
def dijkstra(modulos, inicio, destino):
    distancias = {vertice: float('inf') for vertice in modulos} # Inicializa distâncias como infinito
    distancias[inicio] = 0 # -----------------------------------> Distância inicial = 0
    anterior = {vertice: None for vertice in modulos} # --------> Guarda o caminho percorrido
    fila = [(0, inicio)] # -------------------------------------> Fila de prioridade (heapq)
    while fila:
        distancia_atual, vertice_atual = heapq.heappop(fila)    # Pega o vértice com menor distância
        if distancia_atual > distancias[vertice_atual]:
            continue
        for vizinho, peso in modulos[vertice_atual]["conexoes"].items():
            nova_distancia = distancia_atual + peso # ----------> Calcula nova distância
            if nova_distancia < distancias[vizinho]: # ---------> Se for menor, atualiza
                distancias[vizinho] = nova_distancia
                anterior[vizinho] = vertice_atual
                heapq.heappush(fila, (nova_distancia, vizinho)) # Adiciona vizinho na fila
    caminho = []
    vertice = destino
    while vertice is not None: # -------------------------------> Reconstrói o caminho final
        caminho.insert(0, vertice)
        vertice = anterior[vertice]
    return caminho, distancias[destino]

# Modelagem matemática - Crescimento do consumo energético #
############################################################
def consumo_energetico(energia_total, taxa_crescimento, tempo_meses):
    return energia_total * ((1 + taxa_crescimento) ** tempo_meses)
# Sendo:
# energia_total: a soma do consumo de energia de todos os módulos ativos
# taxa_crescimento: a taxa de crescimento em porcentagem
# tempo_meses: a quantidade de meses que queremos ver no futuro

# Menu do usuário #
###################
def menu():
    while True:
        print("\n=== SIGIC - Sistema Inteligente de Gerenciamento da Infraestrutura da Colônia ===")
        print("1 - Visualizar módulos da colônia")
        print("2 - Executar BFS")
        print("3 - Executar DFS")
        print("4 - Executar Dijkstra (caminho mínimo)")
        print("5 - Simulação de crescimento do consumo energético")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Mostra todos os módulos e seus atributos principais
            print("\n--- Módulos da Colônia ---")
            for nome, dados in modulos.items():
                print(
                    f"{nome} "
                    f"| Prioridade: {dados['prioridade']} "
                    f"| Consumo: {dados['consumo_energia']} kWh "
                    f"| Armazenamento: {dados['capacidade_armazenamento']} kWh "
                    f"| Status: {dados['status']} "
                    f"| Comunicação: {dados['comunicacao']} ")

        elif opcao == "2":
            # Executa BFS a partir de um módulo inicial
            inicio = input("Digite o módulo inicial para BFS: ")
            if inicio in modulos:
                print("Ordem de visita (BFS):", bfs(modulos, inicio))
            else:
                print("Módulo não encontrado.")

        elif opcao == "3":
            # Executa DFS a partir de um módulo inicial
            inicio = input("Digite o módulo inicial para DFS: ")
            if inicio in modulos:
                print("Ordem de visita (DFS):", dfs(modulos, inicio))
            else:
                print("Módulo não encontrado.")

        elif opcao == "4":
            # Executa Dijkstra para encontrar o caminho mínimo entre dois módulos
            inicio = input("Digite o módulo inicial: ")
            destino = input("Digite o módulo destino: ")
            if inicio in modulos and destino in modulos:
                caminho, distancia = dijkstra(modulos, inicio, destino)
                print(f"Caminho mais curto de '{inicio}' até '{destino}' é: {caminho} (distância: {distancia}m)")
            else:
                print("Um dos módulos não foi encontrado.")

        elif opcao == "5":
            # Simulação de crescimento do consumo energético
            # Soma o consumo inicial de todos os módulos ativos
            energia_modulos = sum(dados["consumo_energia"] for dados in modulos.values() if dados["status"] == "Ativo")

            # Usuário escolhe a taxa de crescimento em porcentagem
            taxa = float(input("Digite a taxa de crescimento (%): "))
            taxa_porcentagem = taxa / 100  # Converte para decimal

            # Usuário escolhe o número de meses para simulação
            meses = int(input("Digite o número de meses para simulação: "))

            print("\n--- Crescimento do Consumo Energético ---")
            for mes in range(1, meses + 1):
                print(f"Mês {mes}: {consumo_energetico(energia_modulos, taxa_porcentagem, mes):.2f} kWh")

        elif opcao == "6":
            # Encerra o sistema
            print("Encerrando o sistema SIGIC...")
            break

        else:
            # Caso o usuário digite uma opção inválida
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()