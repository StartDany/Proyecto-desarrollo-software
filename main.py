def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multi(a,b):
    return a * b

def dividir(a,b):
    if b==0:
        return print("No se puede dividir por 0")
    return a / b 

print("===============================")
print("    CALCULADORA EN PYTHON")
print("===============================")

num1=float(input("Digite el primer numero: "))
num2=float(input("Digite el segundo numero: "))

print("\nResultados:")

print("Suma:", sumar(num1, num2))
print("Resta:", restar(num1, num2))
print("Multiplicacion:", multi(num1, num2))
print("Division:", dividir(num1, num2))

print("\nProyecto desarrollo como actividad de Git y Github.")