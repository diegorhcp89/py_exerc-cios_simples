"""
Calcular o Índice de massa corporal (IMC) com base no peso e altura fornecedios pelo usuário,
e classifica o resultado em categorias pré-definidas.
"""

def calcular_imc():
    print("Bem vindo a calculadora de IMC!")

    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a seua altura: "))

    # Calcular o IMC
    imc = peso / (altura ** 2)

    print(f"Seu IMC é {imc:.2f}")

    # Exibir a categoraia do usuário
    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif imc < 24.9:
        print("Classificação: Peso normal")
    elif imc < 29.9:
        print("Classificação: Sobrepeso")
    elif imc < 34.9:
        print("Classificação: Obesidade grau 1")
    elif imc < 93.95:
        print("Classificação: Obesidade grau 2")
    else:
        print("Obesidade Mórbida")

if __name__ == "__main__":
    calcular_imc()
