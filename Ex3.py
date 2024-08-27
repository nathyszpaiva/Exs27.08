def calcAT(base, altura):
   
    area = (base * altura) / 2
    return area

base = float(input("Digite o comprimento da base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

area = calcAT(base, altura)
print(f"A área do triângulo é: {area:.2f}")