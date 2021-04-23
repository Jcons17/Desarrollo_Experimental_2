
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import random
from scipy.spatial import distance
import os
import time 


# Creamos la clase Arreglo 2D aleatorio con margenes. Esta clase nos creara una configuración inicial aleatoria con margenes de n* densidad y de N particulas. Esta clase tiene varios métodos o funciones que definiran al objeto que estamos programando.
# 
# - Init: El método init es la funcion que se correra automaticamente cuando iniciames la clase. Consta de pedirnos los parametros n* y N.
# 
# 
# - L: Nos calcula la longitud de la celda con la formula: $$ L = \sqrt{ \dfrac{N}{n^*} } $$
# 
# 
# - r: Nos calcula el radio de las particulas con la formula:  $$ r = \sqrt{ \dfrac{n^*}{2}} $$
# 
# 
# - new_point: Nos genera un nuevo punto que este dentro de los margenes de la celda. Para eso se tiene que generar un numero tomando en cuanto el largo de la longitud y multiplicarla por $1- \dfrac{2r}{l}$ ya que esta generara un punto que no sobrepasara los extremos de la caja.
# 
# 
# - array: Este es el metodo que generara las N particulas aleatorias en la caja sin traslapes. Primero genero un punto nuevo y lo guardo en una lista. Se crea un ciclo que vaya hasta las N particulas, se genera un nuevo punto con la función new_point y se guarda en la lista creada anteriormente. Despues se crea otro ciclo que vaya hasta donde termine el contador de la función anterior, esto servira para comparar la distancia de la particula nueva con las generadas anteriormente. Si la distancia es mayor al diametro $2r$ de las particulas entonces que no haga nada pero si es menor, que elimine el ultimo punto de la lista y le reste al contador del ciclo. Por ultimo que me devuelva la lista generada.   
# 
# 
# - graph: Esta función nos permitira gráficar las N particulas. En esta función solo se guardaran las graficas.
# 
# 
# - graph_show: Esta función tambien nos permite gráficar las N particulas. Pero aquí si se mostraran en la terminal.

# In[2]:


class arreglo2D_aleatorio_cm:
    def __init__(self,n,N):
        self.n=n
        self.N=N
        self.data=self.array()
        self.large = self.L()

    def L(self):
        return (self.N/self.n)**(1/2)

    def r(self):
        return float(np.sqrt(self.n)/2)
    
    def new_point(self):
        x=self.L()*(1-2*self.r()/self.L())*(random.random() - 1/2)
        y=self.L()*(1-2*self.r()/self.L())*(random.random() - 1/2)
        return (x,y)

    def array(self):
        
        Dat=[self.new_point()]
        
        i=0
        while len(Dat)<self.N:
            i = i+1
            x=self.L()*(1-2*self.r()/self.L())*(random.random() - 1/2)
            y=self.L()*(1-2*self.r()/self.L())*(random.random() - 1/2)
            Par=(x,y)
            Dat.append(Par)
            for j in range(1,i+1):
                distancia=distance.euclidean(Par,Dat[i-j])
                if distancia < 2*self.r():
                    Dat.pop()
                    i=i-1
                    break
        return Dat

    def graph(self,data,title,size,c,contador,trazadora):
        color_pre=c
        plt.ioff()
        fig, ax = plt.subplots(figsize=(size,size))
        plt.xlim(-self.L()/2,self.L()/2)
        plt.ylim(-self.L()/2,self.L()/2)
        plt.grid(linestyle='--')
        ax.set_aspect(1)
        for i in range(0,len(data)):
            if i == trazadora:
                c="r"
            else:    
                c=color_pre
            circle1 = plt.Circle(data[i], self.r(), color=c)
            ax.add_artist(circle1)
            #ax.annotate(str(i), xy=data[i], fontsize=8)

        plt.title(title, fontsize=16)
        plt.savefig("./image/" + str(contador) + ".png")
        plt.close(fig)
        
    def graph_show(self,data,title):
        plt.ion()
        fig, ax = plt.subplots(figsize=(5,5))
        plt.xlim(-self.L()/2,self.L()/2)
        plt.ylim(-self.L()/2,self.L()/2)
        plt.grid(linestyle='--')
        ax.set_aspect(1)
        for i in range(0,len(data)):
            circle1 = plt.Circle(data[i], self.r(), color="r")
            ax.add_artist(circle1)
            #ax.annotate(str(i), xy=data[i], fontsize=8)

        plt.title(title, fontsize=16)
        plt.show
    
   


#Esta clase Arreglo 2D aleatorio sin margenes hereda todos los metodos de la clase anterior (arreglo2D_aleatorio_cm), su unica excepción con la anterior es que en el metodo array los puntos se generan sin margenes, lo que resulta en que las particulas en la configuración inicial puedan estar en una parte afuera de los margenes de la celda.

# In[3]:


class arreglo2D_aleatorio_sm(arreglo2D_aleatorio_cm):
    def array(self):
         
        Dat=[( self.L()*(random.random() - 1/2) , self.L()*(random.random() - 1/2))]
        i=0
        while len(Dat)<self.N:
            i = i+1
            x=self.L()*(random.random() - 1/2)
            y=self.L()*(random.random() - 1/2)
            Par=(x,y)
            Dat.append(Par)
            for j in range(1,i+1):
                distancia=distance.euclidean(Par,Dat[i-j])
                if distancia < 2 * self.r():
                    Dat.pop()
                    i=i-1
                    break
        return Dat


# Este arreglo tambien hereda todos los metodos de las clases anteriores, solamente que en esta clase el metodo array se cambia para generar una configuración inicial cuadrada donde los puntos estan equidistantes uno del otro. 

# In[4]:


class arreglo2D_cuadrado(arreglo2D_aleatorio_cm):
    def array(self):
        i=0
        x=[]
        Nfinal = int(round(np.sqrt(self.N),0))
        for i in range(Nfinal):
            x.append(-self.L()/2+2*self.r()/2  +i*self.L()/(Nfinal))
        p=set([(i, j) for i in x for j in x])
        dat = list(p)
        return dat


# Aquí generamos una nueva clase Montecarlo 2D. Esta se encargara de mover las particulas aleatoriamente y de que no se traslapen. Hereda tambien algunos metodos de arreglo2D_aleatorio_cm, y algunos que agrega el son:
# 
# - mod_pot: Esta es la función de potencial para esferas duras. 
# 
# 
# - sumaup: Es la suma de energía potencial de toda una configuración.
# 
# 
# - UP: es la comparación de de energía potencial de la particula iesima con todas las otras partículas de su configuración. 
# 
# 
# - algoritmo: En este metodo se crea el algoritmo de montecarlo para mover a las particulas de una configuración a otra. Para eso, leemos otros dos nuevos parametro. NSTEP que nos dice cuantas configuraciones habra y RMAX que nos dice cuantas unidades de su radio se pueden mover.
# 
# 
# - Trazadora: Nos permite tener en una lista de los puntos en los cuales la particula trazadora estaba.
# 
# 
# - graph_traz: Nos permite graficar la trayectoria que tomen las particula que escogemos. 
# 
# 
# - animación: Nos permite crear una animación con todas las configuraciónes de las particulas. 
# 
# 
# - Display_gif: Nos permite mostrar la animación que creamos anteriormente. 
# 
# 
# 
# 
# 
# 
# 

# In[5]:



class montecarlo2D(arreglo2D_aleatorio_cm):

    def mod_pot(self, distancia):
        if distancia < self.large/2 and distancia < 2*self.r():
            V =  1e10
        else:
            V = 0
        return V

    def energia3d(self,x,y, rxi, ryi, j):
        V = 0.
        N = self.N
        L = self.L()
        for i in range(N):
            if j != i:
                rxij = rxi - x[i]
                ryij = ryi - y[i]
                #condición de imagen mínima
                rxij = rxij - L * round(rxij/L)
                ryij = ryij - L * round(ryij/L)
                rijsq = np.sqrt(rxij*rxij + ryij*ryij)
                Vij = self.mod_pot(rijsq)
                V = V + Vij
        return V

    def sumaup(self,data):
        V = 0
        i=1
        m=0
        while i<len(data):
            for j in range(0,i):
                ri=np.array(data[i])
                rj=np.array(data[j])
                ri = ri - self.large*np.round(ri/self.large)
                rj = rj - self.large*np.round(rj/self.large)
                rij= ri - rj  
                distancia=np.linalg.norm(rij)
                Vij = self.mod_pot(distancia)
                V = V + Vij
            i = i+1           
        return V

    def algoritmo(self,x, y, nStep, drMax, iRatio, iPrint, cc, V, iTraza, Vlrc, nener):
        import random as rd
        N = self.N
        L = self.L()
        rCut = L/2
        
        acatma = 0.
        ki2 = 0
        xTraza = np.zeros(nStep)
        yTraza = np.zeros(nStep)
        zTraza = np.zeros(nStep)
        vTraza = np.zeros(nStep)

        Cx = np.zeros((N, nStep))
        Cy = np.zeros((N, nStep))

        #vTraza[0] = V
        #Vn = np.zeros(nStep+1)
        #Vn[0] = V

        for i in range(nStep):
            for j in range(N):
                xOld = x[j]
                yOld = y[j]

                Vold = self.energia3d(x,y,xOld, yOld, j)
                xNew = xOld + ((2.*rd.uniform(0,1) - 1.) *drMax)
                yNew = yOld + ((2.*rd.uniform(0,1) - 1.) *drMax)

                #condición de imagen mínima
                xNew = xNew - L * round(xNew/L)
                yNew = yNew - L * round(yNew/L)

                Vnew = self.energia3d(x,y,xNew, yNew, j)


                dV = Vnew - Vold

                if dV < 75.:
                    if dV <= 0. :
                        V = V + dV
                        x[j] = xNew
                        y[j] = yNew
                        acatma = acatma + 1
                    elif np.exp(-dV) > rd.uniform(0,1):
                        V = V + dV
                        x[j] = xNew
                        y[j] = yNew

                        acatma = acatma + 1.
                        
                if i > nener:
                    Cx[j][ki2] = x[j]
                    Cy[j][ki2] = y[j]

                if j==iTraza:
                    xTraza[i] = xNew
                    yTraza[i] = yNew

            Vn = (V + Vlrc)/float(N)


            if i % iRatio == 0:
                ratio = acatma/float((N*iRatio))

                if ratio > cc:
                    drMax = drMax*1.05
                else:
                    drMax = drMax*0.95
                acatma = 0.

            if i % iPrint == 0:
                print("Se han traslapdo ",acatma, " veces en la configuracion",i)
            vTraza[i] = Vn

            if i > nener:
                ki2 = ki2 + 1
            #    for k in range(N):
            #        Cx[k, ki2] = x[k]
            #        Cy[k, ki2] = y[k]
            #        Cz[k, ki2] = z[k]


        return x, y, xTraza, yTraza, vTraza, Cx, Cy, ki2

    def trazadora(self,data,rand):
        k=0
        i=0
        NSTEP=len(data)
        N=len(data[1])
        Path_traz=[]

        for k in range(NSTEP):
            for i in range(N):
                if i==rand:
                    Path_traz.append(data[k][i])

        return Path_traz

    def graph_traz(self,data):
        fig, ax = plt.subplots(figsize=(10,10))
        plt.ioff()
        plt.xlim(-self.L()/2,self.L()/2)
        plt.ylim(-self.L()/2,self.L()/2)
        plt.grid(linestyle='--')
        ax.set_aspect(1)
        for i in range(0,len(data)):
            c=((1,i/len(data),np.exp(-0.8*i/(len(data))),1))
            circle1 = plt.Circle(data[i], self.r()/10, color=c)
            ax.add_artist(circle1)
            #ax.annotate(str(i), xy=data[i], fontsize=8)

        plt.title("Trayectoria partícula trazadora", fontsize=16)
        plt.show()
        plt.close(fig)
        
    def animacion(self,data):
        
        for r in  range(len(data)):
            self.graph(data[r],str(r)+".png",10,"b",r,N_trazadora) 
        
        import glob
        from PIL import Image
        import os

        fp_in = "./image/*.png"
        fp_out = "simulacion_N="+str(self.N)+"_n="+str(self.n)+"_NSTEP="+str(NSTEP)+"_DMAX="+str(DMAX)+".gif"

        img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in), key=os.path.getmtime)]
        img.save(fp=fp_out, format='GIF', append_images=imgs,
                 save_all=True, duration=1000/24, loop=0)
        
        return fp_out
    
    def display_gif(self,fn):
        from IPython import display
        return display.HTML('<img src="{}">'.format(fn))
            

        
