from sys import stdin, stdout, maxsize
from typing import List

def sdiameter_axes(axis_one, axes_two):
    """calcula el diametro**2 entre elementos de un mismo eje"""
    return int(pow(axis_one-axes_two, 2))

def sdiameter_xy(x, y):
    """calcula el diametro**2 entre elementos de ambos ejes"""
    return int(pow(x, 2))+int(pow(y, 2))

prefix_max_y = maxsize
sufix_max_y = maxsize
prefix_min_y = maxsize
sufix_min_y = maxsize

def n2_solution(n:int, points:List):

    if n==1:
        return 0
    # creo los arreglos para computar los maximos y minimos de las <y> por sufijos y prefijos
    # todo sobre el conjunto de puntos ordenados por las x 
    # prefix_max_y[i] es la max <y> en el [0-i]
    # prefix_min_y[i] es la min <y> en el [0-i]
    # sufix_max_y[i] es la max <y> en el [i-n)
    # sufix_min_y[i] es la min <y> en el [i-n)
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
    
    #minimo diametro**2, min_sd guarda la respuesta, que va a estar acotada por el minimo diametro
    #resultante de mover todos los puntos a uno de los ejes respectivamente.
    min_sd = min(sdiameter_axes(points[0][0], points[-1][0]),sdiameter_axes(prefix_min_y[-1], prefix_max_y[-1]))

    # Vamos a crear todos los posibles intervalos de puntos consecutivos en las x
    # para eso, por cada limite izq, se prueban los n posibles limites derechos, y 
    # se computan los diamtros**2 de esa distribucion
    for i in range(n): 
        left_x = points[i][0]  # limite izq
        for j in range(i, n):
            y_min, y_max = maxsize,-maxsize
            right_x = points[j][0] # limite der
            max_x = max(abs(left_x), abs(right_x))  # x mas alejada del eje Y
            left_y = False
            if i > 0: # Comprobar si hay <y's> a la izq del limite izq
                # nos quedamos con la menor y la mayor, las restantes estan contenidas
                y_min = prefix_min_y[i-1]  
                y_max = prefix_max_y[i-1]
                left_y = True
            right_y = False
            if j < n-1: # Comprobar si hay <y's> a la der del limite der
                # se repite con las del limite derecho, ahora comparando con las del segmento
                # anterior si las hubiera 
                y_min = min(y_min, sufix_min_y[j+1])
                y_max = max(y_max, sufix_max_y[j+1])
                right_y = True
            current_mind_sd = -maxsize # para guardar el menor diametro**2 posible con esta distribucion
            if left_y or right_y:
                #calculamos el diametro**2 de las y
                # y el diametro**2 de la mayor x a la menor y mayor y(diagonales)
                current_mind_sd = max(current_mind_sd, sdiameter_axes(y_min, y_max))
                current_mind_sd = max(current_mind_sd, max(sdiameter_xy(max_x, y_min), sdiameter_xy(max_x, y_max)))
            # ahora se compara con el diametro en las x
            current_mind_sd = max(current_mind_sd, sdiameter_axes(left_x, right_x))
            # si en esta distribucion se encuentra un diametro menor que el que se tiene
            # se actualiza
            min_sd = min(min_sd, current_mind_sd)   
    return min_sd

if __name__ == "__main__":
    n = int(stdin.readline())
    in_points = []
    for _ in range(n):
        x, y = map(int, stdin.readline().split())
        in_points.append((x,y))
    min_sd = n2_solution(n, in_points)
    stdout.write(str(min_sd))