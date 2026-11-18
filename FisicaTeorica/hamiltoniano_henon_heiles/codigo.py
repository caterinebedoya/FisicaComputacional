import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class graficador:
    def __init__(self, func, x_range=(-1, 1), y_range=(-1, 1), resolution=100):
        self.func = func
        self.x_range = x_range
        self.y_range = y_range
        self.resolution = resolution
        
        self.x_vals = np.linspace(self.x_range[0], self.x_range[1], self.resolution)
        self.y_vals = np.linspace(self.y_range[0], self.y_range[1], self.resolution)
        self.x_vals, self.y_vals = np.meshgrid(self.x_vals, self.y_vals)
        self.z_vals = self.func(self.x_vals, self.y_vals)

    def plot_3d(self, elev=30, azim=225):
        fig = plt.figure(figsize=(12, 6))
        ax1 = fig.add_subplot(121, projection='3d')
        surf = ax1.plot_surface(self.x_vals, self.y_vals, self.z_vals, cmap='hot')
        
        ax1.view_init(elev=elev, azim=azim)
        
        ax1.set_xlabel('x')
        ax1.set_ylabel('y')
        ax1.set_zlabel('z')
        ax1.set_title('Gráfica 3D del Potencial')  # Título de la gráfica 3D
        
        return fig, ax1
    
    def plot_contour(self, fig):
        ax2 = fig.add_subplot(122)
        contour = ax2.contourf(self.x_vals, self.y_vals, self.z_vals, 20, cmap='hot')
        fig.colorbar(contour, ax=ax2, shrink=0.5, aspect=5)
        
        ax2.set_xlabel('x')
        ax2.set_ylabel('y')
        ax2.set_title('Gráfica de Contorno')  # Título de la gráfica de contorno
        
        return ax2
    
    def show_plots(self):
        fig, ax1 = self.plot_3d()
        self.plot_contour(fig)
        plt.show()


d=2

class IntegradorSimplectico:
    def __init__(self, n, h, lambda_param, E0, num1, num2, tol, filename):
        self.n = n
        self.h = h
        self.lambda_param = lambda_param
        self.E0 = E0
        self.num1 = num1
        self.num2 = num2
        self.tol = tol
        self.filename = filename
        self.c1 = 1.0 / (2.0 * (2.0 - (2.0 ** (1.0 / 3.0))))
        self.c4 = self.c1
        self.c2 = (1.0 - 2.0 ** (1.0 / 3.0)) * self.c4
        self.c3 = self.c2
        self.d1 = 2.0 * self.c1
        self.d3 = self.d1
        self.d2 = -1.0 * (2.0 ** (1.0 / 3.0)) * self.d1
        self.d4 = 0.0

    def paso(self, x, p):
        for j in range(d):
            x[j] += self.h * self.c1 * p[j]

        p[0] -= self.h * self.d1 * (x[0] + 2.0 * self.lambda_param * x[0] * x[1])
        p[1] -= self.h * self.d1 * (x[1] + self.lambda_param * (x[0] ** 2 - x[1] ** 2))

        for j in range(d):
            x[j] += self.h * self.c2 * p[j]

        p[0] -= self.h * self.d2 * (x[0] + 2.0 * self.lambda_param * x[0] * x[1])
        p[1] -= self.h * self.d2 * (x[1] + self.lambda_param * (x[0] ** 2 - x[1] ** 2))

        for j in range(d):
            x[j] += self.h * self.c3 * p[j]

        p[0] -= self.h * self.d3 * (x[0] + 2.0 * self.lambda_param * x[0] * x[1])
        p[1] -= self.h * self.d3 * (x[1] + self.lambda_param * (x[0] ** 2 - x[1] ** 2))

        for j in range(d):
            x[j] += self.h * self.c4 * p[j]

        return x, p

    def ejecutar(self):
        with open(self.filename, "w") as f:
            for i in range(self.num1):
                for j in range(self.num2):
                    x0 = np.zeros(d)
                    p0 = np.zeros(d)
                    x0[0] = 0.0
                    x0[1] = -0.15 + 0.3 * (i / (self.num1 - 1.0))
                    p0[1] = -0.15 + 0.3 * (j / (self.num1 - 1.0))
                    p0[0] = np.sqrt(2.0 * self.E0 - p0[1] ** 2 - x0[1] ** 2 + (2.0 / 3.0) * x0[1] ** 3)

                    K = 0.5 * (p0[0] ** 2 + p0[1] ** 2)
                    V = 0.5 * (x0[0] ** 2 + x0[1] ** 2) + self.lambda_param * (x0[0] ** 2 * x0[1] - (1.0 / 3.0) * x0[1] ** 3)
                    H = K + V
                    print(f"bucle = ({i + 1}, {j + 1})\t{H}")

                    x, p = x0.copy(), p0.copy()
                    t = 0.0
                    for _ in range(self.n):
                        x, p = self.paso(x, p)
                        t += self.h
                        if 0.0 - self.tol <= x[0] <= 0.0 + self.tol:
                            f.write(f"{x[1]}\t{p[1]}\n")



