# Formatação de texto:
negrito = "\033[1m"
texto_normal = "\033[0m"

import json
import heapq
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

###################################################
#                      1.1                        #
###################################################
# Carregamento dos dados simulados da colônia Aurora Siger
# Arquivos:
modulos_json = "dados_aurora_siger.json"

# Abrir o arquivo e carregar o conteúdo JSON:
with open(modulos_json, "r", encoding="utf-8") as f:
    dados = json.load(f)

###################################################
#                      1.2                        #
###################################################
# Organização dos dados em um DataFrame para análise:
df = pd.DataFrame(dados)

# Cálculo do Erro Absoluto:
df["erro_absoluto_ms"] = (df["latencia_observada_ms"] - df["latencia_prevista_ms"]).abs()
# Cálculo do Erro Relativo:
df["erro_relativo"] = df["erro_absoluto_ms"] / df["latencia_observada_ms"]
# Erro Relativo em porcentagem:
df["erro_relativo_pct"] = (df["erro_relativo"] * 100).round(2).astype(str) + "%"

# Formatação da tabela:
colunas_exibicao = [
    "nome_modulo",
    "latencia_observada_ms",
    "latencia_prevista_ms",
    "ruido_ms",
    "tamanho_dados_kb",
    "erro_absoluto_ms",
    "erro_relativo_pct",
    "status_operacional",
]

###################################################
#                      1.3                        #
###################################################
# Construção de um modelo de previsão de latência:
X = df[["latencia_prevista_ms", "ruido_ms", "tamanho_dados_kb", "potencia_watts"]]
y = df["latencia_observada_ms"]

# Divisão dos dados em treino (80%) e teste (20%):
x_train, x_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Treinamento do modelo de Regressão Linear:
modelo = LinearRegression()
modelo.fit(x_train, y_train)

# Previsão nos dados de teste:
y_pred = modelo.predict(x_test)

# Previsão no dataset completo para exibição no painel/relatório:
df["latencia_prevista_modelo"] = modelo.predict(X).round(2)

# Cálculo das métricas de avaliação:
mae = mean_absolute_error(y_test, y_pred)   # Erro absoluto médio.
mse = mean_squared_error(y_test, y_pred)    # Erro quadrático médio.
rmse = np.sqrt(mse) # ----------------------> Raiz do erro quadrático médio.
r2 = r2_score(y_test, y_pred) #-------------> Coeficiente de determinação.

# Cálculo da Baseline:
y_pred_baseline = [y_train.mean()] * len(y_test)
mae_baseline = mean_absolute_error(y_test, y_pred_baseline)

###################################################
#                      1.4                        #
###################################################
# Priorização de alertas usando Heap:
def lista_prioridade():
    fila_prioridade = []

    # Inserindo cada alerta na heap com base na prioridade:
    for _, alerta in df.iterrows():
        item_heap = (
            alerta["alerta_nivel_prioridade"],  # Prioridade.
            alerta["id_registro"],              # ID.
            alerta["mensagem_alerta"]           # Mensagem.
        )
        heapq.heappush(fila_prioridade, item_heap)
        print(f"Alerta registrado: Módulo {alerta['nome_modulo']} (Prioridade {alerta['alerta_nivel_prioridade']})")

    print(f"\nTotal de alertas organizados na Heap: {len(fila_prioridade)} registros.")

    # Processando os alertas em ordem de prioridade:
    while fila_prioridade:
        prioridade, id_alerta, mensagem = heapq.heappop(fila_prioridade)
        print(f"\nNível de Urgência: {prioridade}")
        print(f" • ID do Alerta : #{id_alerta}")
        print(f" • Mensagem : {mensagem}")

###################################################
#                      1.5                        #
###################################################

# Estrutura Trie para busca eficiente por prefixo:
class NoTrie:
    def __init__(self):
        self.filhos = {} # -------> Dicionário de filhos.
        self.fim_de_chave = False # Marca se é fim de uma palavra.
        self.dados_registro = None

class TrieSCIC:
    def __init__(self):
        self.raiz = NoTrie()

    def inserir(self, chave: str, dados: dict = None):
        # Insere uma chave (nome do módulo) na Trie:
        no_atual = self.raiz
        chave_norm = chave.lower()

        for caractere in chave_norm:
            if caractere not in no_atual.filhos:
                no_atual.filhos[caractere] = NoTrie()
            no_atual = no_atual.filhos[caractere]
        no_atual.fim_de_chave = True
        no_atual.dados_registro = dados

    def buscar_por_prefixo(self, prefixo: str) -> list:
        # Busca registros que começam com o prefixo determinado:
        no_atual = self.raiz
        prefixo_norm = prefixo.lower()

        for caractere in prefixo_norm:
            if caractere not in no_atual.filhos:
                return []
            no_atual = no_atual.filhos[caractere]

        resultados = []
        self._coletar_registros(no_atual, resultados)
        return resultados

    def _coletar_registros(self, no_atual: NoTrie, resultados: list):
        # Coleta todos os registros a partir de um nó:
        if no_atual.fim_de_chave:
            resultados.append(no_atual.dados_registro)

        for filho in no_atual.filhos.values():
            self._coletar_registros(filho, resultados)

# Construindo a Trie com os módulos da colônia:
trie_colonia = TrieSCIC()
for _, registro in df.iterrows():
    trie_colonia.inserir(registro["nome_modulo"], registro.to_dict())

def pesquisar_modulo():
    busca_por_trie = input("Pesquise o nome do módulo: ")
    resultados_pesquisa = trie_colonia.buscar_por_prefixo(busca_por_trie)
    for res in resultados_pesquisa:
        print(f" • {res['nome_modulo']} | Código: {res['codigo_sensor']} | Tipo: {res['tipo_modulo']}")

###################################################
#                      1.6                        #
###################################################

def conversao_base():
    for _, registro in df.iterrows():
        # Conversão do código do sensor para diferentes bases:
        codigo_hex = registro["codigo_sensor"]
        codigo_int = int(codigo_hex, 16)
        print(f"\nMódulo: {registro['nome_modulo']}")
        print(f" • Código do sensor (hex): {codigo_hex}")
        print(f" • Código em decimal: {codigo_int}")
        print(f" • Código em binário: {bin(codigo_int)}")

def analise_eletricidade():
    for _, registro in df.iterrows():
        # Cálculo da potência aproximada (Lei de Ohm: P = V * I):
        potencia_calc = registro["tensao_volts"] * registro["corrente_amperes"]

        print(f"\nMódulo: {registro['nome_modulo']}")
        print(f" • Tensão: {registro['tensao_volts']} V")
        print(f" • Corrente: {registro['corrente_amperes']} A")
        print(f" • Potência calculada: {potencia_calc:.2f} W")
        print(f" • Potência registrada: {registro['potencia_watts']} W")

###################################################
#                      User Menu                  #
###################################################

def menu():
    while True:
        print(f"\n{negrito}=== SCIC - Sistema de Comunicação Interplanetária da Colônia ==={texto_normal}")
        # Cálculos de latência
        print("1 - Calcular erro absoluto e relativo da latência dos módulos")
        print("2 - Previsão da latência dos módulos")

        # Heap e Trie
        print("3 - Visualizar lista de prioridade")
        print("4 - Pesquisar módulos")

        # Conversões e Análise de Eletricidade
        print("5 - Converter a base dos códigos dos sensores")
        print("6 - Analise de eletricidade dos módulos")

        opcao = input(f"\n{negrito}Escolha uma opção: {texto_normal}")

        if opcao == "1":
            print("\n--- [SCIC] Análise de Latência dos Módulos ---")
            print(df[colunas_exibicao].to_string(index=False))

        elif opcao == "2":
            print("\n--- [SCIC] Avaliação de Performance do Modelo ---")
            print(f"MAE  : {mae:.2f} ms (Baseline Média: {mae_baseline:.2f} ms)")
            print(f"MSE  : {mse:.2f}")
            print(f"RMSE : {rmse:.2f} ms")
            print(f"R²   : {r2:.4f}")

            print("\n--- Comparação de Previsões no Dataset Completo ---")
            print(df[["nome_modulo", "latencia_observada_ms", "latencia_prevista_modelo"]].to_string(index=False))

        elif opcao == "3":
            print("\n--- [SCIC] Cadastrando Alertas na Fila de Prioridade ---")
            lista_prioridade()

        elif opcao == "4":
            print("\n--- [SCIC] Pesquisa de Módulos na Base de Dados ---")
            pesquisar_modulo()

        elif opcao == "5":
            print("\n--- [SCIC] Conversão de Bases Númericas dos Sensores ---")
            conversao_base()

        elif opcao == "6":
            print("\n--- [SCIC] Análise de Dispositivos e Eletricidade ---")
            analise_eletricidade()

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()