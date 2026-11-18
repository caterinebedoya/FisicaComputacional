import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from tarea_1 import particulas


if __name__=="__main__":

    def trayectoria(particula_1, particula_2, campo,tiempo,dt):

        posicion_1 = []
        velocidad_1 =[]
        aceleracion_1 =[]


        posicion_2 = []
        velocidad_2 =[]
        aceleracion_2 = []
        
        #arreglos por componentes para la partícula 1

        aceleracionx_1=[]
        aceleraciony_1=[]
        aceleracionz_1=[]

        velocidadx_1=[]
        velocidady_1=[]
        velocidadz_1=[]

        posicionx_1=[]
        posiciony_1=[]
        posicionz_1=[]

        #arreglos por componentes para la partícula 2

        aceleracionx_2=[]
        aceleraciony_2=[]
        aceleracionz_2=[]

        velocidadx_2=[]
        velocidady_2=[]
        velocidadz_2=[]

        posicionx_2=[]
        posiciony_2=[]
        posicionz_2=[]
    
        for i in tiempo:

            if i==0:
                posicion_1.append(particula_1.posicion.copy())
                posicionx_1.append(particula_1.posicion[0].copy())
                posiciony_1.append(particula_1.posicion[1].copy())
                posicionz_1.append(particula_1.posicion[2].copy())
                
                posicion_2.append(particula_2.posicion.copy())
                posicionx_2.append(particula_2.posicion[0].copy())
                posiciony_2.append(particula_2.posicion[1].copy())
                posicionz_2.append(particula_2.posicion[2].copy())

                velocidad_1.append(particula_1.velocidad.copy())
                velocidadx_1.append(particula_1.velocidad[0].copy())
                velocidady_1.append(particula_1.velocidad[1].copy())
                velocidadz_1.append(particula_1.velocidad[2].copy())

                velocidad_2.append(particula_2.velocidad.copy())
                velocidadx_2.append(particula_2.velocidad[0].copy())
                velocidady_2.append(particula_2.velocidad[1].copy())
                velocidadz_2.append(particula_2.velocidad[2].copy())

                aceleracion_1.append(np.array([0,0,0]))
                aceleracionx_1.append(0)
                aceleraciony_1.append(0)
                aceleracionz_1.append(0)
                
                aceleracion_2.append(np.array([0,0,0]))
                aceleracionx_2.append(0)
                aceleraciony_2.append(0)
                aceleracionz_2.append(0)

            else:

                particula_1.aceleraciones(campo,particula_2)
                particula_2.aceleraciones(campo,particula_1)
                particula_1.velocidades(dt)
                particula_2.velocidades(dt)
                particula_1.posiciones(dt)
                particula_2.posiciones(dt)

                aceleracion_1.append(particula_1.aceleracion.copy())
                aceleracionx_1.append(particula_1.aceleracion[0].copy())
                aceleraciony_1.append(particula_1.aceleracion[1].copy())
                aceleracionz_1.append(particula_1.aceleracion[2].copy())

                aceleracion_2.append(particula_2.aceleracion.copy())
                aceleracionx_2.append(particula_2.aceleracion[0].copy())
                aceleraciony_2.append(particula_2.aceleracion[1].copy())
                aceleracionz_2.append(particula_2.aceleracion[2].copy())

                velocidad_1.append(particula_1.velocidad.copy())
                velocidadx_1.append(particula_1.velocidad[0].copy())
                velocidady_1.append(particula_1.velocidad[1].copy())
                velocidadz_1.append(particula_1.velocidad[2].copy())

                velocidad_2.append(particula_2.velocidad.copy())
                velocidadx_2.append(particula_2.velocidad[0].copy())
                velocidady_2.append(particula_2.velocidad[1].copy())
                velocidadz_2.append(particula_2.velocidad[2].copy())

                posicion_1.append(particula_1.posicion.copy())
                posicionx_1.append(particula_1.posicion[0].copy())
                posiciony_1.append(particula_1.posicion[1].copy())
                posicionz_1.append(particula_1.posicion[2].copy())

                posicion_2.append(particula_2.posicion.copy())
                posicionx_2.append(particula_2.posicion[0].copy())
                posiciony_2.append(particula_2.posicion[1].copy())
                posicionz_2.append(particula_2.posicion[2].copy())
        
        velocidad_1 = np.array(velocidad_1)
        posicion_1 = np.array(posicion_1)
        aceleracion_1 = np.array(aceleracion_1)

        velocidad_2 = np.array(velocidad_2)
        posicion_2 = np.array(posicion_2)
        aceleracion_2 = np.array(aceleracion_2)
       
        data_sets1 = [(aceleracionx_1),(aceleraciony_1),(aceleracionz_1),
        (velocidadx_1),(velocidady_1),(velocidadz_1),
        (posicionx_1),(posiciony_1),(posicionz_1)]

        data_sets2 = [(aceleracionx_2),(aceleraciony_2),(aceleracionz_2),
        (velocidadx_2),(velocidady_2),(velocidadz_2),
        (posicionx_2),(posiciony_2),(posicionz_2)]

        graficadora_multiple(tiempo, data_sets1, "Gráficas para el electrón")
        graficadora_multiple(tiempo, data_sets2, "Gráficas para el protón")


        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(posicion_1[:, 0], posicion_1[:, 1], posicion_1[:, 2], label='Electrón')
        ax.plot(posicion_2[:, 0], posicion_2[:, 1], posicion_2[:, 2], label='Protón')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()
        plt.show()
        print(posicion_1)


    def graficadora_multiple(tiempo_array, data_sets, title): #recibe un arrreglo de tiempos como primer argumento
                                                          #como segundo argumento recibe array con los conjuntos de datos por componentes de las magnitudes físicas estudiadas para cada partícula (aceleración, velocidad, posición, en x, y, z)
                                                          #como tercer argumento un titulo (str) que quiera darse al conjunto de gráficas
        fig, axs = plt.subplots(3, 3, figsize=(10, 10))  # Crear una figura con 3 filas y 3 columnas de subgráficas
        plt.suptitle(title, fontsize=16, fontweight='bold')

        indices=["x","y","z"]
        variables=["aceleración", "velocidad", "posición"]

        for i in range(3):  #Iterar sobre las filas
            for j in range(3):  #Iterar sobre las columnas
                index = i * 3 + j  # Calcular el índice correspondiente al par de datos actual
                y_data = data_sets[index]  # Obtener los datos para la gráfica actual
                axs[i, j].plot(tiempo_array, y_data)  # Dibujar en la subgráfica actual
                axs[i, j].set_title(f'Gráfica {variables[i]} {indices[j]}')
                axs[i, j].set_xlabel("tiempo (s)")
                axs[i, j].set_ylabel(f"{variables[i]} (a.u)")
                plt.tight_layout()



    masa1 = 1 #9.109e-31 
    carga1 = -1 #.602e-19  
    x1_i = [0,0,0]
    v1_i = [2, 2, 0]

    masa2 = 1 #.673e-27
    carga2 = 1 #.602e-19 
    x2_i = [2,2,0]
    v2_i = [-2, 2, 0]


    campo = [0,0,1.]
    dt = 0.3

    particula_1 = particulas(masa1, carga1, x1_i, v1_i)
    particula_2 = particulas(masa2, carga2, x2_i, v2_i)

    tiempo = np.arange(0, 50, dt)
    trayectoria(particula_1,particula_2,campo,tiempo,dt)

