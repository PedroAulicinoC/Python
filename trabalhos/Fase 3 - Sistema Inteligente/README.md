# Gestão Autônoma de Energia da Aurora Siger

Este projeto simula a gestão de energia da base Aurora Siger em Marte.
Devido à distância da Terra, a base precisa tomar decisões de forma autônoma, analisando geração,
consumo e reserva de energia, além de prever valores futuros.

### Como funciona

- Os dados da colônia são armazenados em um dicionário Python, chamado de `colonia`.

- A função `gerenciar_sistemas` decide automaticamente quais sistemas ficam
ativos ou desligados, com base na energia disponível e na reserva.

- A função `previsao_linear` aplica regressão linear simples para
prever a geração futura de energia (solar e eólica).

- O programa diz a situação atual da colônia e o estado dos sistemas.

## Exemplo de execução

### Dados de entrada:

- colonia["energia"]["solar"]["geracao"] = 40
- colonia["energia"]["eolica"]["geracao"] = 30
- colonia["energia"]["consumo"] = 70
- colonia["energia"]["reserva"] = 20
- colonia["clima"]["vento"] = 11

### Saída esperada:

- Energia atual: 70
- Consumo atual: 70
- Reserva atual: 20
- Previsão eólica: 27.5
- Previsão solar: 37.5
- Energia prevista total: 65.0
- Decisão: SISTEMA ESTÁVEL

Estado dos sistemas:
- habitacao -> Ativo
- laboratorio -> Ativo
- logistica_medica -> Ativo
- agricultura -> Ativo
- reciclagem -> Ativo
- agua_oxigenio -> Ativo
- comunicacao -> Ativo
- transporte -> Ativo
- armazenamento_extra -> Desligado
