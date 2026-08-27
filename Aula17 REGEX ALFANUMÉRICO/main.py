import re
codigo = input("Digite sua senha: (5 caractéres)")
while not re.fullmatch(r"[a-z0-9]{5}", codigo):
    print("Senha errada, tente novamente.")
    codigo = input("Digite sua senha: ")
 
print("Senha aceita! ")   