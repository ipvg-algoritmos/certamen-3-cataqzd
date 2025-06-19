#sistema_acceso

edad = int(input("ingrese su edad: "))

supervisor = input("¿es usted supervisor? (si/no): ")
tiene_autorización = input("¿tiene usted una autorización? (si/no): ")

supervisor = (supervisor == "si")
tiene_autorización = (supervisor == "si")

edad = (edad >= 18)
autorización = (supervisor or tiene_autorización)
acceso = (edad and tiene_autorización)

if acceso:
    print("acceso permitido")
else:
    print("no tiene acceso")
    