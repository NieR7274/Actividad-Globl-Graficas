#Importamos las librerías necesarias:
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec  

#Definimos las funciones de activación:

def Identidad(x):
    return x

def BinaryStep(x):
    if x < 0:
        fx = 0
    else:
        fx = 1
    return fx

def sigmoide(x):
    return 1/(1+ np.exp(-x))

def tanh(x):
    return np.tanh(x)

def ArcTanH(x):
    return np.arctanh(x)

def ReLU(x):
    if x<=0:
        fx = 0
    else:
        fx = x
    return fx

def PReLU(a,x):
    if x < 0:
        fx = a*x
    else:
        fx = x
    return fx

def ELU(a,x):
    if x < 0:
        fx = a*(np.exp(x) - 1)
    else:
        fx = x
    return fx

def softplus(x):
    return np.log(1 + np.exp(x))


x = np.linspace(-10,10,500)
x1 = np.linspace(-1,1,100)[1:-1]

#Definimos una figura que contendrá 9 gráficas en un arreglo de 3x3:
fig = plt.figure(tight_layout=True)
gs = gridspec.GridSpec(3, 3)

#Grafica de la función identidad
ax = fig.add_subplot(gs[0, 0])
ax.set_title("Función identidad")
ax.plot(x,Identidad(x), color='red', label='$I(x)$')
ax.set_ylabel('$f(x)$')
ax.set_xlabel('$x$')
ax.legend()
ax.grid()

#Grafica de la función paso binario
ax = fig.add_subplot(gs[0, 1])
ax.set_title("Paso binario")
ax.plot(x,[BinaryStep(i) for i in x], color='coral', label='$BinaryStep(x)$')
ax.set_ylabel('$f(x)$')
ax.set_xlabel('$x$')
ax.legend()
ax.grid()

#Grafica de la función sigmoide
ax = fig.add_subplot(gs[0, 2])
ax.set_title("Función sigmoide")
ax.plot(x,sigmoide(x), color='hotpink', label='$sigmoide(x)$')
ax.set_ylabel('$f(x)$')
ax.set_xlabel('$x$')
ax.legend()
ax.grid()

#Grafica de la función tangente hiperbólica
ax = fig.add_subplot(gs[1, 0])
ax.set_title("Función tangente hiperbólica")
ax.plot(x,tanh(x), color='orange', label='$tanh(x)$')
ax.set_ylabel('$f(x)$')
ax.set_xlabel('$x$')
ax.legend()
ax.grid()

#Grafica de la función arcotangente hiperbólica
ax = fig.add_subplot(gs[1, 1])
ax.set_title("Función arcotangente hiperbólica")
ax.plot(x1,ArcTanH(x1), color='cyan', label='$arctanh(x)$')
ax.set_ylabel('$f(x)$')
ax.set_xlabel('$x$')
ax.legend()
ax.grid()

#Grafica de la función ReLU
ax = fig.add_subplot(gs[1, 2])
ax.set_title("Función ReLU")
ax.plot(x,[ReLU(i) for i in x], color='green', label='$ReLU(x)$')
ax.set_ylabel('$f(x)$')
ax.set_xlabel('$x$')
ax.legend()
ax.grid()

#Grafica de la función PReLU
ax = fig.add_subplot(gs[2, 0])
ax.set_title("Función PReLU")
ax.plot(x,[PReLU(4,i) for i in x], color='purple', label='$PReLU(x)$')
ax.set_ylabel('$f(x)$')
ax.set_xlabel('$x$')
ax.legend()
ax.grid()

#Grafica de la función ELU
ax = fig.add_subplot(gs[2, 1])
ax.set_title("Función ELU")
ax.plot(x,[ELU(4,i) for i in x], color='deepskyblue', label='$ELU(x)$')
ax.set_ylabel('$f(x)$')
ax.set_xlabel('$x$')
ax.legend()
ax.grid()

#Grafica de la función softplus
ax = fig.add_subplot(gs[2, 2])
ax.set_title("Función softplus")
ax.plot(x,softplus(x), color='magenta', label='$softplus(x)$')
ax.set_ylabel('$f(x)$')
ax.set_xlabel('$x$')
ax.legend()
ax.grid()


fig.align_labels()  # same as fig.align_xlabels(); fig.align_ylabels()
plt.show()  #Mostramos la figura con las gráficas