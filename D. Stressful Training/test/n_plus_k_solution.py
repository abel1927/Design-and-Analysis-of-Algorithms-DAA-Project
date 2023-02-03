from sys import stdin,stdout

n = -1   #numero de equipos
k = -1   #tiempo
a = None #cargas
b = None #descargas

def check(x):
    """
    n = total de equipos
    k = minutos totales
    a = cargas iniciales
    b = valor de descarga por minuto
    x = potencia del cargador

    Devuelve True si x es una solucion factible, sino False
    """
    global n,k, a, b
    # next es una lista de listas por cada minuto entre el inicio y el final(k), donde se guarda 
    # para cada minuto j, el indice de los equipos que se descargan en ese minuto
    next = [[] for _ in range(k)] 
    c_i = [0]*n # c_i guarda la carga del equipo i en el minuto de su descarga
    for i in range(n):
        end_time = a[i]//b[i] + 1 # ultimo minuto de carga del equipo i
        if end_time < k:
            c_i[i] = a[i]%b[i]
            next[end_time].append(i)
    idx_next = 0 # mantiene la referencia a la primera posicion no vacia en next
    for j in range(k): # se hace una iteracion por los minutos que dura el concurso
        while idx_next < k and len(next[idx_next]) == 0: # se coloca la referencia en la primera posicion no vacia
            idx_next+=1
        if idx_next <= j: # el ultimo momento de carga del equipo pasó, se hizo negativa.
            return False
        if idx_next == k: # se llego al final sin nuevas descargas.
            return True
        idx_charger = next[idx_next].pop() # selecciono uno de los mas proximos a descargarse
        c_i[idx_charger]+=x # se carga
        time_to_end = c_i[idx_charger] // b[idx_charger] # se recalcula el tiempo restante de carga
        c_i[idx_charger] %=  b[idx_charger]
        if idx_next+time_to_end<k: # si supera k, ese equipo ya no se descarga
            next[idx_next+time_to_end].append(idx_charger)
    return True


def n_plus_k_solution(in_n,in_k,in_a,in_b):
    global n,k, a, b
    n, k = in_n, in_k
    a, b = in_a, in_b
    left = 0
    rigth= k*max(b)
    while left < rigth-1:
        mid = (left+rigth)//2
        if check(mid):
            rigth = mid
        else:
            left = mid
    if not check(rigth): # por la estructura del predicado, si el de la derecha es False, el de la izq es False.
        return '-1'
    else:
        return str(left) if check(left) else str(rigth)


if __name__ == "__main__":
    # n- numero de equipos
    # k- total de minutos
    n, k = map(int, stdin.readline().split())
    # a- array con las cargas iniciales de cada equipo
    a = list(map(int, stdin.readline().split()))
    # b- array con los valores de descarga por minuto de cada equipo
    b = list(map(int, stdin.readline().split()))
    sol = n_plus_k_solution(n,k,a,b)
    stdout.write(sol)