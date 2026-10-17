total_alimentos = int(input("Quantos alimentos você comeu hoje: "))
total_calorias = 0

for alimento_atual in range(1, total_alimentos + 1, 1):
    calorias = float(input(f"Quantas calorias tinha o alimento {alimento_atual}: "))
    total_calorias += calorias

print(f"No total, você comeu {total_calorias} calorias.")