from sys import stdin, stdout, maxsize
from typing import List

def sdiameter_axes(axis_one, axes_two):
    """calcula el diametro**2 entre elementos de un mismo eje"""
    return int(pow(axis_one-axes_two, 2))

def sdiameter_xy(x, y):
    """calcula el diametro**2 entre elementos de ambos ejes"""
    return int(pow(x, 2))+int(pow(y, 2))

prefix_max_y = None
sufix_max_y = None
prefix_min_y =None
sufix_min_y = None

#source va a ser el Xl/Xr elegido y target el xl/xr a #validar 
def valid(source, target, D, points):
    """
    Respuesta al predicado: Es target un x_min valida para source?
    """
    global prefix_max_y, prefix_min_y, sufix_max_y, sufix_min_y
    if sdiameter_axes(points[source][0], points[target][0]) > D:
        return False
    if abs(points[source][0])<abs(points[target][0]):
        return False
    return True

def check(D, n, points):
    """
    Respuesta al Predicado(D):
    El diametro**2 D contiene al conjunto?
    """
    global prefix_max_y, prefix_min_y, sufix_max_y, sufix_min_y
    min_sd = maxsize
    for limit_left in range(n):
        if points[limit_left][0]>0:
            break
        limit_right = limit_left # el mejor limite der hasta el momento
        end = n
        while limit_right+ 1 < end:
            mid = (limit_right+end)//2
            if valid(limit_left, mid, D, points):
                limit_right = mid # el ultimo "si" es el mejor xr
            else:
                end = mid
        y_min, y_max = maxsize,-maxsize
        left_y = False
        if limit_left > 0: # Comprobar si hay <y's> a la izq del limite izq
            # nos quedamos con la menor y la mayor, las restantes estan contenidas
            y_min = prefix_min_y[limit_left-1]  
            y_max = prefix_max_y[limit_left-1]
            left_y = True
        right_y = False
        if limit_right < n-1: # Comprobar si hay <y's> a la der del limite der
            # se repite con las del limite derecho, ahora comparando con las del segmento
            # anterior si las hubiera 
            y_min = min(y_min, sufix_min_y[limit_right+1])
            y_max = max(y_max, sufix_max_y[limit_right+1])
            right_y = True
        current_mind_sd = maxsize
        if left_y or right_y:
            d1 = sdiameter_axes(y_min, y_max)
            d2 = max(sdiameter_xy(points[limit_left][0], y_min), sdiameter_xy(points[limit_left][0], y_max))
            current_mind_sd = max(d1,d2)
        min_sd = min(min_sd, current_mind_sd)
        if min_sd <= D:
            return True

    for limit_right in range(n-1, -1, -1):
        if points[limit_right][0]<0:
            break
        limit_left = limit_right # el mejor limite izquierdp hasta el momento
        end = -1
        while end < limit_left-1:
            mid = (limit_left+end)//2
            if valid(limit_right,mid, D, points):
                limit_left = mid # el ultimo "si" es el mejor xl
            else:
                end = mid
        y_min, y_max = maxsize,-maxsize
        left_y = False
        if limit_left > 0: # Comprobar si hay <y's> a la izq del limite izq
            # nos quedamos con la menor y la mayor, las restantes estan contenidas
            y_min = prefix_min_y[limit_left-1]  
            y_max = prefix_max_y[limit_left-1]
            left_y = True
        right_y = False
        if limit_right < n-1:# Comprobar si hay <y's> a la der del limite der
            # se repite con las del limite derecho, ahora comparando con las del segmento
            # anterior si las hubiera 
            y_min = min(y_min, sufix_min_y[limit_right+1])
            y_max = max(y_max, sufix_max_y[limit_right+1])
            right_y = True
        current_mind_sd = maxsize
        if left_y or right_y:
            #calculamos el diametro**2 de las y
            # y el diametro**2 de la mayor x a la menor y mayor y(diagonales)
            d1 = sdiameter_axes(y_min, y_max)
            d2 = max(sdiameter_xy(points[limit_right][0], y_min), sdiameter_xy(points[limit_right][0], y_max))
            current_mind_sd = max(d1,d2)
        min_sd = min(min_sd, current_mind_sd)
        if min_sd <= D:
            return True    
    return False

def bs_solution(n:int, points:List):
    if n==1:
        return 0
    # creo los arreglos para computar los maximos y minimos de las <y> por sufijos y prefijos
    # todo sobre el conjunto de puntos ordenados por las x 
    # prefix_max_y[i] es la max <y> en el [0-i]
    # prefix_min_y[i] es la min <y> en el [0-i]
    # sufix_max_y[i] es la max <y> en el [i-n)
    # sufix_min_y[i] es la min <y> en el [i-n)
    global prefix_max_y, prefix_min_y, sufix_max_y, sufix_min_y
    prefix_max_y, sufix_max_y = [0]*n, [0]*n 
    prefix_min_y, sufix_min_y = [0]*n, [0]*n
    points.sort(key= lambda t: t[0])
    prefix_max_y[0], sufix_max_y[-1] = points[0][1], points[-1][1]
    prefix_min_y[0], sufix_min_y[-1] = points[0][1], points[-1][1]

    for i in range(1, n):
        prefix_max_y[i] = max(points[i][1], prefix_max_y[i-1])
        prefix_min_y[i] = min(points[i][1], prefix_min_y[i-1])
    for i in range(n-2,-1,-1):
        sufix_max_y[i] = max(points[i][1], sufix_max_y[i+1])
        sufix_min_y[i] = min(points[i][1], sufix_min_y[i+1])
    
    #max_sd diametro**2, guarda el menor diametro resultante de mover todos los puntos a uno de los ejes respectivamente.
    #la respuesta optima tiene que estar acotada por el minimo de los d**2 resultantes de proyectar en uno de los ejes todos los puntos
    min_sd = min(sdiameter_axes(points[0][0], points[-1][0]),sdiameter_axes(prefix_min_y[-1], prefix_max_y[-1]))
    left, right = 0, min_sd 
    while( left <= right):
        D = (left + right)//2
        if check(D, n, points):
            min_sd = D #sabemos que el ultimo si sera la solucion
            right = D-1
        else:
            left = D+1
    return min_sd 

if __name__ == "__main__":
    n = int(stdin.readline())
    in_points = []
    for _ in range(n):
        x, y = map(int, stdin.readline().split())
        in_points.append((x,y))
    _sd = bs_solution(n, in_points)
    stdout.write(str(_sd))