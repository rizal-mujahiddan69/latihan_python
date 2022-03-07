import os 

print('pastikan python 3')
print('hapus # pada os.system jika anda belum download packagenya')

os.system('python -m pip install --user scipy')
os.system('python -m pip install --user matplotlib')
os.system('python -m pip install --user numpy')
os.system('python -m pip install --user scikit-learn')
os.system('python -m pip install --user Pillow')

import scipy.cluster.hierarchy as shc
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from PIL import Image

def namewa(sa):
	saku = sa.split('/')
	return(saku[-1])

matriks = []

print('perhatian!!! ketika masukkan data tolong disertai dengan lokasi yang tepat seperti C:/xampp/locationfotoanda')
print('dan sertai juga tipe datanya seperti .jpeg atau .jpg')

berapa = int(input('berapa foto yang ingin dimasukkan? '))

nama = []


for i in range(berapa):
	filing = input('masukkan file '+str(i+1)+' anda:')
	nama.append(namewa(filing))
	aku = filing.split('.')

	if(aku[1]!='png'):
		im1 = Image.open(filing)
		filing = aku[0]+'.png'
		im1.save(aku[0]+'.png')

	img = Image.open(filing).convert('L')

	filing_abu = filing.split('.')
	filing_abu = filing_abu[0]+'abu.'+filing_abu[1]

	img = img.resize((120,100))

	img.save(filing_abu)
	im = Image.open(filing_abu,'r')
	pix_val = list(im.getdata())
	matriks.append(pix_val)

matriks = np.array(matriks)

print(matriks.shape)

matriks = np.reshape(matriks,(berapa,12000))
scaler = MinMaxScaler()
matriks_rescale = scaler.fit_transform(matriks)

pca = PCA(n_components=0.95)
pca.fit(matriks_rescale)
hasilnya = pca.transform(matriks_rescale)

print(hasilnya)

plt.figure(figsize=(10,7))
plt.title("dendrograms")
dend = shc.dendrogram(shc.linkage(hasilnya,method='ward'))

ara = [i for i in range(berapa)]
# plt.xticks(ara,nama)

plt.show()
