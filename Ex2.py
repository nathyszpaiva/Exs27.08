def calcReajuste(salario):
    if salario > 5000:
        return salario * 1.10  # Reajuste de 10%
    else:
        return salario * 1.15  # Reajuste de 15%
    
salario = float(input("Digite o salário atual: R$"))
novo_salario = calcReajuste(salario)
print(f"Novo salário após o reajuste: R${novo_salario:.2f}")