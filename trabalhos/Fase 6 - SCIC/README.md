# SCIC - Sistema de Comunicação Interplanetária da Colônia

## Visão Geral do Projeto
O SCIC é um protótipo computacional desenvolvido para monitorar, analisar e otimizar o fluxo de comunicação interplanetária e o desempenho operacional dos módulos da colônia Aurora Siger em Marte.  
O sistema realiza a leitura de telemetrias operacionais, avalia a precisão de latências previstes vs. observadas, aplica um modelo preditivo para estimar atrasos de rede, prioriza alertas de emergência, permite consultas otimizadas de módulos, analisa a eficiência elétrica dos transmissores e incorpora princípios de gestão inteligente e responsabilidade social e ambiental.

## Tecnologias e Dependências Utilizadas
- pandas
- numpy
- scikit-learn
- heapq

## Como Executar o Projeto
### Pré-requisitos
Tenha certeza que as bibliotecas necessárias foram instaladas:
```
pip install pandas numpy scikit-learn
```

### Executando o Sistema
1. Extraia o conteúdo do arquivo .zip para uma pasta de sua preferência.
2. Certifique-se de que o arquivo dados_aurora_siger.json e o script codigo_fonte.py estejam no mesmo diretório.
3. Execute o script principal via terminal:
```
python codigo_fonte.py
```

