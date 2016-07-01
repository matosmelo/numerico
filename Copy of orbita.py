from pylab import *

def rk():
    G = 4 * pi ** 2  # Definicao do G.
    M = 1.0  # Massa do corpo celeste
    Ro = 1.0  # Radianos da orbita 
    v = sqrt(398600.4418 / Ro) 
    print("Para circulo orbital r = %g, and v = %g." % (Ro, v)) 
    
    x0 = 1
    vy0 = 6.28  
    y0 = 0.0
    vx0 = 0.0
    
    tempo_inicial = 0.0
    tempo_final = 2  
    h = 0.0001  
    
    valores_x = [x0]
    valores_y = [y0]
    valores_vx = [vx0]
    valores_vy = [vy0]
    valores_tempo = [tempo_inicial]

    x_antigo = x0    
    y_antigo = y0
    vx = vx0
    vy = vy0
    t = tempo_inicial

    while (t < tempo_final):
        x = x_antigo + vx * h  
        y = y_antigo + vy * h

        k1 = h * funcaox(x, y)
        k2 = h * funcaox(x + (0.5 * h), y + (0.5 * k1))
        k3 = h * funcaox(x + (0.5 * h), y + (0.5 * k2))
        k4 = h * funcaox(x + h, y + k3)
        
        l1 = h * funcaoy(x, y)
        l2 = h * funcaoy(x + (0.5 * h), y + (0.5 * l1))
        l3 = h * funcaoy(x + (0.5 * h), y + (0.5 * l2))
        l4 = h * funcaoy(x + h, y + l3)
        
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
        
    return valores_x, valores_y, x0, vy0, h

def euler():
    G = 4 * pi ** 2  # Definicao do G.
    M = 1.0  # Massa do corpo celeste
    Ro = 1.0  # Radianos da orbita 
    v = sqrt(398600.4418 / Ro)
    print("Para circulo orbital r = %g, and v = %g." % (Ro, v)) 
    
    x0 = 1
    vy0 = 6.28  
    y0 = 0.0
    vx0 = 0.0
    
    tempo_inicial = 0.0
    tempo_final = 10  
    h = 0.01  
    
    valores_x = [x0]
    valores_y = [y0]
    valores_vx = [vx0]
    valores_vy = [vy0]
    valores_tempo = [tempo_inicial]

    x_antigo = x0    
    y_antigo = y0
    vx = vx0
    vy = vy0
    t = tempo_inicial

    while (t < tempo_final):
        x = x_antigo + vx * h  
        y = y_antigo + vy * h

        valor_funx = funcaox(x, y)
        valor_funy = funcaoy(x, y)
        
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
        
    return valores_x, valores_y, x0, vy0, h

def euler_modificado():
    G = 4 * pi ** 2  # Definicao do G.
    M = 1.0  # Massa do corpo celeste
    Ro = 1.0  # Radianos da orbita 
    v = sqrt(398600.4418 / Ro)
    print("Para circulo orbital r = %g, and v = %g." % (Ro, v)) 
    
    x0 = 1
    vy0 = 6.28  
    y0 = 0.0
    vx0 = 0.0
    
    tempo_inicial = 0.0
    tempo_final = 1 
    # h = 0.01  
    
    t = tempo_inicial
    xa = x0
    ya = y0
    vxa = vx0
    vya = vy0
    
    valores_x = [x0]
    valores_y = [y0]
    valores_vx = [vx0]
    valores_vy = [vy0]
    valores_tempo = [tempo_inicial]
    
    dt = 0.001 #(tempo_final - tempo_inicial) / 2.
    while (t < tempo_final):
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
        
        #print vxa, vya, xa, ya
    return valores_x, valores_y, vx0, vy0

def funcaox(x, y):
    G = 4 * pi ** 2  # Definicao do G.
    M = 1.0  # Massa do corpo celeste
    return -(G * M * x) / (sqrt(x ** 2 + y ** 2)) ** 3

def funcaoy(x, y):
    G = 4 * pi ** 2  # Definicao do G.
    M = 1.0  # Massa do corpo celeste
    return -(G * M * y) / (sqrt(x ** 2 + y ** 2)) ** 3

def f_vx(t, x, y, vx, vy):
    G=4 * pi ** 2
    M=1.0
    #return (12 * y * y)
    return -(G * M * y) / (sqrt(x ** 2 + y ** 2)) ** 3
def f_vy(t, x, y, vx, vy):
    G=4 * pi ** 2
    M=1.0
    #return (-0.25 / (pow((cbrt(0.5 * x)), 1.5)))
    return -(G * M * y) / (sqrt(x ** 2 + y ** 2)) ** 3

def Euler_A_vx(t, dt, x, y, vx, vy):
    
    f_modificado = f_vx(t + dt, x + (dt * vy), y + (dt * vy), vx + (dt * f_vx(t, x, y, vx, vy)), vy + (dt * f_vy(t, x, y, vx, vy)))
    
    return vx + ((dt / 2) * (f_vx(t, x, y, vx, vy) + f_modificado))
      
       
def Euler_A_vy(t, dt, x, y, vx, vy):
    return (vy + ((dt / 2) * (f_vy(t, x, y, vx, vy) + f_vy(t + dt, x + (dt * f_x(t, x, y, vx, vy)), y + (dt * f_y(t, x, y, vx, vy)), vx + (dt * f_vx(t, x, y, vx, vy)), vy + (dt * f_vy(t, x, y, vx, vy))))))

def Euler_A_x(t, dt, x, y, vx, vy):
    return (x + ((dt / 2) * (f_x(t, x, y, vx, vy) + f_x(t + dt, x + (dt * f_x(t, x, y, vx, vy)), y + (dt * f_y(t, x, y, vx, vy)), vx + (dt * f_vx(t, x, y, vx, vy)), vy + (dt * f_vy(t, x, y, vx, vy))))))

def Euler_A_y(t, dt, x, y, vx, vy):
    return (y + ((dt / 2) * (f_y(t, x, y, vx, vy) + f_y(t + dt, x + (dt * f_x(t, x, y, vx, vy)), y + (dt * f_y(t, x, y, vx, vy)), vx + (dt * f_vx(t, x, y, vx, vy)), vy + (dt * f_vy(t, x, y, vx, vy))))))

def f_x (t, x, y, vx, vy):
    return vx
      
def f_y (t, x, y, vx, vy):
    return vy

valores_x, valores_y, x0, vy0, h = euler()
figure(1)
clf()
title(r'Euler')
plot(valores_x, valores_y)
centerx = 0.
centery = 0.
plot(centerx, centery, 'ko')
axis('equal')

valores_x, valores_y, x0, vy0, h = rk()
figure(2)
clf()
title(r'RK')
plot(valores_x, valores_y)
centerx = 0.
centery = 0.
plot(centerx, centery, 'ko')
axis('equal')

valores_x, valores_y, vx0, vy0 = euler_modificado()
figure(3)
clf()
title(r'Euler Modificado')
plot(valores_x, valores_y)
centerx = 0.
centery = 0.
plot(centerx, centery, 'ko')
axis('equal')

show()


