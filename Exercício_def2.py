def soma_imposto(imposto, custo):
    if imposto < 0 or custo < 0:
        raise ValueError("O imposto e o custo devem ser valores não negativos.")
    
    total = custo + (custo * (imposto / 100))
    return total

calculo_imposto = float(input("Digite a taxa de imposto (em %): "))
custo_item = float(input("Digite o custo do item: "))

print(f"O custo total do item após a aplicação do imposto é: {soma_imposto(calculo_imposto, custo_item):.2f}")