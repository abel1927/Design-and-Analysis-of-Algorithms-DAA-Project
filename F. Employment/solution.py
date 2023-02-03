from sys import stdin, stdout, maxsize

def calc_distance(m, h,w):
    if h == w:
        return 0
    if h>w:
        h,w=w,h
    d1 = w - h
    d2 = h + m - w
    return min(d1,d2)

#ciudades, y cantidad de vacantes-empleados
m, n = map(int, stdin.readline().split())
result = [0]*n
#vacantes
v = list(map(int, stdin.readline().split()))
#candidatos(casa)
c = list(map(int, stdin.readline().split()))

vacancies = []
candidates = []
for i in range(n):
    #pares (posicion original, valor)
    vacancies.append((i, v[i]))   
    candidates.append((i, c[i]))
# se ordena por el orden de la ciudad
vacancies.sort(key=lambda x: x[1])
candidates.sort(key=lambda x: x[1])

min_distance = maxsize  # para guardar la distancia optima
result_distribution = None # para guardar la distribucion optima
for i in range(n): # se itera por las vacantes, para seleccionar la del primer candidato  
    still_better = True
    current_distance = 0  # para mantener la distancia acumulada en la distribucion actual
    current_distribution = [-1]*n  # para mantener la distribucion actual
    current_distribution[vacancies[i][0]] = candidates[0][0]+1 # se coloca al primer candidato
    current_distance += calc_distance(m, candidates[0][1], vacancies[i][1]) # se calcula la distancia
    if current_distance >= min_distance: # poda
        continue
    cand_idx = 1 # indice del candidato
    j = i+1
    while j < n:  # se itera desde esa vacante hasta la de mayor ciudad
        # se calcula distancia para los candidadatos asignados a esas vacantes
        d = calc_distance(m, candidates[cand_idx][1], vacancies[j][1]) 
        if current_distance + d >= min_distance:  #poda
            still_better = False
            break
        else:
            current_distance += d
            current_distribution[vacancies[j][0]] = candidates[cand_idx][0]+1
        cand_idx+=1
        j+=1
    if not still_better:
        continue
    j = 0
    while j < i: # se sigue colocando los candidatos(orden circular, se comienza por el principio del arreglo,
        #manteniendo en aumento el indice del candidato)
        d = calc_distance(m, candidates[cand_idx][1], vacancies[j][1])
        if current_distance + d >= min_distance:
            still_better = False
            break
        else:
            current_distance += d
            current_distribution[vacancies[j][0]] = candidates[cand_idx][0]+1
        cand_idx+=1
        j+=1
    if still_better and min_distance>current_distance: # si se disminuye el valor de distancia, se actualiza
        min_distance = current_distance
        result_distribution = current_distribution

stdout.write(str(min_distance)+'\n')
stdout.write(" ".join(map(str,result_distribution)))