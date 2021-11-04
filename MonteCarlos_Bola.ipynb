import random 
import numpy as np 
import matplotlib.pyplot as plt 

#Copie e Cole o codigo no Jupyter Notebook

urna = ['B','B','B','B','B','B','P','P','P','P']
print('Urna:',urna)


Num = 0 # numero de retiradas de bolas brancas
NumeroDeExperimentos = 1000 # numero de experimentos
for i in range(0, NumeroDeExperimentos):
    Pos_Bola = random.randint(0, len(urna) - 1)
    if(urna[Pos_Bola] == 'B'):
        Num = Num + 1
print('Fração de vezes que saiu uma bola branca:', Num / NumeroDeExperimentos)
# vamos calcular a Probabilidade 
Valor_teo = 0
for bola in urna:
    if (bola == 'B'):
        Valor_teo = Valor_teo + 1
Valor_teo = Valor_teo / len(urna)
print('Valor teórico da probabilidade:', Valor_teo)

vp = [] 
vsim = [] 
Nmax = 1000 
for NumeroDeExperimentos in np.arange(1, Nmax, 1):
    Num = 0 # numero de retiradas de bolas brancas
    for i in range(1, NumeroDeExperimentos):
        Pos_Bola = random.randint(0, len(urna) - 1)
        if(urna[Pos_Bola] == 'B'):
            Num = Num + 1
    vp.append(Num / NumeroDeExperimentos)
    vsim.append(NumeroDeExperimentos)

plt.figure(figsize=(8,6))
plt.plot(vsim, vp, linestyle='-', color="blue", linewidth=2,label = 'Valor simulado')
plt.axhline(y=Valor_teo, color='r', linestyle='--', label ='Valor teorico')
plt.ylabel("olas brancas", fontsize=20)
plt.xlabel("Numero de experimentos", fontsize=20)
plt.xlim([0.0, Nmax])
plt.ylim([0.0, 1.0])
plt.legend()
plt.show(True)