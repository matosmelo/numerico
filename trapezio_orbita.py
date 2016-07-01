# coding: utf-8
from numpy import *
import pylab as p
import re
if __name__ == '__main__':
    arquivo = open('saida.txt', 'r')
    valores = arquivo.readlines()
    x = []
    y = []
    for v in valores:
        v = re.sub(ur'\s+',';', v.strip())
        v = re.search(ur'(.*);(.*)', v)
        x.append(v.group(1))
        y.append(v.group(2))
    print x
    print y
    p.figure(1)
    p.plot( x, y,"--", color='black')
    p.xlabel('Passos')
    p.ylabel('Valor encontrado')
    p.grid()
    #p.ylim([0,5])
    #p.xlim([1,1.55])
    p.title('Euler Modificado')
#     p.savefig('euler_modificado_01.pdf')
    p.show()   