
#COMIENZA LAS DEFINICIONES DE FUNCIONES

####################################
def create_cost_str_wd_time(n,cota,time):
    #Esta funcion inicia el algoritmo e impone en la primera rama el corte al tiempo "time"
    strv="";
    #Utilizamos diccionarios globales ya que los utilizaran todas las funciones
    global costedic;
    global strdic;
    global reversed_prime;
    global reversed_prime_lite20;
    global reversed_prime_lite15;
    global reversed_prime_lite10;
    global reversed_prime_lite5;
    #Si ya tenemos calculado el valor lo saca directamente
    if n in costedic:
        return costedic[n],strdic[n];
    else:
        min = cota;
        if (n < 10000):
            lista=reversed_prime; #El numero es pequeno, prueba con todos los primos
        #elif (n<100000):#100000
        #    lista=reversed_prime_lite20; #Si se quiere refinar se pueden estudiar estos valores simulando muchos
        #elif (n<1000000):#1000000        #casos aleatorios y ajustando los valores
        #    lista=reversed_prime_lite20;
        elif (n<10000000):#10000000
            lista=reversed_prime_lite20; #El numero es medio, prueba con 20 primos
        else:
            lista=reversed_prime_lite10; #El numero es grande, prueba con pocos primos
        for p in lista:
                a = n % p; #Hallamos lo que debemos restarle a n para que sea multiplo de p
                if(a in costedic): #Si a no esta en el diccionario no lo barajamos como opcion (alto coste)
                    ctemp = costedic[a] + costedic[p]; #Cuanto nos costaria esta operacion.
                    if min - ctemp >=0:
                        n1 = (n-a)//p; #Reduccion del coste
                        if n1 != 1:
                            aux,str_n1 = create_cost_str_wd(n1,min-ctemp); #Llamamos recursivamente a la funcion. Esta vez sin limite de tiempo
                            ctemp += aux;                                  #debido a que son ramas mas bajas y van rapido.
                        else:
                            str_n1="";
                        if ctemp < min :
                            min= ctemp;
                            strv="("+str_n1+")*"+str(p); #Expresion escrita
                            if a!=0:#Si a=0 entonces tiene coste 0 y no hace falta meterlo
                                strv+="+"+strdic[a]; 
                                
                if((p-a) in costedic): #Probamos con el modulo superior. (Analogo)
                    ctemp = costedic[p-a] + costedic[p];         
                    if min - ctemp >=0:
                        n1 = (n-a)//p +1;
                        if n1 != 1:
                            (aux,str_n1) = create_cost_str_wd(n1,min-ctemp);
                            ctemp += aux;
                        else:
                            str_n1="";
                        if ctemp < min :
                            min= ctemp;
                            strv="("+str_n1+")*"+strdic[p];
                            if (p-a)!=0:
                                strv+="-"+strdic[p-a]; 
                            #print (p)
                if(time<datetime.datetime.now()): #Si gastamos mucho tiempo, devuelve la solucion que tengamos, nos vamos a otro caso.
                    print("LIMITE DE TIEMPO POR CASO EXCEDIDO. ABORTAMOS!");
                    break;
    if(min!=cota): #Esto en realidad aqui no es necesario pero se anade por analogia. Ver explicacion en la siguiente funcion.
        costedic[n]=min;
        strdic[n]=strv;
    return min,strv;
##########################################
def create_cost_str_wd(n,cota):
    #Esta funcion continua el algoritmo recursivamente sin considerar limite de tiempo.
    #Todo es analogo a la anterior. No la comentamos.
    strv="";
    global costedic;
    global strdic;
    global reversed_prime;
    global reversed_prime_lite20;
    global reversed_prime_lite15;
    global reversed_prime_lite10;
    global reversed_prime_lite5;
    if n in costedic:
        return costedic[n],strdic[n];
    else:
        min = cota;
        if (n < 10000):
            lista=reversed_prime;
        elif (n<100000):#100000
            lista=reversed_prime_lite20;
        elif (n<1000000):#1000000
            lista=reversed_prime_lite20;
        elif (n<10000000):#10000000
            lista=reversed_prime_lite20;
        else:
            lista=reversed_prime_lite10; 
        for p in lista:
                a = n % p;
                if(a in costedic):
                    ctemp = costedic[a] + costedic[p];
                    if min - ctemp >=0:
                        n1 = (n-a)//p;
                        if n1 != 1:
                            aux,str_n1 = create_cost_str_wd(n1,min-ctemp);
                            ctemp += aux;
                        else:
                            str_n1="";
                        if ctemp < min :
                            min= ctemp;
                            strv="("+str_n1+")*"+str(p);
                            if a!=0:
                                strv+="+"+strdic[a]; 

                if((p-a) in costedic):
                    ctemp = costedic[p-a] + costedic[p];         
                    if min - ctemp >=0:
                        n1 = (n-a)//p +1;
                        if n1 != 1:
                            (aux,str_n1) = create_cost_str_wd(n1,min-ctemp);
                            ctemp += aux;
                        else:
                            str_n1="";
                        if ctemp < min :
                            min= ctemp;
                            strv="("+str_n1+")*"+strdic[p];
                            if (p-a)!=0:
                                strv+="-"+strdic[p-a]; 

    if(min!=cota): #Si hemos obtenido una solucion optima, debemos guardarla. Asi si se vuelve a intentar calcular en una subrama no la calculamos de nuevo.
        costedic[n]=min;
        strdic[n]=strv;
    return min,strv;
##################################################
def casidef(n,cota,quitap,t):
    #Solucionador del problema
    ahora=datetime.datetime.now();
    #time sera el tiempo en el cual como maximo ha debido de terminar nuestra funcion.
    time=ahora+datetime.timedelta(0,t);
    #Los diccionarios son globales. Las funciones recursivas deben acceder a ellos continuamente.
    global prime;
    global reversed_prime;
    global costedic;
    global strdic;
    global reversed_prime_lite20;
    global reversed_prime_lite15;
    global reversed_prime_lite10;
    global reversed_prime_lite5;
    #En cada caso debemos inicializar nuestro diccionario, eliminando el primo que toque.
    tprime = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
    index=0;
    for i in range(0,25): #Observacion. 1 no es primo y por tanto no nos lo quitaran.
        if tprime[i]==quitap:
            index=i;
    prime=np.delete(tprime,index); #Eliminamos el primo

    reversed_prime = prime[::-1] #Es mejor iterar los primos de mayor a menor, para dividir y hacer el numero lo mas pequeno al principio, para bajar a cota.
    costedic={}
    strdic={}
    costedic[0]=0; #El 0 no tiene coste
    strdic[0]="";
    costedic[1]=1; #El 1 siempre tiene coste 1
    strdic[1]="1";
    for p in prime:
        costedic[p]=1;
        strdic[p]=str(p);
    #Anadimos numeros pequenos basicos a nuestro diccionario
    for p in prime:
        for q in prime:
            if((not (p+q) in costedic)):
                costedic[p+q]=2;
                strdic[p+q]="("+str(p)+"+"+str(q)+")";
            if((not (p-q) in costedic) and (p-q)>0):
                costedic[p-q]=2;
                strdic[p-q]="("+str(p)+"-"+str(q)+")";
            if((not (p*q) in costedic)):
                costedic[p*q]=2;
                strdic[p*q]="("+str(p)+"*"+str(q)+")";
    #Con esto nos aseguramos que casi todos los restos modulo 97 esten en el diccionario
    #Por ultimo anadimos las sumas de tres primos
    for p in prime:
        for q in prime:
            for r in prime:
                if((not (p+q+r) in costedic)):
                    costedic[p+q+r]=3;
                    strdic[p+q+r]="("+str(p)+"+"+str(q)+"+"+str(r)+")";
    #Anadimos estos numeros porque el coste computacional es muy bajo y son muy escurridizos para nuestro algoritmo. Al ser impares no se podran obtener como
    #p1*p2+p3 con los tres primos distintos de 2. Esto puede ocurrir en numeros mas altos pero es mucho mas improbable!
    reversed_prime_lite5=reversed_prime[0:5:1] #Lista de primos recortadas, para iterar menos si el numero es muy grande.
    reversed_prime_lite10=reversed_prime[0:10:1]
    reversed_prime_lite15=reversed_prime[0:15:1]
    reversed_prime_lite20=reversed_prime[0:20:1]
    strv="";
    return create_cost_str_wd_time(n,cota,time);#Obten la solucion.
########################################################
#COMIENZA EL SCRIPT:

import datetime
import numpy as np
ahora=datetime.datetime.now();
fhout = open('SCORE.txt','w')
ok=0; #Para saltarnos la primera linea del archivo
fhout.write(ahora.strftime("%Y-%m-%d-%H:%M:%S.%f")[:24]); #El formato exacto es ese
fhout.write("\n");
with open('TEST.txt') as f:
   for line in f:
        if(ok==1):
            #print(line); #Muestra el caso por el que va
            line_split = line.split('|')
            id = line_split[0]
            number = int(line_split[1])
            pe = int(line_split[2])
            #Resolvemos el problema
            (sol,str_sol)=casidef(number,100,pe,3); #Como maximo admitimos 3s por caso
            #Escribimos la solucion
            fhout.write("11869945J|"+id+"|"+str(sol)+"|"+str_sol+"\n")
        else:
            ok=1;
luego=datetime.datetime.now();
fhout.write(luego.strftime("%Y-%m-%d-%H:%M:%S.%f")[:24]); #El formato exacto es ese
fhout.close()
print(luego-ahora); #Imprime el tiempo utilizado

#FIN DEL SCRIPT