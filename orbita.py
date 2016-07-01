from pylab import *

# Metodo Runge Kutta
def rk(tempo_delta):
    x_inicial = 2.
    vy_inicial = 0.5  
    y_inicial = 1.
    vx_inicial = 6.
    
    tempo_inicial = 1.
    tempo_final = 2.  
    h = (tempo_delta) / 2   
    
    valores_x = [x_inicial]
    valores_y = [y_inicial]
    valores_vx = [vx_inicial]
    valores_vy = [vy_inicial]
    valores_tempo = [tempo_inicial]

    x_antigo = x_inicial    
    y_antigo = y_inicial
    vx = vx_inicial
    vy = vy_inicial
    t = tempo_inicial

    while (t < tempo_final):
        x = x_antigo + vx * h  
        y = y_antigo + vy * h

        k1 = h * funcaox(x, y, t)
        k2 = h * funcaox(x + (0.5 * h), y + (0.5 * k1), t)
        k3 = h * funcaox(x + (0.5 * h), y + (0.5 * k2), t)
        k4 = h * funcaox(x + h, y + k3, t)
        
        l1 = h * funcaoy(x, y, t)
        l2 = h * funcaoy(x + (0.5 * h), y + (0.5 * l1), t)
        l3 = h * funcaoy(x + (0.5 * h), y + (0.5 * l2), t)
        l4 = h * funcaoy(x + h, y + l3, t)
        
        vx = vx + ((k1 + k2 + k2 + k3 + k3 + k4) / 6)
        vy = vy + ((l1 + l2 + l2 + l3 + l3 + l4) / 6)
        
        valores_x = append(valores_x, x)  
        valores_y = append(valores_y, y)
        valores_vx = append(valores_vx, vx)
        valores_vy = append(valores_vy, vy)
        valores_tempo = append(valores_tempo, t)
        
        x_antigo = x  
        y_antigo = y
        
        t = t + h  
        
    return valores_x, valores_y, valores_vx, valores_vy, h, valores_tempo

# Metodo de Euler
def euler(tempo_delta):
    x_inicial = 2.
    vy_inicial = 0.5  
    y_inicial = 1.
    vx_inicial = 6.
    
    tempo_inicial = 1.
    tempo_final = 2.  
    h = (tempo_delta) / 2  
    
#     x_inicial = 1.5
#     vy_inicial = 6.28  
#     y_inicial = 0.0
#     vx_inicial = 0.0
#     
#     tempo_inicial = 0.1
#     tempo_final = 8.0  
#     h = 0.01  
#     
    valores_x = [x_inicial]
    valores_y = [y_inicial]
    valores_vx = [vx_inicial]
    valores_vy = [vy_inicial]
    valores_tempo = [tempo_inicial]

    x_antigo = x_inicial    
    y_antigo = y_inicial
    vx = vx_inicial
    vy = vy_inicial
    t = tempo_inicial

    while (t < tempo_final):
        x = x_antigo + vx * h  
        y = y_antigo + vy * h

        valor_funx = funcaox(x, y, t)
        valor_funy = funcaoy(x, y, t)
        
        vx = vx + h * valor_funx
        vy = vy + h * valor_funy
        
        valores_x = append(valores_x, x)  
        valores_y = append(valores_y, y)
        valores_vx = append(valores_vx, vx)
        valores_vy = append(valores_vy, vy)
        valores_tempo = append(valores_tempo, t)
        
        x_antigo = x  
        y_antigo = y
        
        t = t + h  
        
    return valores_x, valores_y, valores_vx, valores_vy, h, valores_tempo

# Funcao para x
def funcaox(x, y, t):
#     G = 4 * pi ** 2  # Definicao do G.
#     M = 1.0  # Massa do corpo celeste
#     resultado = -(G * M * x) / (sqrt(x ** 2 + y ** 2)) ** 3
    resultado = 12 * t
    return resultado

# Funcao para y
def funcaoy(x, y, t):
#     G = 4 * pi ** 2  # Definicao do G.
#     M = 1.0  # Massa do corpo celeste
#     resultado = -(G * M * y) / (sqrt(x ** 2 + y ** 2)) ** 3
    resultado = -0.25 / (t ** 1.5)
    return resultado

import csv
n = 0
tempo_delta = 2. - 1.
csv_euler = csv.writer(open("tabelaEuler.csv", "wb"))

while n <= 15:
    csv_euler.writerow(["h", "valores do tempo", "Valores de x", "valores de y", "valores de vx", "valores de vy"])
    valores_x, valores_y, valores_vx, valores_vy, h, valores_tempo = euler(tempo_delta)
    val = 0
    while val < len(valores_tempo):
        csv_euler.writerow([h, valores_tempo[val], valores_x[val], valores_y[val], valores_vx[val], valores_vy[val]])
        val += 1
    csv_euler.writerow([' '])
    csv_euler.writerow(['Delta anterior / 2'])
    n += 1
    tempo_delta = h

n = 0
tempo_delta = 2. - 1.
csv_rk = csv.writer(open("tabelaRk.csv", "wb"))

while n <= 15:
    csv_rk.writerow(["h", "valores do tempo", "Valores de x", "valores de y", "valores de vx", "valores de vy"])
    valores_x, valores_y, valores_vx, valores_vy, h, valores_tempo = rk(tempo_delta)
    val = 0
    while val < len(valores_tempo):
        csv_rk.writerow([h, valores_tempo[val], valores_x[val], valores_y[val], valores_vx[val], valores_vy[val]])
        val += 1
    csv_rk.writerow([' '])
    csv_rk.writerow(['Delta anterior / 2'])
    n += 1
    tempo_delta = h


# figure(1)
# clf()
# title(r'Euler')
# plot(valores_x, valores_y)
# centerx = 0.
# centery = 0.
# plot(centerx, centery, 'ko')
# axis('equal')

# valores_x, valores_y, x_inicial, vy_inicial, h, valores_tempo = rk()
# figure(2)
# clf()
# title(r'RK')
# plot(valores_x, valores_y)
# centerx = 0.
# centery = 0.
# plot(centerx, centery, 'ko')
# axis('equal')
# show()
