from random import randint
from brute_force import brute_force

n_low, n_up, k_low, k_up = 1,7,1,9
a_low, a_up, b_low, b_up= 1,100,1,100

in_path = "test/in/"
out_path = "test/out/"

def save_in(in_path, gn,gk,charges,discharges):
    with open(in_path, 'w') as file:
        file.write(f"{gn} {gk}\n")
        file.write(" ".join(map(str,charges)))
        file.write("\n")
        file.write(" ".join(map(str,discharges)))
    return

def save_out(out_path, out):
    with open(out_path, 'w') as file:
        file.write(f"{out}")
    return

def generate(name):
    gn = randint(n_low, n_up)
    gk = randint(k_low, k_up)
    charges  = [randint(a_low, a_up) for _ in range(gn)]
    discharges = [randint(b_low, b_up) for _ in range(gn)]

    out = brute_force(gn,gk,charges,discharges)
    save_in(in_path+name+".in", gn,gk,charges, discharges)
    save_out(out_path+name+".out", out)

    print("Caso generado.")

if __name__ == "__main__":
    name = input("Nombre para el test: ")
    model = int(input("Seleccione> Algoritmo: FB(1), Prune FB(2): "))
    type_ = input("Seleccione> Generador completamente aleatorio(1), Parametrizado(2): ")
    if type_ == "1":
        generate(name)
    elif type_ == "2":
        n_low, n_up, k_low, k_up = 1,50,1,40
        a_low, a_up, b_low, b_up= 1,100,1,100
        n_low, n_up = map(int, input("Numero de equipos(rango-> min:1 max:7):").split()) 
        k_low, k_up = map(int, input("Numero de etapas(k)(rango-> min:1 max:9):").split()) 
        a_low, a_up = map(int, input("Valores de carga inicial ai(rango--> min:1 max:1000):").split()) 
        b_low, b_up = map(int, input("Valores de descarga bi(rango-->  min:1 max:10000):").split())
    else:
        print("1 o 2")
        