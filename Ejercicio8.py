nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
print("Nombre:", nombre)
print("Edad:", edad) 
Nota1 = float(input("Ingresa tu Nota 1: "))
print("Nota 1:", Nota1)
Nota2 = float(input("Ingresa tu Nota 2: "))
print("Nota 2:", Nota2)
Nota3 = float(input("Ingresa tu Nota 3: "))
print("Nota 3:", Nota3)
promedio = (Nota1 + Nota2 + Nota3) / 3
print("Promedio:", promedio)
if promedio >= 71:
    print("Aprobado")
else:
    print("No aprobado")
