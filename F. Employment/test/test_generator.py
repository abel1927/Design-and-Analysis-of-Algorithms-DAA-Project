from random import randint
from brute_force import brute_force

M = int(1e9)
N = 10

in_path = "test/in/"
out_path = "test/out/"

def save_in(in_path, gm, gn, gvacancies, gcandidates):
    with open(in_path, 'w') as file:
        file.write(f"{gm} {gn}\n")
        file.write(" ".join(map(str,gvacancies))+'\n')
        file.write(" ".join(map(str,gcandidates)))
    return

def save_out(out_path, min_d, r):
    with open(out_path, 'w') as file:
        file.write(f"{min_d}\n")
        file.write(" ".join(map(str,r)))
    return

def generate(name, m_up=M, m_down=1, n_up=N, n_down=1):
    print("Generando")
    gm = randint(m_down, m_up)
    n_up = min(n_up, N)
    gn = randint(n_down, n_up)
    gvacancies = [randint(1,gm) for _ in range(gn)]
    gcandidates = [randint(1,gm) for _ in range(gn)]

    min_d, r = brute_force(gm, gn, gvacancies, gcandidates)
    save_in(in_path+name+".in", gm, gn, gvacancies, gcandidates)
    save_out(out_path+name+".out", min_d, r)

    print("Caso generado.")

def generate_with_eq_limit(name, vac_equality_limit, can_equality_limit, m_up=M, m_down=1, n_up=N, n_down=1, ):
    vacancy_equality = {}
    candidate_equality = {}
    gm = randint(m_down, m_up)
    gn = randint(n_down, n_up)
    gvacancies = []
    total = 0
    while total < gn:
        v = randint(1,gm)
        if vacancy_equality.get(v) != None:
            vacancy_equality[v] = 1
        elif vacancy_equality[v] == vac_equality_limit:
            continue
        else:
            gvacancies.append(v)
            vacancy_equality[v] += 1
            total+=1
    total = 0
    gcandidates = []
    while total < gn:
        v = randint(1,gm)
        if candidate_equality.get(v) != None:
            candidate_equality[v] = 1
        elif candidate_equality[v] == can_equality_limit:
            continue
        else:
            gcandidates.append(v)
            candidate_equality[v] += 1
            total+=1
    min_d, r = brute_force(gm, gn, gvacancies, gcandidates)
    save_in(in_path+name+".in", gm, gn, gvacancies, gcandidates)
    save_out(out_path+name+".out", min_d, r)

    print("Caso generado.")

if __name__ == "__main__":
    name = input("Nombre para el test: ")
    type_ = input("Seleccione> Generador completamente aleatorio(1), Parametrizado(2)")
    if type_ == "1":
        generate(name)
    elif type_ == "2":
        m_up = int(input("Seleccione el numero de ciudades maximo(1-10^9): "))
        m_down = int(input("Seleccione el numero de ciudades minimo(1-10^9): "))
        n_up = int(input("Seleccione el numero de vacantes y candidatos maximo(1-10): "))
        n_down = int(input("Seleccione el numero de vacantes y candidatos minimo(1-10): "))
        ##more_cond = int(input("Agregar mas condiciones Maxima igualdad(1) No(0): "))
        #if more_cond == 1:
            #vac_equality_limit = int(input("Cantidad maxima de elementos iguales en las vacantes(1-n): "))
            #can_equality_limit = int(input("Cantidad maxima de elementos iguales en los candidatos(1-n): "))
            #generate_with_eq_limit(name, vac_equality_limit, can_equality_limit, m_up, m_down, n_up, n_down)
        generate(name, m_up, m_down, n_up, n_down)
    else:
        print("1 o 2")