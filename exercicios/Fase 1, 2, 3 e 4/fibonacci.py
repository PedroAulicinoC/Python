def eh_fibonacci(n):
    a, b = 1, 1
    while b < n:
        a, b = b, a+b
    return b == n or n == 1

numero = int(input("Digite um número inteiro: "))

if eh_fibonacci(numero):
    print("Ação bem-sucedida!")
else:
    print("A ação falhou...")
