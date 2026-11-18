import numpy as np
import matplotlib.pyplot as plt

class particulas:
    
    def __init__(self, masa,carga,x_i,v_i):
        self.masa = masa
        self.carga = carga
        self.posicion = np.array(x_i, dtype=float)
        self.velocidad = np.array(v_i, dtype=float)
        self.aceleracion = np.array([0,0,0])
        
    def aceleraciones(self,campo, particula_2):
        k = 1
        r = particula_2.posicion - self.posicion
        norma = np.linalg.norm(r)
        fuerza_coulomb = (k * self.carga * particula_2.carga / norma**3) * r
        fuerza_lorentz = np.cross(self.carga * self.velocidad, campo)
        self.aceleracion = (fuerza_coulomb + fuerza_lorentz) / self.masa

    def velocidades(self,dt):
        self.velocidad += self.aceleracion * dt
        
    def posiciones(self,dt):
        self.posicion += self.velocidad * 0.5 + self.aceleracion * dt **2