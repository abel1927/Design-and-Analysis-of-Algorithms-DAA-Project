from sys import stdin, stdout

def variations(a_p, x, b, v, time):
    """
    Generar las posibles selecciones del equipo a cargar en cada minuto. 
    Variaciones con repeticion de n en k
    """
    if time == len(v): # Se completo una secuencia, entonces hay respuesta afiramativa
        return True
    for i in range(len(a_p)):
        v[time] = i
        a_p[i] += x
        for j in range(len(a_p)):
            a_p[j]-=b[j]
        if min(a_p)>=0:   # si luego de cargar el elemento en ese minuto, alguno se descarga, no hay solucion
            if variations(a_p,x,b,v,time+1):
                return True
        for j in range(len(a_p)):
            a_p[j]+=b[j]
        a_p[i] -= x
    return False
    

def is_solution(a_p, x,k,b):
    return variations(a_p,x,b,[0]*(k-1),0)

def brute_force(n,k,a,b):
    max_solution = max(b)*k + 1
    for x in range(max_solution):
        if is_solution([_ for _ in a],x,k,b):
            return str(x)
    return '-1'

if __name__ == "__main__":
    # n- numero de equipos
    # k- total de minutos
    n, k = map(int, stdin.readline().split())
    # a- array con las cargas iniciales de cada equipo
    a = list(map(int, stdin.readline().split()))
    # b- array con los valores de descarga por minuto de cada equipo
    b = list(map(int, stdin.readline().split()))
    sol = brute_force(n,k,a,b)
    stdout.write(sol)