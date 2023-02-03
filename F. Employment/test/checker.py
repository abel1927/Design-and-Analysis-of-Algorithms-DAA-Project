import os
from brute_force import calc_distance
from solution import solution

in_path = "test/in/"
out_path = "test/out/"

def checker(name):
    in_vacancies = []
    in_candidates = []
    in_m, in_n = -1, -1
    with open(in_path+name+'.in','r') as in_file:
        in_m, in_n = map(int, in_file.readline().split()) 
        in_vacancies = list(map(int, in_file.readline().split()))
        in_candidates = list(map(int, in_file.readline().split()))
    out_min_d, sol_min_d = -1, -1
    out_distr, sol_distr = [],[]
    with open(out_path+name+'.out', 'r') as out_file:
        out_min_d = int(out_file.readline())
        out_distr = list(map(int, out_file.readline().split()))
    sol_min_d, sol_distr = solution(in_m, in_n, in_vacancies, in_candidates)
    if out_min_d != sol_min_d:
        print(f"Test <<{name}>> Fallo Distancia M:{out_min_d} se obtuvo: {sol_min_d}")
        return
    if len(out_distr) != len(sol_distr):       
        print(f"Test <<{name}>> Fallo. La distribucion planteada no es realmente optima")
        return
    check = True
    for i in range(len(out_distr)):
        if out_distr[i] != sol_distr[i]:
            check=False
            break
    if check:
        print(f"Test <<{name}>> OK. Distancia M:{out_min_d} se obtuvo: {sol_min_d}. Distribucion comprobada") 
        return
    c_min_d = 0
    for i in range(len(sol_distr)):
        c_min_d+= calc_distance(in_m,in_candidates[sol_distr[i]-1]-1,in_vacancies[i]-1)
    if c_min_d == out_min_d:
        print(f"Test <<{name}>> OK. Distancia M:{out_min_d} se obtuvo: {sol_min_d}. Distribucion comprobada") 
        return
    else:
        print(f"Test <<{name}>> Fallo. La distribucion planteada no es realmente optima")
        return

def all_checked():
    ins = os.listdir(in_path)
    for in_f in ins:
        name, ext = os.path.splitext(in_f)
        if not ext.endswith("in"):
            continue
        checker(name)

if __name__ == "__main__":
    option = int(input("Seleccionar un solo caso(1) o correr el verificador para todos(2):"))
    if option == 1:
        name = input("Nombre del caso de prueba, (sin extension):")
        checker(name)
    else:
        all_checked()
        

