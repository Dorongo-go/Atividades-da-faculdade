def validação_tamanho(nome):
    if len(nome) <= 100:
        return True
    else:
        return False

C_de_tamanho = input("Digite um algo: ")

if validação_tamanho(C_de_tamanho):
    print(f"O tamanho do nome é mínimo, possuindo-se {len(C_de_tamanho)} caracteres.")

else:
    print(f"O tamanho do nome é máximo, possuindo-se {len(C_de_tamanho)} caracteres.")
