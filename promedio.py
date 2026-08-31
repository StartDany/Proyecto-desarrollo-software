nota1 = float(input("Digite la nota 1: "))

while nota1 < 0:
    print("La nota no puede ser inferior a 0.")
    nota1 = float(input("Digite la nota 1: "))


nota2 = float(input("Digite la nota 2: "))

while nota2 < 0:
    print("La nota no puede ser inferior a 0.")
    nota2 = float(input("Digite la nota 2: "))


nota3 = float(input("Digite la nota 3: "))

while nota3 < 0:
    print("La nota no puede ser inferior a 0.")
    nota3 = float(input("Digite la nota 3: "))


promedio = (nota1 + nota2 + nota3) / 3

print("Promedio:", promedio)

if promedio >= 3:
    print("Aprobado")
else:
    print("No aprobado")