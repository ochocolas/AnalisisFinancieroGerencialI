import numpy as np

print('*******************************************')
print('Analisis financiero gerencial I')
print('Diana Melisa Oliva Paiz - 4290-06-578')
print('Jorge Barquero - 4290-12-5366')
print('Maria Fernanda Ruano - 4290-13-82')
print('*******************************************')
print('VALOR PRESENTE')
print('Se le presenta una oportunidad de inversion a CAMFIVE')

i = 0.06
periodos = 5 #5 anios de inversion
valor_esperado = 1500000 #la ganancia esperada a 5 anios

p_str = 'Por un periodo de ' + str(periodos) + ' anios'
i_str = 'A una tasa del ' + str(i*100) + '% de intereses'
v_str = 'Se espera una cantidad de ' + str('Q{:,.2f}'.format(valor_esperado)) + ' al final del periodo'

print(i_str)
print(p_str)
print(v_str)

valor_presente = np.pv(rate=i, nper= periodos, pmt=0, fv=valor_esperado)

print('==================================================================')
print('El valor requerido de inversion para obtener ')
print('el beneficio planteado es de: Q{:,.2f}'.format(-valor_presente))
print('==================================================================')