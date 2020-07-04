import numpy as np
import matplotlib.pyplot as plt

print('*******************************************')
print('Analisis financiero gerencial I')
print('Diana Melisa Oliva Paiz - 4290-06-578')
print('Jorge Barquero - 4290-12-5366')
print('Maria Fernanda Ruano - 4290-13-82')
print('*******************************************')
print('Tasa interna de retorno')

inversion_ventas = -250000
retorno = 43750
tir = np.irr([inversion_ventas, retorno, retorno, retorno, retorno, retorno, retorno, retorno, retorno])

print(tir * 100)

