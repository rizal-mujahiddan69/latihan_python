from sklearn.decomposition import PCA
import numpy as np

matriks = []
r = int(input('berapa baris nih'))
c = int(input('berapa baris nih'))

for i in range(r):
	a = []
	for j in range(c):
		g = int(input())
		a.append(g)
	matriks.append(a)

