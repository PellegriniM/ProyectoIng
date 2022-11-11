from time import sleep

def barra_progreso(part, total, lengh=30):
    frac = part/total
    completed = int(frac * lengh)
    missing = lengh - completed
    bar = f"[{'#'*completed}{'-'*missing}]{frac:.2%}"
    return bar
n = 50

def Barra():
    print("--------------Cargando--------------")
    for i in range (n + 1):
        sleep(0.1)
        print(barra_progreso(i, n, 35), end='\r')
    print(end='\n\r')
    print("------------------------------------")