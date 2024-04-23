CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome

nome_usuario = input("Digite seu nome: ")

if nome_usuario.isdigit():
    print("Você digitou seu nome errado: ")
    exit()
elif len(nome_usuario) == 0:
    print("Você nao digitou nada")
    exit()
elif nome_usuario.isspace(): 
    print("Você digitou só espaço!")
else: 
    print("Seja bem vinde!", nome_usuario)



# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:

    salario = float(input("Digite o seu salário: "))
    if salario < 0 :
        print("Digite um valor positivo: ")
except ValueError:
    print("Entrada inválida! Digite um numero válido")
    exit()





# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

try:
    bonus = float(input("Digite o valor do bônus recebido: "))
    if bonus < 0:
        print("Por favor, digite um valor positivo para o bônus.")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")
    exit()
    
# 4) Calcule o valor do bônus final

# 5) Imprima cálculo do KPI para o usuário

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?