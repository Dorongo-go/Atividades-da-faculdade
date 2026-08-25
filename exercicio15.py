#Custo final da compra
preco_uni = float(input("Digite o preço unitário do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))
frete = float(input("Digite o valor do frete: "))

custo_final = (preco_uni * quantidade) + frete
print(f"O custo final da compra é {custo_final}")