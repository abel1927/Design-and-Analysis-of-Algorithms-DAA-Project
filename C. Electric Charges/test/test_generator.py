from random import randint
from brute_force import brute_force

M = int(1e8)
N = 22

in_path = "test/in/"
out_path = "test/out/"

def save_in(in_path, gn, points):
    with open(in_path, 'w') as file:
        file.write(f"{gn}\n")
        for i in range(gn):
            file.write(" ".join(map(str,points[i])))
            if i != gn-1:
                file.write("\n")
    return

def save_out(out_path, min_sd):
    with open(out_path, 'w') as file:
        file.write(f"{min_sd}")
    return

def generate(name, n_max=N, n_min=1, x_max=M, x_min=1, y_max=M, y_min=1, x_signed = 10, y_signed=10):
    gn = randint(n_min, n_max)
    points = []
    checked_points = set()
    total = 0
    while total < gn:
        x_sig = 1 if x_signed > 10 else -1 if x_signed < 0 else -1 if randint(1,x_signed)%2 == 0 else 1
        y_sig = 1 if y_signed > 10 else -1 if y_signed < 0 else -1 if randint(1,y_signed)%2 == 0 else 1
        x =x_sig*randint(x_min, x_max)
        y = y_sig*randint(y_min, y_max)
        p = (x,y)
        if p in checked_points:
            continue
        checked_points.add(p)
        points.append(p)
        total+=1

    min_sd = brute_force(gn, points)
    save_in(in_path+name+".in", gn, points)
    save_out(out_path+name+".out", min_sd)

    print("Caso generado.")


if __name__ == "__main__":
    name = input("Nombre para el test: ")
    type_ = input("Seleccione> Generador completamente aleatorio(1), Parametrizado(2): ")
    if type_ == "1":
        generate(name)
    elif type_ == "2":
        n_max = int(input("Seleccione el numero de puntos maximo(1-22): "))
        n_min = int(input("Seleccione el numero de puntos minimo(1-22): "))
        x_max = int(input("Seleccione el maximo valor absoluto para las x(1-10^8): "))
        x_min = int(input("Seleccione el minimo valor absoluto para las x(1-10^8): "))
        y_max = int(input("Seleccione el maximo valor absoluto para las y(1-10^8): "))
        y_min = int(input("Seleccione el minimo valor absoluto para las y(1-10^8): "))
        more_cond = int(input("Agregar mas condiciones de Signos(1) No(0): "))
        if more_cond == 1:
            x_signed = int(input("Solo x + o -? +(1) -(2) ambos(3): "))
            if x_signed == 3:
                x_signed = 10
            elif x_signed == 2:
                x_signed -= 10
            elif x_signed == 1:
                x_signed += 10 
            y_signed = int(input("Solo y + o -? +(1) -(2) ambos(3): "))
            if y_signed == 3:
                y_signed = 10
            elif y_signed == 2:
                y_signed -= 10
            elif y_signed == 1:
                y_signed += 10 
            generate(name,  n_max, n_min, x_max, x_min, y_max, y_min, x_signed, y_signed)
        else:
            generate(name,  n_max, n_min, x_max, x_min, y_max, y_min)
    else:
        print("1 o 2")