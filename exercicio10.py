#Salario com comissão
salario = float(input("Digite o valor do salário: "))
total_vendas = float(input("Digite o valor total de vendas: "))

comissao = total_vendas * 0.04

print(f"O valor do salário é {salario}, com comissão de 5% sobre as vendas o valor final é {salario + comissao}")