# void final ();
# void inicio (double *ti, double *t_final, double *n, double *y_inicial, double *precisao, double *k);
# double discretiza_dt (double ti, double t_final, double n);
# void imprime (double t, double y);
# void algoritmo_trapezios (double ti, double t_final, double dt, double y_inicial, double precisao, double k);
# double trapezios (double t_inicial, double t1, double ti, double t_final, double dt, double y_inicial, double precisao, double k);
# double aprox_suc (double chute, double a, double b, double c, double dt, double precisao, double k, double ti, double t_final);
# bool parada(int m, double x, double xant, double precisao, double k, double ti, double t_final, double a, double b, double c, double dt);
# bool criterio5(double k, int m, double ti, double t_final, double precisao);
# bool criterio4(double k, double x, double xant, double precisao);
# bool criterio3(double x, double precisao, double xant, double a, double b, double c, double dt);
# bool criterio2(double x, double xant, double precisao);
# bool criterio1(int m);
# double fi (double chute, double a, double b, double c, double dt);
# double g (double chute, double a, double b, double c, double dt);
# double dg (double chute, double a, double b, double c, double dt);



def final():
    print("O resultado foi salvo no arquivo saida.txt.\nFim do programa.\n");

#def inicio(double *ti, double *t_final, double *n, double *y_inicial, double *precisao, double *k):
#      arq = fopen("saida.txt","w");
#      fprintf(arq,"\n");
#      fclose(arq);
#     
     
     #coloque os parametros iniciais aqui:
#      *ti=
#      *t_final=
#      *n=
#      *y_inicial=
#      *precisao=
#      *k=0;
     #obs: precisao é para o metodo de newton. k = max |fi'| < 1, para aproximacoes sucessivas. nesse programa é usada a fi de newton, onde k = 0 para qualquer funcao g(x).



def discretiza_dt(double ti, double tf, double n):
       return ((t_final-ti)/n)

# def imprime (double t, double y):
#      FILE *arq;
#      arq = fopen("saida.txt","a");
#      fprintf(arq,"%.5f     %.5f\n",t,y);
#      fclose(arq);

def algoritmo_trapezios (double ti, double tf, double dt, double y0, double precisao, double k):
       
       double t_inicial=ti, t1=ti, y1;
       
       imprime(t_inicial,y_inicial);
       while (t1<t_final):
             t1=t_inicial+dt;
             //chute=yk+1, a=yk, b=tk, c=tk+1
             y1 = trapezios(t0,t1,ti,tf,dt,y0,precisao,k);
             imprime(t1,y1);
             t0=t1;
             y0=y1;

def trapezios (double t0, double t1, double ti, double tf, double dt, double y0, double precisao, double k):
       //chute=yk+1, a=yk, b=tk, c=tk+1
       return (aprox_suc(y0,y0,t0,t1,dt,precisao,k,ti,tf));

def aprox_suc (double chute, double a, double b, double c, double dt, double precisao, double k, double ti, double tf):
       double x, xant;
       int m=0;

       do {
          xant=chute;
          x = fi(chute,a,b,c,dt);
          chute = x;
          m++;
       }while (parada(m,x,xant,precisao,k,ti,tf,a,b,c,dt)==false);
       return x;
}

def parada(int m, double x, double xant, double precisao, double k, double ti, double tf, double a, double b, double c, double dt):
     // retire os comentarios // para desabilitar os criterios 4 e 5
     #if(criterio5(k,m,ti,t_final,precisao)==true)return true;
     #else if(criterio4(k,x,xant,precisao)==true)return true;
     #else         //            */
          if(criterio3(x,precisao,xant,a,b,c,dt)==true)return true;
     else if(criterio2(x,xant,precisao)==true)return true;
     else if (criterio1(m)==true)return true;
     else return false;
}

def criterio5(double k, int m, double ti, double tf, double precisao):
     if (((pow(k,m))*(fabs(tf-ti)))<=precisao):
        //printf("Parada: criterio 5.\n");
        return true;

     else return false;

def criterio4(double k, double x, double xant, double precisao):
     if (((k/(1-k))*(fabs(x-xant)))<=precisao):
        //printf("Parada: criterio 4.\n");
        return true;
     else return false;

def criterio3(double x, double precisao, double xant, double a, double b, double c, double dt):
     if (fabs(g(xant,a,b,c,dt))<=precisao):
        //printf("Parada: criterio 3.\n");
        return true;
     else return false;

def criterio2(double x, double xant, double precisao):
     if (fabs((x-xant)/x)<=precisao):
        //printf("Parada: criterio 2.\n");
        return true;
     else return false;

def criterio1(int m):
     if (m>=200) {
        //printf("Parada: criterio 1.\n");
        return true;
     else return false;

#OBS: os valores de y[k], y[k+1], t[k], t[k+1] foram trocados para facilitar a escrita das funcoes abaixo.
#chute=yk+1, a=yk, b=tk, c=tk+1

def fi (double chute, double a, double b, double c, double dt):
       #fi de Newton
       double x;
       x = chute - (g(chute,a,b,c,dt)/dg(chute,a,b,c,dt));
       return x;

def g (double chute, double a, double b, double c, double dt):
       double y;
       //chute=yk+1, a=yk, b=tk, c=tk+1
       y = //coloque aqui a funcao g(x). exemplo:(chute-a-((dt*(pow(M_E,b))*(pow(M_E,((-2)*a))))/2)-((dt*(pow(M_E,c))*(pow(M_E,((-2)*chute))))/2));
       return y;

def dg (double chute, double a, double b, double c, double dt):
       double y;
       #chute=yk+1, a=yk, b=tk, c=tk+1
       y = #coloque aqui a funcao g'(x). exemplo:(1+(dt*(pow(M_E,c))*(pow(M_E,(chute*(-2))))));
       return y;

if __name__ == '__main__':
    double ti, tf, dt, y0, precisao, k, n;
    
    inicio(&ti,&tf,&n,&y0,&precisao,&k);
    
    dt = discretiza_dt(ti,tf,n);
    
    algoritmo_trapezios (ti,tf,dt,y0,precisao,k);
    
    final();
    return 0;