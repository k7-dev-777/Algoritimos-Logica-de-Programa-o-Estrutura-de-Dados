idade = 15
resultado = ""

if idade < 18:
    resultado = "menor de idade"
elif idade >= 18 and idade <= 60:
    resultado = "maior de idade"
elif idade > 60:
    resultado = "idoso"

print(resultado)