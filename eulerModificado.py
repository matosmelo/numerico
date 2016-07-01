# coding: utf-8
from numpy import *
import pylab as p
from matplotlib.mlab import log2

# #############################
# # Nome: Felipe de Matos Melo#
# # N 7658876                 #
# # MAP0214 - Fisica          #
# #############################

# Funcao calculada
def funcao(t, y_n):
    return 2 * (y_n * t)

# Parametros
t_f = 1.55
h = 0.1
t_n = 1.0
y_n = 1.0
m = []

# Euler modificado
resultado_euler_modificado = []
valor_exato_funcao = []
while t_n < t_f:
    resultado_euler_modificado.append(y_n)
    
    euler = y_n + h * funcao(t_n, y_n)
    y_n += (h / 2.) * (funcao(t_n, y_n) + funcao(t_n + h, euler))
    
    m.append(t_n)
    
    valor_exato_funcao.append(pow(2.7182, (pow(t_n, 2) - 1))) 
    
    t_n += h   

# Calculo do erro
contador = 0
erro_absoluto = []
erro_absoluto_anterior = []
for n in valor_exato_funcao:
    if contador != 0:
        erro_absoluto_anterior.append(abs(resultado_euler_modificado[contador - 1] - n))
    else:
        erro_absoluto_anterior.append(0.0)
    
    erro_absoluto.append(abs(resultado_euler_modificado[contador] - n))
    
    contador += 1

# Encontra a diferenca dos erros e o log da diferenca dos erros
deferenca_erros = []
log_erro = []
i = 1
while i < len(erro_absoluto):
    deferenca_erros.append(erro_absoluto_anterior[i] / erro_absoluto[i])
    log_erro.append(log2(erro_absoluto_anterior[i] / erro_absoluto[i]))
    i += 1

# Imprime os valores
print u"Passos: ", m
print u"Valor do y_n: ", resultado_euler_modificado
print u"valor exato da funcao: ", valor_exato_funcao
print u"erro m-1: ", erro_absoluto_anterior  
print u"erro absoluto: ", erro_absoluto    
print u"Diferenca dos erros: ", deferenca_erros
print u"log da diferenca dos erros: ", log_erro

# Gera o grafico 
p.figure(1)
p.plot( m, valor_exato_funcao, m, resultado_euler_modificado,"--", color='black')
p.xlabel('Passos')
p.ylabel('Valor encontrado')
p.grid()
p.ylim([0,5])
p.xlim([1,1.55])
p.title('Euler Modificado')
p.savefig('euler_modificado_01.pdf')
p.show()
