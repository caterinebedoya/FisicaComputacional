import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from codigo import graficador

if __name__=="__main__":

# Definimos la función de dos variables usando NumPy
    def func(x, y):
        return x**2 * y + 0.5 * x**2 - y**3 / 3 + 0.5 * y**2

# Función para leer el archivo y graficar los datos
    def plot_poincare_map(filename,E):
        # Leer el archivo de texto
        data = np.loadtxt(filename)
        
        # Asumimos que los datos están en dos columnas
        y = data[:, 0]
        py = data[:, 1]
        
        # Crear la gráfica
        plt.figure(figsize=(8, 8))
        plt.plot(y, py, 'b.', markersize=2)
        
        # Configurar etiquetas y título
        plt.xlabel(r'$y$', fontsize=14)
        plt.ylabel(r'$py$', fontsize=14)
        plt.title(rf'Mapa de Poincaré para $E={E}$', fontsize=16)
        
        # Configurar límites de los ejes

        
        # Mostrar la gráfica
        plt.grid(True)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

        
    # Creamos una instancia 
    grapher = graficador(func)

    # Mostramos las gráficas
    grapher.show_plots()
    # Llamar a la función con el nombre del archivo
    plot_poincare_map('poincare_11.dat',"1/11")
    plot_poincare_map('poincare_10.dat',"1/10")
    plot_poincare_map('poincare_9.dat',"1/9")
    plot_poincare_map('poincare_8.dat',"1/8")
    plot_poincare_map('poincare_7.dat',"1/7")
    plot_poincare_map('poincare_6.dat',"1/6")