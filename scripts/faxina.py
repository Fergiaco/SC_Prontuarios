import shutil
import os

#Deleta Dados armazenados
shutil.rmtree('./build/deployments')
shutil.rmtree('./dados/hosp')
os.mkdir('./dados/hosp')
print('\nDados Sobre Contratos Deletados\n')
exit()