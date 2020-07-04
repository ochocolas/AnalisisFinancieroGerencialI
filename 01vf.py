import numpy as np
import matplotlib.pyplot as plt

print('*******************************************')
print('Analisis financiero gerencial I')
print('Diana Melisa Oliva Paiz - 4290-06-578')
print('Jorge Barquero - 4290-12-5366')
print('Maria Fernanda Ruano - 4290-13-82')
print('*******************************************')
print('VALOR FUTURO')

n = 8 #periodos
t = list(range(0,n))
inversion_maq = -400 #Inversion en miles de Q (Q400,000)
inversion_ven = -250 #Inversion en miles de Q (Q250,000)

def vf6(n,importe):
	i = 0.08 #tasa de interes calculada de incremento por maquinaria
	
	print('Tasa de interes del: {}%'.format(i*100))
	return np.fv(pv=importe,rate=i,pmt=0,nper=n)

def vf8(n,importe):
	i = 0.179 #tasa de crecimiento basado en incremento de vents del 2018 al 2019
	print('Tasa de interes del: {}%'.format(i*100))
	return np.fv(pv=importe,rate=i,pmt=0,nper=n)

vf6 = vf6(t, inversion_maq)
vf8 = vf8(t, inversion_ven)


plt.title("Graficando Valor futuro de inversion de 400K al 8% y 250K 17.9%")

plt.plot(t,vf6,label="INV MAQ 8% y 400K",linewidth=4)
plt.plot(t,vf8,label="INV VEN 17.9% y 250K",linewidth=4)
plt.xlabel("Anios")
plt.ylabel("Miles de Q")
plt.legend(loc='upper left')
plt.show()
