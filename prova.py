nome = input("digite o nome do paciente: ")
idade = input("digite sua idade: ")
altura = float(input("digite sua altura(m): "))
peso = int(input("digite seu peso(kg): "))

imc = peso/(altura* altura)

if imc < 18.5:
    print(f"{nome} tem {imc}, e sua classificacao resultou em  Abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print(f"{nome} tem {imc} e  e sua classificacao resultou em  Peso normal")
elif 25.0 <= imc <= 29.9:
    print(f"{nome} tem {imc} e sua classificacao resultou em Sobrepeso")
elif 30.0 <= imc <= 34.9:
    print(f"{nome} tem {imc}  e sua classificacao resultou em Obesidade grau 1")
elif 35.0 <= imc <= 39.9:
    print(f"{nome} tem {imc}  e sua classificacao resultou em Obesidade grau 2")
else:
    print(f"{nome} tem {imc}  e sua classificacao resultou em obesidade grau 3")