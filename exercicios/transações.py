total_transacoes = int(input("Quantas transações financeiras você realizou: "))
total_gastos = 0

for transacao_atual in range(1, total_transacoes + 1, 1):
    gasto = float(input(f"Qual foi o valor da {transacao_atual}ª transação: R$"))
    total_gastos += gasto

print(f"Seu total de gastos foi R${total_gastos}.")
media_gastos = total_gastos / total_transacoes
print(f"Você gastou em média R${media_gastos}.")