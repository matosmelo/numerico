# coding: utf-8
from numpy import *
import pylab as p

#############################
# Nome: Felipe de Matos Melo#
# N 7658876                 #
# MAP0214 - Fisica          #
#############################

# Declaracao das variaveis
n = 5500 # Número de repeticoes.
tempo_inicial = 0.0  # Tempo inicial
tempo_final = 120.0  # Tempo final
delta_t = (tempo_final - tempo_inicial) / n

# Paramentros do modelo
crescimento_presa = 0.55 # Taxa de crescimento da presa (sem predador)
crescimento_predador = 0.01 # Taxa de crescimento da predador (se aliemtando da presa)
mortalidade_presa = 0.05 # Taxa mortalidade da presa
mortalidade_predador = 0.3  # Taxa mortalidade do predador

presa = []
predador = []
tempo = []
presa.append(10.0) # Quantidade de presa no inicio
predador.append(10.0) # Quantidade de predador no inicio
tempo.append(0.0)

for i in range(n):
    # Usando método de Euler para calcular
    y_1 = presa[i] + (delta_t* ((presa[i]*crescimento_presa) - (mortalidade_presa * predador[i] * presa[i]) ))
    predador_atual = predador[i] + (delta_t * ((predador[i] * crescimento_predador * presa[i]) - (predador[i] * mortalidade_predador)))
    
    #Salvando os valores
    presa.append(y_1)
    predador.append(predador_atual)
    
    t_n = tempo_inicial + delta_t
    tempo_inicial = t_n
    tempo.append(t_n)
    
#Imprime os valores 
print presa
print predador
print tempo

# Gera figura 1 Populaca de predador e presa por tempo
p.figure(1)
p.plot( tempo, presa, linestyle='--',label='Presas', color='black')
p.plot( tempo, predador, label='Predadores', color='black')
p.grid()
p.xlabel('Tempo[dias]')
p.ylabel('Populacao')
p.ylim([0,100])
p.title('Presa-Predador')
p.legend(loc='best') 
p.savefig('presa-predador por tempo.pdf')

# Gera figura 2 Populaca de predador por presa
p.figure(2)
p.plot( presa, predador, color='black')
p.grid()
p.xlabel('Populacao de presas')
p.ylabel('Populacao de predadores')
p.title('Presa-Predador')

p.savefig('presa por predador.pdf')

p.show()
