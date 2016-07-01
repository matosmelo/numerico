from pylab import *
import csv

if __name__ == '__main__':
    valores_x = []
    valores_y = []
    # Pega os valores de um arquivo csv separado por colunas
    with open('grafico.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            valores_x = append(valores_x, row[0])
            valores_y = append(valores_y, row[1])
    
    #Gera a imagem
    figure(1)
    title(r'Halley')
    plot(valores_x, valores_y, color='black')
    grid(True)
    xlabel('x (UA)')
    ylabel('y (UA)')
    centerx = 0.
    centery = 0.
    plot(centerx, centery, 'ko')
    axis('equal')
    savefig('halley.pdf')
    show()