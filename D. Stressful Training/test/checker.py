import os
from nk_solution import nk_solution
from n_plus_k_solution import n_plus_k_solution

in_path = "test/in/"
out_path = "test/out/"

def checker(name, model):
    n,k = -1,-1
    charges, discharges = [], []
    out_min_sd, sol_min_sd = -1, -1
    with open(in_path+name+'.in', 'r') as in_file:
        n,k = map(int,in_file.readline().split())
        charges = list(map(int, in_file.readline().split()))
        discharges = list(map(int, in_file.readline().split()))
    sol_min_sd = model(n, k, charges, discharges)
    with open(out_path+name+'.out', 'r') as out_file:
        out_min_sd = out_file.readline()
    if out_min_sd != sol_min_sd:
        print(f"Test <<{name}>> Fallo Respuesta esperada:{str(out_min_sd)} se obtuvo: {str(sol_min_sd)}")
        return
    print(f"Test <<{name}>> OK. Respuesta esperada:{str(out_min_sd)} se obtuvo: {str(sol_min_sd)}.") 
    return

def all_checked(model):
    ins = os.listdir(in_path)
    for in_t in ins:
        name, ext = os.path.splitext(in_t)
        if not ext.endswith(".in"):
            continue
        checker(name, model=model)

if __name__ == "__main__":
    model_opt = int(input("Seleccionarr el modelo a evaluar. nk(1), n+k(2):" ))
    model = None
    if model_opt == 1:
        model = nk_solution
    elif model_opt ==2:
        model = n_plus_k_solution
    else:
        print("Error en la seleccion del modelo")
    option = int(input("Seleccionar un solo caso(1) o correr el verificador para todos(2): "))
    if option == 1:
        name = input("Nombre del caso de prueba, (sin extension): ")
        checker(name, model=model)
    else:
        all_checked(model=model)