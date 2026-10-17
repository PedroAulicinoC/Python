import json
from datetime import datetime

# Formatação de texto:
negrito = "\033[1m"
texto_normal = "\033[0m"

# Arquivos:
arquivo_modulos = "dados_colonia.json"
arquivo_alertas = "registros_colonia.txt"
arquivo_interacoes = "interacoes_colonia.json"

# Dicionario:
modulos_dicionario = {
    "Habitação": {
        "prioridade": 1,
        "consumo_energia": 60,
        "capacidade_armazenamento": 200,
        "status": "Ativo"
    },
    "Energia": {
        "prioridade": 2,
        "consumo_energia": 90,
        "capacidade_armazenamento": 500,
        "status": "Ativo"
    },
    "Laboratório Científico": {
        "prioridade": 4,
        "consumo_energia": 50,
        "capacidade_armazenamento": 150,
        "status": "Ativo"
    },
    "Logística e Médico": {
        "prioridade": 2,
        "consumo_energia": 70,
        "capacidade_armazenamento": 250,
        "status": "Em manutenção"
    },
    "Agricultura": {
        "prioridade": 3,
        "consumo_energia": 80,
        "capacidade_armazenamento": 300,
        "status": "Ativo"
    },
    "Reciclagem e Reuso": {
        "prioridade": 3,
        "consumo_energia": 40,
        "capacidade_armazenamento": 180,
        "status": "Ativo"
    },
    "Produção de Água e Oxigênio": {
        "prioridade": 1,
        "consumo_energia": 100,
        "capacidade_armazenamento": 400,
        "status": "Ativo"
    },
    "Comunicação e Controle": {
        "prioridade": 3,
        "consumo_energia": 30,
        "capacidade_armazenamento": 100,
        "status": "Em alerta"
    },
    "Transporte e Mobilidade": {
        "prioridade": 5,
        "consumo_energia": 70,
        "capacidade_armazenamento": 220,
        "status": "Ativo"
    },
    "Armazenamento e Manutenção": {
        "prioridade": 4,
        "consumo_energia": 60,
        "capacidade_armazenamento": 600,
        "status": "Em manutenção"
    }
}

#####################################################
# Funções para o Usuário manipular os arquivos TXT #
#####################################################

# Função para o Usuário gerar alertas automáticos:
def gerar_alertas_automaticos():
    modulos = ler_json()
    for nome, dados in modulos.items():
        A = dados["status"] == "Em alerta"
        B = dados["prioridade"] <= 3
        C = dados["status"] == "Em manutenção"

        if B and (A or C):
            mensagem = f"Módulo {nome} em estado crítico (status={dados['status']}, prioridade={dados['prioridade']})."
            gravar_alerta(mensagem, nome, dados["prioridade"])
    print("Alertas automáticos gerados com base em status e prioridade.")

# Visualização dos alertas para o Usuário:
def visualizar_alertas():
    try:
        with open(arquivo_alertas, "r", encoding="utf-8") as file:
            print("\n=== Alertas Operacionais ===")
            print(file.read())
    except FileNotFoundError:
        print("Nenhum alerta registrado ainda.")

# Gravar alerta em arquivo texto:
def gravar_alerta(mensagem, modulo, prioridade):
    with open(arquivo_alertas, "a", encoding="utf-8") as file:
        registro = f"{datetime.now()} | Módulo: {modulo} | Prioridade: {prioridade} | Mensagem: {mensagem}\n"
        file.write(registro)
    print("Alerta registrado com sucesso!")

#####################################################
# Funções para o Usuário manipular os arquivos JSON #
#####################################################

# Visualização para o Usuário:
def visualizar_modulos():
    print("\n=== Módulos da base Aurora Siger ===")
    with open(arquivo_modulos, "r", encoding="utf-8") as file:
        modulos = json.load(file)
    print(json.dumps(modulos, indent=4, ensure_ascii=False))

# Adição de novos modulos pelo Usuário:
def adicionar_modulos():
    modulo = ler_json()
    print("\n=== Registro de um novo Módulo ===")
    nome = input("Digite o nome do modulo: ")
    if nome in modulo:
        print("Esse módulo já existe!")
        return
    prioridade = int(input("Digite a prioridade do módulo (1-5): "))
    consumo = int(input("Digite o consumo do módulo (kWh): "))
    capacidade = int(input("Digite a capacidade do módulo (kWh): "))
    status = input("Digite o status do modulo (Ativo, Em manutenção, Em alerta): ")

    modulo[nome] = {
        "prioridade": prioridade,
        "consumo_energia": consumo,
        "capacidade_armazenamento": capacidade,
        "status": status
    }

    gravar_json(modulo)
    print("Adicionado com sucesso!")

# Para o Usuário retornar os valores padrões do arquivo JSON:
def regravar_json():
    print("\nArquivo restaurado para seus valores padrões!")
    modulos_json = json.dumps(modulos_dicionario, indent=4, ensure_ascii=False)
    with open(arquivo_modulos, "w", encoding="utf-8") as file:
        file.write(modulos_json)

# Leitura do arquivo JSON:
def ler_json():
    with open(arquivo_modulos, "r", encoding="utf-8") as file:
        return json.load(file)

# Gravação do arquivo JSON:
def gravar_json(dados):
    with open(arquivo_modulos, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)

###################################
# Funções de simulação de prompts #
###################################

# Zero-Shot - Classificação de prioridade de alerta:
def zero_shot_prioridade(alerta, modulo):
    resposta = "Prioridade: Alta" if modulo["prioridade"] == 1 else "Prioridade: Média"
    gravar_interacao(alerta, resposta)

# Few-Shot - Sugestão de ação corretiva:
def few_shot_acao(alerta, modulo):
    exemplos = {
        "Energia": "Reduzir consumo e redistribuir carga.",
        "Agricultura": "Ativar irrigação manual temporária.",
        "Logística e Médico": "Revisar estoque e acionar suprimentos emergenciais."
    }
    resposta = exemplos.get(modulo["nome"], "Acionar equipe técnica para diagnóstico.")
    gravar_interacao(alerta, resposta)

# Saída Estruturada - Resposta organizada em JSON:
def saida_estruturada(alerta, modulo):
    resposta_json = {
        "modulo": modulo["nome"],
        "status": modulo["status"],
        "causa": alerta,
        "acao_sugerida": "Verificar sistema e aplicar manutenção preventiva.",
        "prioridade": modulo["prioridade"],
        "data": str(datetime.now())
    }
    gravar_interacao(alerta, json.dumps(resposta_json, indent=4, ensure_ascii=False))

# Gravar interação no arquivo JSON:
def gravar_interacao(pergunta, resposta):
    try:
        with open(arquivo_interacoes, "r", encoding="utf-8") as file:
            interacoes = json.load(file)
    except FileNotFoundError:
        interacoes = []

    interacoes.append({
        "data": str(datetime.now()),
        "pergunta": pergunta,
        "resposta": resposta
    })

    with open(arquivo_interacoes, "w", encoding="utf-8") as file:
        json.dump(interacoes, file, indent=4, ensure_ascii=False)

    print("Interação registrada com sucesso!")

# Visualizar interações do arquivo JSON:
def visualizar_interacoes():
    try:
        with open(arquivo_interacoes, "r", encoding="utf-8") as file:
            interacoes = json.load(file)
            print("\n=== Histórico de Interações ===")
            for i in interacoes:
                print(f"\n{i['data']} | Pergunta: {i['pergunta']} | Resposta: {i['resposta']}")
    except FileNotFoundError:
        print("Nenhuma interação registrada ainda.")

###################
# Menu do usuário #
###################

def menu():
    while True:
        print(f"\n{negrito}=== NCAS - Núcleo Cognitivo da Aurora Siger ==={texto_normal}")
        # Manipulação do arquivo JSON
        print("1 - Visualizar módulos da colônia")
        print("2 - Adicionar módulo à colônia")
        print("3 - Restaurar dados da colônia")

        # Alertas (Regras lógicas)
        print("4 - Gerar alertas automáticos")
        print("5 - Visualizar alertas")

        # Simulação da IA
        print("6 - Simular Zero-Shot (Classificação de prioridade)")
        print("7 - Simular Few-Shot (Sugestão de ação corretiva)")
        print("8 - Simular Saída Estruturada (JSON)")

        # Interações
        print("9 - Visualizar interações")

        opcao = input(f"\n{negrito}Escolha uma opção: {texto_normal}")

        if opcao == "1":
            visualizar_modulos()

        elif opcao == "2":
            adicionar_modulos()

        elif opcao == "3":
            regravar_json()

        elif opcao == "4":
            gerar_alertas_automaticos()

        elif opcao == "5":
            visualizar_alertas()

        elif opcao == "6":
            print("\n === Simulação de Zero-Shot ===")
            alerta = "Módulo Produção de Água e Oxigênio em alerta por consumo elevado."
            print(f"'{alerta}'")
            modulo = {"nome": "Produção de Água e Oxigênio", "prioridade": 1, "status": "Em alerta"}
            zero_shot_prioridade(alerta, modulo)

        elif opcao == "7":
            print("\n === Simulação de Few-Shot ===")
            alerta = "Módulo Logística e Médico em manutenção por falha no sistema de suprimentos."
            print(f"'{alerta}'")
            modulo = {"nome": "Logística e Médico", "prioridade": 2, "status": "Em manutenção"}
            few_shot_acao(alerta, modulo)

        elif opcao == "8":
            print("\n === Simulação de Saída Estruturada ===")
            alerta = "Módulo Comunicação e Controle em alerta por falha intermitente no sistema de transmissão."
            print(f"'{alerta}'")
            modulo = {"nome": "Comunicação e Controle", "prioridade": 2, "status": "Em alerta"}
            saida_estruturada(alerta, modulo)

        elif opcao == "9":
            visualizar_interacoes()

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()