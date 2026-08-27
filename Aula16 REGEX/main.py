import re
codigo = input("Digite um código: ")
if re.fullmatch(r"\d{4}", codigo):
    print("Código válido! ")

else:
    print("Código inválido! ")