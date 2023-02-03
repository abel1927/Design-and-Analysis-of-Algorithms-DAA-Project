from sys import stdin, stdout, maxsize

points = []
min_sd = maxsize # diametro**2 minimo

def sdiameter_axes(axis_one, axes_two):
    """calcula el diametro**2 entre elementos de un mismo eje"""
    return int(pow(axis_one-axes_two, 2))

def sdiameter_xy(x, y):
    """calcula el diametro**2 entre elementos de ambos ejes"""
    return int(pow(x, 2))+int(pow(y, 2))

def binaries_string(n, bin, i):
    global min_sd
    if i == n:
        min_x = maxsize   # minimo punto en el eje x
        max_x = -maxsize  # maximo punto en el eje x
        min_y = maxsize   # minimo punto en el eje y
        max_y = -maxsize  # maximo punto en el eje y
        count_x = 0       # cantidad de puntos en el eje x
        count_y = 0       # cantidad de puntos en el eje y   
        for i in range(n):
            if bin[i]: # X
                count_x += 1
                x = points[i][0]
                min_x = min(x,min_x)
                max_x = max(x, max_x)
            else: # Y
                count_y += 1
                y = points[i][1]
                min_y = min(y,min_y)
                max_y = max(y, max_y)
        if count_x == 0: # si no hay puntos en las x, no nos interesa este eje
            min_sd = min(min_sd,sdiameter_axes(min_y, max_y))
        elif count_y == 0: # si no hay puntos en las y, no nos interesa este eje
            min_sd = min(min_sd,sdiameter_axes(min_x, max_x))
        else:
            d0 = -1
            if count_x >1: # si hay un solo puntos en las x, no hay distancia en este eje
                d0 = sdiameter_axes(min_x, max_x)
            if count_y > 1: # si hay un solo puntos en las y, no hay distancia en este eje
                d0 = max(d0, sdiameter_axes(min_y, max_y))
            # las 4 diagonales
            d1 = sdiameter_xy(min_x, min_y)
            d2 = sdiameter_xy(min_x, max_y)
            d3 = sdiameter_xy(max_x, min_y)
            d4 = sdiameter_xy(max_x, max_y)
            min_sd = min(min_sd, max(d0, max(max(d1,d2), max(d3,d4))))
        return
    bin[i] = 0
    binaries_string(n, bin, i + 1)
    bin[i] = 1
    binaries_string(n, bin, i + 1)



def brute_force(n, in_points):
    global points, min_sd
    points = in_points
    min_sd = maxsize

    binaries_string(n, [None]*n, 0)
    return min_sd
    
if __name__ == "__main__":
    n = int(stdin.readline())
    in_points = []
    for _ in range(n):
        x, y = map(int, stdin.readline().split())
        in_points.append((x,y))
    r_min_sd = brute_force(n, in_points)
    stdout.write(str(r_min_sd))



