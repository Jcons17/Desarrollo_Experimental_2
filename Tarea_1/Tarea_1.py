#!/usr/bin/env python
# coding: utf-8

# <center>
# 
# # Tarea 1
# ### Desarrollo Experimental 2
# ### Julio Cesar Cons Calderón
# </center>
# 

# #### Objetivos
# 
# Realizar  rutinas (seguir  protocolos) para  comprobar  el  buen  estado  inicial  del  equipo  de cómputo, recordar  comandos  básicos,  revisión  de  edición,  graficación  y  compilación  en actividades específicas.

# ##### Actividad 0
# 
# 
# * Conectarse al servidor del centro de computo
# 
# 
# 
# 
# 
# ![title](1.png)
# 
# 
# 

# <li>Conectarse al servidor del centro de computo</li>
# <li>Crear el directorio DE2</li>
# <li>Cambiarse al directorio DE2 y generar otro directorio Tarea1</li>
# <li>Regresar al directorio raiz</li>
# <li>Salirse de la coneccion al servidor</li>
#   <img src="./2.png" width=600 height=800>
#     <img>  

# <li>Consultar  su  correo  institucional  y  guardar en  un  directorio  local los  archivos enviadospor el profesor</li>
# <li>Transferir el archivo del inciso anterior al directorio Tarea 1 generado en el servidor</li>
# <li>Salirse del protocolo de transferencia</li>
# 
#  <img src="./3.png" width=600 height=800>
#     <img>  

# <li>Volver a conectarse al servidor e ir al directorio Tarea 1</li>
# <li>Confirmar que el directorio contiene el archivo transferido</li>
# <li>Visualizar el contenido del archivo</li>
#  <img src="./5.png" width=600 height=800>
#     </img>  

# <li>Gráficar los archivos</li>
# <img src="./ei.png" width=400 height=600>
#     </img>  
# <img src="./ea.png" width=400 height=600>
#     </img>      

# ##### Actividad 1
# 

# Graficaremos la funcion:
# 
# $$
#  f(x)=e^\frac{-x^2}{2} $$

# ###### Pasos a seguir
# 

# 1. Importamos las librerias necesarias para la actividad. Seran tres librerias. 
# 
# * NumPy es una biblioteca para el lenguaje de programación Python que da soporte para crear vectores y matrices grandes multidimensionales, junto con una gran colección de funciones matemáticas de alto nivel para operar con ellas.
# 
# 
# * Pandas es una biblioteca de software escrita como extensión de NumPy para manipulación y análisis de datos para el lenguaje de programación Python. En particular, ofrece estructuras de datos y operaciones para manipular tablas numéricas y series temporales.
# 
# 
# * Matplotlib es una biblioteca para la generación de gráficos a partir de datos contenidos en listas o arrays en el lenguaje de programación Python y su extensión matemática NumPy.

# In[ ]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# 2. Definimos una función en Python. Se usara el comando def que nos define la función y como unico argumento sera x.

# In[ ]:


def funcion(x):
    f=np.exp(-x**2/2)
    return f


# 3. Asignamos valor de inicio y final al intervalo en el cual se va a graficar la función.

# In[ ]:


x0=-3
xf=3


# 4. Creamos un array $x$ que vaya desde el intervalo $[x_0,x_f]$ y tenga un step de 0.1. 
# 5. Despues creamos otro array que contenga los valores de la función valuado en cada valor del elemento $x$.
# 6. Metemos los arrays en un marco de datos que podamos exportar a un archivo txt.

# In[ ]:


x=np.arange(x0,xf,step=0.1)
y=[funcion(z) for z in x]
df=pd.DataFrame({"x":x,"f(x)":y})
df.to_csv("grafica.txt",index=None)


# 7. Leemos el archivo txt que habiamos exportado en el paso anterior y lo guardamos en un marco de datos llamado read.

# In[ ]:


read= pd.read_csv("grafica.txt")


# 8. Graficamos los datos guardados en el marco de datos read. Los graficamos en forma de puntos y continua.

# In[ ]:


plt.figure(figsize=([20,10]))
plt.plot(read["x"],read["f(x)"], 'ro')
plt.plot(read["x"],read["f(x)"], 'b')

plt.grid()
plt.show()


# ##### Actividad 2
# 

# Elaborar un programa para colocar N partículas (puntos) en una recta de longitud L, de forma tal que la distancia de separación entre ellas sea uniforme.
# 
# * Ejecutar su programa para N y L dadas por Usted.
# * Mostrar gráficamente la distribución de partículas (puntos) obtenida.

# ###### Pasos a seguir
# 1. Dar un valor para los $N$ puntos y para $L$ de longitud. 
# 2. Definir $x$ como un array.
# 3. Crear un ciclo que se repeti $N$ veces. En ese ciclo se le asignara un nuevo valor al array x. Ese nuevo valor ira creciendo $\frac{L}{N}$ veces cada ciclo, hasta completar los $N$ ciclos.
# 4. Crearemos un array $y$ que tenga la misma cardenalidad de x, solo que en cada entrada valdra 0.

# In[ ]:


L=10
N=10
i=0
x=[]
while i<N:
    x.append(i*L/(N-1))
    i = i+1

y = [_*0 for _ in x]


# 5. Graficaremos los valores de x. Lo haremos primero de forma discreta y despues de forma continua para simular la linea recta. 

# In[ ]:


plt.figure(figsize=([20,5]))
plt.plot(x, y, 'b')
plt.plot(x, y, 'ro')
plt.xticks(x, rotation=90)
plt.show()


# ##### Actividad 3 
# 
# Elaborar un programa para colocar partículas (puntos) en una superficie cuadrada de lado L, de forma tal que formen un arreglo cuadrangular.
# * Ejecutar su programa para $N$ y $L$ dadas por Usted. 
# * Mostrar gráficamente la distribución de partículas obtenida

# ##### Pasos a seguir
#  
# 1. Basicamente, el problema se basa en usar el mismo array pero aplicar el producto cartesiano a si mismo. Esto generará una pareja de pares que a cada valor del array $x$ le asignara cada valor del mismo array.
# 2. Para generar un producto cartesiano usamos el comando set para generar un conjunto de pares. Despues creamos dos ciclos donde a la primer valor del par le asignamos cada elemento del array $x$. El segundo ciclo le asigna al segundo valor del par un elemento del array $x$.

# In[ ]:


p=set([(z, y) for z in x for y in x])


# 3. Separamos el valor de los pares en dos arrays diferentes. Así, tendremos la facilidad de graficarlos.

# In[ ]:


x_val = [x[0] for x in p]
y_val = [x[1] for x in p]


# 4. Graficamos la cuadricula.

# In[ ]:


plt.figure(figsize=([20,20]))
plt.plot(x_val,y_val, 'ro')
plt.grid()
plt.xticks(x)
plt.yticks(x)
plt.show()


# ##### Observaciones finales:
# 
# Esta actividad fue muy ilustrativa. Mis conocimientos usando la consola de Unix es limitado pero las pocas lineas de comando que usé me ayudo a recordar algunos elementos de Fortran. Para mi, el Lenguaje Python junto con el IDE Jupyter Notebook, forman una excelente dupla a la hora de resolver problemas que no necesiten lineas de codigo extensas.  
# 
# 
