from sys import stdin,stdout

n = -1   #numero de equipos
k = -1   #tiempo
a = None #cargas
b = None #descargas

def get_min(j, a_p)->int:
    global n, k, a, b
    min = k#-j  # quedan k-j minutos, todo con carga por encima, termina
    ans = -1
    for i in range(n):
        time_left = a_p[i]//b[i] # tiempo restante para descargarse
        if time_left < min:
            ans = i
            min = time_left
    return ans

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
    a_p = [_ for _ in a]   # copia de a para guardar las cargas actualizadas
    for j in range(k):
        next = get_min(j, a_p)
        if next == -1: # todos tienen carga para terminar
            return True
        elif a_p[next]<0: # el menor ya tenia carga negativa, con lo cual no es valido x
            return False
        else:
            a_p[next] += x # se carga el elegido
        for i in range(n):
            a_p[i]-=b[i]
    return True

def nk_solution(in_n,in_k,in_a,in_b):
    global n,k, a, b
    n,k = in_n, in_k
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
    sol = nk_solution(n,k,a,b)
    stdout.write(sol)
