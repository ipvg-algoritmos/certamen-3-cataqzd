temperaturas = [1]
for i in range(5):
    temp = int(input("ingrese una temperatura"))
    temperaturas.append(temp)

    promedio = sum(temperaturas)/len(temperaturas)
    t_max = max(temperaturas)

check = True
for t in temperaturas:
    if t < 15 or t > 30:
        check = False
        break
    if check:
        print("todas las temperaturas estan dentro del rango")
    else:
        print("hay temperaturas fueras del rango")

