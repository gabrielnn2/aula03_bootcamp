CONSTANTE_BONUS = 1000

nome_valido = False
salario_valido = False
bonus_valido = False

# 1. Solicita ao usuário que digite seu nome
while nome_valido == False:
    nome = input("Digite seu nome: ")
    #nome = "gabriel"
    if any(char.isdigit() for char in nome):
        print("Insira um nome válido")
    elif len(nome.replace(' ','')) == 0:
        print("Nome em branco")
    else:
        print("Nome válido.")
        nome_valido = True

# 2. Solicita ao usuário que digite o valor do seu salário
while salario_valido is not True:
    try:
        salario = float(input("Digite seu salário: "))
        #salario = "0"
        if salario <= 0:
            print("Digite um salário maior que zero")
        else:
            print("Salário válido")
            salario_valido = True
    except ValueError:
        print("Digite um número válido")

# 3. Solicita ao usuário que digite o valor do bônus recebido
while bonus_valido is not True:
    try:
        bonus = float(input("Digite o bônus: "))
        if bonus <= 1:
            print("Digite um bônus maior que 1")
        else:
            print("Bonus válido")
            bonus_valido = True
    except ValueError:
        print("Digite um número válido")

# 4. Calcule o bônus final
kpi = CONSTANTE_BONUS + salario * bonus
print(f"Sua KPI é {kpi:.2f}")
