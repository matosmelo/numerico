from pylab import *


def f_x (t, x, y, vx, vy):
    return vx
      
def f_y (t, x, y, vx, vy):
    return vy

# G=6.67408, M=1.98892, D=pow(10,19)

def f_vx(t, x, y, vx, vy):
    G=6.67408
    M=1.98892
    D=pow(10,19)
    #return (12 * y * y)
    return (((-1) * (G) * (M) * (D) * x) / (pow((sqrt((x * x) + (y * y))), 3)))
def f_vy(t, x, y, vx, vy):
    G=6.67408
    M=1.98892
    D=pow(10,19)
    #return (-0.25 / (pow((cbrt(0.5 * x)), 1.5)))
    return (((-1) * (G) * (M) * (D) * y) / (pow((sqrt((x * x) + (y * y))), 3)))

def Euler_A_vx(t, dt, x, y, vx, vy):
    return (vx + ((dt / 2) * (f_vx(t, x, y, vx, vy) + f_vx(t + dt, x + (dt * f_x(t, x, y, vx, vy)), y + (dt * f_y(t, x, y, vx, vy)), vx + (dt * f_vx(t, x, y, vx, vy)), vy + (dt * f_vy(t, x, y, vx, vy))))))
      
       
def Euler_A_vy(t, dt, x, y, vx, vy):
    return (vy + ((dt / 2) * (f_vy(t, x, y, vx, vy) + f_vy(t + dt, x + (dt * f_x(t, x, y, vx, vy)), y + (dt * f_y(t, x, y, vx, vy)), vx + (dt * f_vx(t, x, y, vx, vy)), vy + (dt * f_vy(t, x, y, vx, vy))))))

def Euler_A_x(t, dt, x, y, vx, vy):
    return (x + ((dt / 2) * (f_x(t, x, y, vx, vy) + f_x(t + dt, x + (dt * f_x(t, x, y, vx, vy)), y + (dt * f_y(t, x, y, vx, vy)), vx + (dt * f_vx(t, x, y, vx, vy)), vy + (dt * f_vy(t, x, y, vx, vy))))))

def Euler_A_y(t, dt, x, y, vx, vy):
    return (y + ((dt / 2) * (f_y(t, x, y, vx, vy) + f_y(t + dt, x + (dt * f_x(t, x, y, vx, vy)), y + (dt * f_y(t, x, y, vx, vy)), vx + (dt * f_vx(t, x, y, vx, vy)), vy + (dt * f_vy(t, x, y, vx, vy))))))

if __name__ == '__main__':
    tempo_inicial = 1. 
    tempo_final = 10.
    m = 1.
    x_inicial = 1.
    y_inicial = 0. 
    vx_inicial = 6.28
    vy_inicial = 0.
    dt = (tempo_final - tempo_inicial) / 2. ** m
    
    t = tempo_inicial
    xa = x_inicial
    ya = y_inicial
    vxa = vx_inicial
    vya = vy_inicial

    valores_x = [x_inicial]
    valores_y = [y_inicial]
    valores_vx = [vx_inicial]
    valores_vy = [vy_inicial]
    valores_tempo = [tempo_inicial]

    while (t <= tempo_final):
        vx = Euler_A_vx(t, dt, xa, ya, vxa, vya)
        vxa = vx
        valores_vx = append(valores_vx, vx)
        
        vy = Euler_A_vy(t, dt, xa, ya, vxa, vya)
        vya = vy
        valores_vy = append(valores_vy, vy)
        
        x = Euler_A_x(t, dt, xa, ya, vxa, vya)
        xa = x
        valores_x = append(valores_x, x)
        
        y = Euler_A_y(t, dt, xa, ya, vxa, vya)
        ya = y
        valores_y = append(valores_y, y)
        
        t = t + dt 
        valores_tempo = append(valores_tempo, t)  

    figure(1)
    clf()
    title(r'Euler')
    plot(valores_x, valores_y)
    centerx = 0.
    centery = 0.
    plot(centerx, centery, 'ko')
    axis('equal')
    show()