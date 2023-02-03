import os
from double_bs_solution import bs_solution
from n2_solution import n2_solution
from two_pointers_solution import tp_solution

in_path = "test/in/"
out_path = "test/out/"
#sol_path = "test/sol/"

def checker(name, model):
    points = []
    n = -1
    out_min_sd, sol_min_sd = -1, -1
    with open(in_path+name+'.in', 'r') as in_file:
        n = int(in_file.readline())
        for _ in range(n):
            x, y = map(int, in_file.readline().split())
            points.append((x,y))
    sol_min_sd = model(n, points)
    with open(out_path+name+'.out', 'r') as out_file:
        out_min_sd = int(out_file.readline())
    #with open(sol_path+name+'.txt', 'r') as sol_file:
    #    sol_min_sd = int(sol_file.readline())
    if out_min_sd != sol_min_sd:
        print(f"Test <<{name}>> Fallo Respuesta esperada:{out_min_sd} se obtuvo: {sol_min_sd}")
        return
    print(f"Test <<{name}>> OK. Respuesta esperada:{out_min_sd} se obtuvo: {sol_min_sd}.") 
    return

def all_checked(model):
    ins = os.listdir(in_path)
    for in_t in ins:
        name, ext = os.path.splitext(in_t)
        if not ext.endswith(".in"):
            continue
        checker(name, model=model)

if __name__ == "__main__":
    model_opt = int(input("Seleccionarr el modelo a evaluar. two_pointers(1), double_bs(2), n^2(3) :" ))
    model = None
    if model_opt == 1:
        model = tp_solution
    elif model_opt ==2:
        model = bs_solution
    elif model_opt == 3:
        model =n2_solution
    else:
        print("Error en la seleccion del modelo")
    option = int(input("Seleccionar un solo caso(1) o correr el verificador para todos(2): "))
    if option == 1:
        name = input("Nombre del caso de prueba, (sin extension): ")
        checker(name, model=model)
    else:
        all_checked(model=model)