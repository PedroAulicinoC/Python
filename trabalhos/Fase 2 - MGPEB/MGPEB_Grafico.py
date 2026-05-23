import numpy as np
import matplotlib.pyplot as plt

# Horários simulados (em horas):
t = np.linspace(14, 20, 100)

# Modelo trigonométrico para os ventos:
A = 40   # amplitude da variação
B = 0.5  # frequência
D = 30   # valor médio
t0 = 14  # deslocamento inicial

velocidade = D + A * np.sin(B * (t - t0))

# Plotando o gráfico:
plt.plot(t, velocidade, label="Velocidade dos ventos (km/h)")
plt.axhline(60, color='r', linestyle='--', label="Limite de segurança")
plt.xlabel("Hora do dia")
plt.ylabel("Velocidade (km/h)")
plt.title("Previsão trigonométrica da velocidade dos ventos em Marte")
plt.legend()
plt.show()
