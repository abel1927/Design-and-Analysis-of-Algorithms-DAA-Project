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

def check(D, n, points):
    """Respuesta al Predicado(D):
    El diametro**2 D contiene al conjunto?
    """
    global prefix_max_y, prefix_min_y, sufix_max_y, sufix_min_y
    limit_right = 1 #para buscar min_x hacia la derecha
    for limit_left in range(1,n+1): # para mover el max_x
        while limit_right < n and sdiameter_axes(points[limit_left][0], points[limit_right+1][0])<= D and abs(points[limit_left][0])>=abs(points[limit_right+1][0]):
            limit_right+=1 #mientras cumpla las condiciones avanza
        while abs(points[limit_left][0])<abs(points[limit_right][0]):
            limit_right-=1  # retrocede hasta que se valida limit_left
        # Se calculan los d**2 para las distribuciones formadas.
        y_min = min(prefix_min_y[limit_left-1], sufix_min_y[limit_right+1])
        y_max = max(prefix_max_y[limit_left-1], sufix_max_y[limit_right+1])
        d1 = sdiameter_axes(y_min, y_max)
        d2 = max(sdiameter_xy(points[limit_left][0], y_min), sdiameter_xy(points[limit_left][0], y_max))
        # si encontro una distribucion tal que D la contiene
        # responde si
        if max(d1,d2) <= D:
            return True 
    limit_left = n #para buscar min_x hacia la izquierda
    for limit_right in range(n,0,-1): # para mover el max_x
        while limit_left > 1 and sdiameter_axes(points[limit_left-1][0], points[limit_right][0])<= D and abs(points[limit_left-1][0])<=abs(points[limit_right][0]):
            limit_left-=1
        while abs( points[limit_left][0])>abs(points[limit_right][0]):
            limit_left+=1
        y_min = min(prefix_min_y[limit_left-1], sufix_min_y[limit_right+1])
        y_max = max(prefix_max_y[limit_left-1], sufix_max_y[limit_right+1])
        d1 = sdiameter_axes(y_min, y_max)
        d2 = max(sdiameter_xy(points[limit_right][0], y_min), sdiameter_xy(points[limit_right][0], y_max))
        if max(d1,d2) <= D:
            return True
    #Si no encuentra ninguna distribucion de puntos tal que el D^2 <= D, responde No
    return False

def tp_solution(n:int, points:List):
    if n==1:
        return 0
    # creo los arreglos para computar los maximos y minimos de las <y> por sufijos y prefijos
    # todo sobre el conjunto de puntos ordenados por las x 
    # prefix_max_y[i] es la max <y> en el [1-i]
    # prefix_min_y[i] es la min <y> en el [1-i]
    # sufix_max_y[i] es la max <y> en el [i-n]
    # sufix_min_y[i] es la min <y> en el [i-n]
    global prefix_max_y, prefix_min_y, sufix_max_y, sufix_min_y
    prefix_max_y, sufix_max_y = [0]*(n+2), [0]*(n+2) 
    prefix_min_y, sufix_min_y = [0]*(n+2), [0]*(n+2)
    points.sort(key= lambda t: t[0])
    points.insert(0,None)
    prefix_max_y[0], sufix_max_y[-1] = -int(1e8 + 1), -int(1e8 + 1)
    prefix_min_y[0], sufix_min_y[-1] = int(1e8 + 1), int(1e8 + 1)

    for i in range(1, n+1):
        prefix_max_y[i] = max(points[i][1], prefix_max_y[i-1])
        prefix_min_y[i] = min(points[i][1], prefix_min_y[i-1])
    for i in range(n,0,-1):
        sufix_max_y[i] = max(points[i][1], sufix_max_y[i+1])
        sufix_min_y[i] = min(points[i][1], sufix_min_y[i+1])
    
    #min_sd diametro**2, guarda el menor diametro resultante de mover todos los puntos a uno de los ejes respectivamente.
    #la respuesta optima tiene que estar acotada por el minimo de los d**2 resultantes de proyectar en uno de los ejes todos los puntos
    min_sd  = min(sdiameter_axes(points[1][0], points[-1][0]),sdiameter_axes(prefix_min_y[-2], prefix_max_y[-2]))
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
    min_sd = tp_solution(n, in_points)
    stdout.write(str(min_sd))