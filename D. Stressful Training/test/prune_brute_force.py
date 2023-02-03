from sys import stdin,stdout

def check_time_condition(a_p,rk,b):
    """
    Para validar las condiciones de tiempo necesarias para que pueda haber una solucion
    rk= tiempo restante
    a_p = energia actual de los equipos
    cond2: si rk>=2 y al menos dos equipos cumplen que a_p[i]<b[i], no hay solucion
    cond3: si rk>=3 y al menors tres equipos cumplen que a_p[i]<=b[i], no hay solucion
    """
    if rk<2:
        return True
    cond_three = 0
    cond_two = 0
    for i in range(len(a_p)):
        if b[i]>= a_p[i]:
            cond_three += 1
            if rk>=3 and cond_three==3:
                return False
            if b[i] > a_p[i]:
                cond_two+=1
                if cond_two==2:
                    return False
    return True
    

def variations(a_p, x, b,v, time):
    """
    Generar las posibles selecciones del equipo a cargar en cada minuto. 
    Variaciones con repeticion de n en k
    """
    if time == len(v): # Se completo una secuencia, entonces hay respuesta afirmativa
        return True
    if not check_time_condition(a_p,k-time,b): # Comprobar que puede haber solucion
        return False
    for i in range(len(a_p)):
        v[time] = i
        a_p[i] += x
        for j in range(len(a_p)):
            a_p[j]-=b[j]
        if min(a_p)>=0:  # si luego de cargar el elemento en ese minuto, alguno se descarga, no hay solucion
            if variations(a_p,x,b,v,time+1):
                return True
        for j in range(len(a_p)):
            a_p[j]+=b[j]
        a_p[i] -= x
    return False
    

def is_solution(a_p, x,k,b):
    return variations(a_p,x,b,[0]*(k-1),0)

def prune_brute_force(n,k,a,b):
    max_solution = max(b)*k + 1
    if check_time_condition(a, k,b):
        for x in range(max_solution):
            if is_solution([_ for _ in a],x,k,b):
                return str(x)
    return '-1'


    #while left < rigth-1:
    #    mid = (left+rigth)//2
    #    if is_solution(mid):
    #        rigth = mid
    #    else:
    #        left = mid
    #if not is_solution(rigth): # por la estructura del predicado, si el de la derecha es False, el de la izq es False.
    #    stdout.write('-1')
    #else:
    #    stdout.write(str(left)) if is_solution(left) else stdout.write(str(rigth))

if __name__ == "__main__":
    # n- numero de equipos
    # k- total de minutos
    n, k = map(int, stdin.readline().split())
    # a- array con las cargas iniciales de cada equipo
    a = list(map(int, stdin.readline().split()))
    # b- array con los valores de descarga por minuto de cada equipo
    b = list(map(int, stdin.readline().split()))
    sol = prune_brute_force(n,k,a,b)
    stdout.write(sol)