# ===============================================
# ATIVIDADE PRÁTICA 02 - Exercícios em Python
# ===============================================

# 1 - Conversor de Moeda
print("=== 1 - Conversor de Moeda ===")
valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Em dólares: US$ {valor_dolar:.2f}")
print(f"Em euros: € {valor_euro:.2f}\n")


# 2 - Calculadora de Desconto
print("=== 2 - Calculadora de Desconto ===")
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}\n")


# 3 - Calculadora de Média Escolar
print("=== 3 - Calculadora de Média Escolar ===")
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média final: {media:.2f}\n")


# 4 - Calculadora de Consumo de Combustível
print("=== 4 - Calculadora de Consumo de Combustível ===")
distancia = 300
combustivel = 25

consumo_medio = distancia / combustivel

print(f"Distância percorrida: {distancia} km")
print(f"Combustível gasto: {combustivel} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l\n")


# 5 - Calculadora de Soma com Entrada do Usuário
print("=== 5 - Calculadora de Soma ===")
A = int(input("Digite o primeiro número (A): "))
B = int(input("Digite o segundo número (B): "))

X = A + B
print(f"X = {X}\n")


# 6 - Calculadora de Salário por Horas Trabalhadas
print("=== 6 - Calculadora de Salário ===")
numero_funcionario = int(input("Número do funcionário: "))
horas_trabalhadas = int(input("Horas trabalhadas: "))
valor_por_hora = float(input("Valor por hora: "))

salario = horas_trabalhadas * valor_por_hora

print(f"NÚMERO = {numero_funcionario}")
print(f"SALÁRIO = R$ {salario:.2f}")
