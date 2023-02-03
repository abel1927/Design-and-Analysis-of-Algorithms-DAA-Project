from sys import stdin, stdout, maxsize
from itertools import permutations
from typing import List, Tuple
from brute_force import calc_distance

def brute_force(m,n,vacancies,candidates)->Tuple[int,List]:
    p = list(permutations(range(1,n+1),n))
    result = []
    min_d = maxsize
    for perm in p:
        temp_d = 0
        for i in range(n):
            temp_d+= calc_distance(m,candidates[perm[i]-1]-1,vacancies[i]-1)
        if temp_d < min_d:
            result.clear()
            result.append(perm)
            min_d = temp_d
        elif temp_d == min_d:
            result.append(perm)
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
    print(sorted(candidates))
    print(sorted(vacancies))
    for p in r:
        temp = []
        for i in range(len(p)):
            temp.append((vacancies[i],candidates[p[i]-1]))
        print(temp)
        # stdout.write(" ".join(map(str,temp))+"\n")
    
