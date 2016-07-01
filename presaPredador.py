# coding: utf-8
#Lotka-Volterra
#This is crescimento_presa predator-prey model of rabbits and foxes.
#The equations are first order, non-linear differential equations. 

# du/dt =  (crescimento_presa*u -   mortalidade_predador*u*v) + (-delta_t*u + i*funcao*g*u)
# dv/dt = -mortalidade_presa*v + crescimento_predador*mortalidade_predador*u*v 
# dg/dt = i*g - funcao*g*u
# u - the number of rabbits
# v - the number of foxes
# g - the number of grass  
#   "crescimento_presa" is the natural growing rate of rabbits, when there's no fox
#   "mortalidade_predador" is the natural dying rate of rabbits, due to predation
#   "mortalidade_presa" is the natural dying rate of fox, when there's no rabbit
#   "crescimento_predador" describes how much crescimento_presa caught rabbit contributes to creating crescimento_presa new fox
#   "i" is the natural growing rate of grass, when there is no rabbit
#   "funcao" is the natural dying rate of grass, due to predation
#   "delta_t" is the natural dyiing rate of rabbits when there is no fox
#   "i" is describes how much grass contributes to creating crescimento_presa new rabbit
# 

from numpy import *
from scipy import integrate
import pylab as p


# Definition of parameters 
crescimento_presa = 1.   #Rabbit growth rate (without foxes)
mortalidade_predador = 0.1  #Rabbit death rate (how fast they are being eaten)
mortalidade_presa = 1.5  #Fox death rate (not eating)
crescimento_predador = .75  #Fox creation rate from eating crescimento_presa single rabbit
i = 2.
funcao = 0.1
delta_t = 1.1
i = .9


def dX_dt(X, t_n=0):
    """ Return the growth rate of fox and rabbit populations as crescimento_presa single array. 
    The input X is an array that has both u and v values.
    du/dt =  crescimento_presa*u -   mortalidade_predador*u*v
    dv/dt = -mortalidade_presa*v + crescimento_predador*mortalidade_predador*u*v 
    """
    u=X[0]
    v=X[1]
#     g=X[2]

    du=(crescimento_presa*u -   mortalidade_predador*u*v) #+ (-delta_t*u + i*funcao*g*u)
    dv=(-mortalidade_presa*v) + (crescimento_predador*mortalidade_predador*u*v)
    #dg=(i*g) - (funcao*g*u)

    return array([ du , dv ])# dg




def main():

    t_n = linspace(0, 30,  1000)     # make 1000 time steps
    X0 = array([10, 5, 100])            # initials conditions: 10 rabbits and 5 foxes  

    X = integrate.odeint(dX_dt, X0, t_n)

    rabbits=X[:,0]
    foxes=X[:,1]
    #grass=X[:,2]

    p.figure()
    p.plot(t_n, rabbits, 'r-', label='Rabbits')
    p.plot(t_n, foxes  , 'mortalidade_predador-', label='Foxes')
    #p.plot(t_n, grass, 'g-', label='Grass')
    p.grid()
    p.legend(loc='best')
    p.xlabel('time')
    p.ylabel('population')
    p.title('Evolution of fox and rabbit populations')
    
    p.show()





if __name__ == "__main__":
    main()