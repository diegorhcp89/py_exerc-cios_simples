from datetime import datetime

ano_atual = datetime.now().year

ano_nascimento = int(input("Em que ano você nasceu?"))

idade = ano_atual - ano_nascimento

print("Você tem", idade, "anos")
