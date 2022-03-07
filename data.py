import os

def folderno():
  nama_folder = [chr(i) for i in range(65,91)]
  print(nama_folder)
  for iii in nama_folder:
    os.system('mkdir '+iii)

def buat_folder(letak):
  a = next(os.walk('.'))[1]
  a = [i for i in a if i[0]!='.']  
  if letak == 0 :
    folderno()
  else:
    folderno()
    for jalan in a:
      os.chdir(os.getcwd()+'/'+jalan)
      buat_folder(letak-1)
      os.chdir(os.path.dirname(os.getcwd()))
      
buat_folder(10)
    
    
    
