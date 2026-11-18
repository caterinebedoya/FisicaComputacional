import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from codigo import graficador
from codigo import IntegradorSimplectico


if __name__=="__main__":

    # Constantes globales
    n = int(5e7)        # Número de subintervalos temporales
    h = 1e-2            # Paso temporal
    lambda_param = 1.0  # Parámetro de Henon-Heiles
    d = 2               # Dimensión del problema
    num1 = 4            # Número de condiciones iniciales en y
    num2 = 4            # Número de condiciones iniciales en py
    tol = 5e-6          # Tolerancia Henon Heiles

    integrator = IntegradorSimplectico(n, h, lambda_param, 1 / 11.0, num1, num2, tol, "poincare_11.dat")
    integrator.ejecutar()

    integrator = IntegradorSimplectico(n, h, lambda_param, 1 / 10.0, num1, num2, tol, "poincare_10.dat")
    integrator.ejecutar()

    integrator = IntegradorSimplectico(n, h, lambda_param, 1 / 9.0, num1, num2, tol, "poincare_9.dat")
    integrator.ejecutar()

    integrator = IntegradorSimplectico(n, h, lambda_param, 1 / 8.0, num1, num2, tol, "poincare_8.dat")
    integrator.ejecutar()

    integrator = IntegradorSimplectico(n, h, lambda_param, 1 / 7.0, num1, num2, tol, "poincare_7.dat")
    integrator.ejecutar()

    integrator = IntegradorSimplectico(n, h, lambda_param, 1 / 6.0, num1, num2, tol, "poincare_6.dat")
    integrator.ejecutar()