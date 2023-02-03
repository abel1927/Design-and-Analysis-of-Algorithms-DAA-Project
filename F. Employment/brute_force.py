from sys import stdin, stdout, maxsize
from itertools import permutations

def calc_distance(m, h,w):
    if h == w:
        return 0
    if h>w:
        h,w=w,h
    d1 = w - h
    d2 = h + m - w
    return min(d1,d2)

def brute_force(m,n,vacancies,candidates):
    p = list(permutations(range(1,n+1),n))
    result = None
    min_d = maxsize
    for perm in p:
        temp_d = 0
        for i in range(n):
            temp_d+= calc_distance(m,candidates[perm[i]-1]-1,vacancies[i]-1)
        if temp_d < min_d:
            result = perm
            min_d = temp_d
    return min_d, result
    

if __name__ == "__main__":
    #ciudades, y cantidad de vacantes-empleados
    m, n = map(int, stdin.readline().split())
    #vacantes
    vacancies = list(map(int, stdin.readline().split()))
    #casas
    candidates = list(map(int, stdin.readline().split()))

    d, r = brute_force(m,n,vacancies,candidates)
    stdout.write(str(d)+'\n')
    stdout.write(" ".join(map(str,r)))