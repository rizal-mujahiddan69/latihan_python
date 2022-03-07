import os
os.system('pip install numpy')
import numpy as np

def nilainya(aa):
    assert aa in ["batu","gunting","kertas"],"harus string lah"
    if aa=="batu":
        return 0
    elif aa=="gunting":
        return 1
    elif aa=="kertas":
        return 2



def pilihan(a,b):
    if(a==b):
        print("Samalah")
    else:
        a1 = nilainya(a)
        b1 = nilainya(b)
        if(a1==0):
            if(b1==1):
                print('menang')
            else:
                print('kalah')
        elif(a1==1):
            if(b1==0):
                print('kalah')
            else:
                print('menang')
        else:
            if(b1==0):
                print('menang')
            else:
                print('kalah')

pilih = input("main gunting batu kertas, lu pilih apa ?")
pilih = pilih.lower()
gun = ["batu","gunting","kertas"]
kepilih = np.random.choice(gun, 1)[0]
pilihan(pilih,kepilih)
