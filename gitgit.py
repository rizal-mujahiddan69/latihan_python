import os

try:
  os.system('git clone https://github.com/JamieMicro/NeuralNetworkSimulator')
except:
  pass
os.chdir('NeuralNetworkSimulator')
os.system('pip install pygame')
os.system('pip install cx_freeze')
os.system('python VisualML.py')