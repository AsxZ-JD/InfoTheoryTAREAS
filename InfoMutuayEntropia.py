'''
Programa de calcular la Información Mutua y Entropía
'''

import math

#VARIABLES --------------------------------------------------------------
Eventos=[]
inp = input("Elija tipo de proceso: \n 1.Cuantificable \n 2.Transmisión de datos binaria \n 3.Transición de estados\n")
N = input("\nListe los eventos (Separados por " ") \n")
Eventos = N.split()
repetidos=[]
IE=[]
HE=[]
j = 0



#FUNCIONES --------------------------------------------------------------
def Calculo_InfoMutua (inp, probabilidad):
  if inp == 1:
    return -math.log(probabilidad, 10)
  elif inp ==2:
    return -math.log(probabilidad, 2)
  elif inp ==3:
    if probabilidad <1:
      return -math.log(probabilidad)
    else:
      return math.log(probabilidad)



#MAIN --------------------------------------------------------------
rept = input("\nAlguna probabilidad se repite? 1-SI, 2-NO\n")
if rept =="1":
  print("\nIngrese cuantas veces cada una\n ")
  for prob in Eventos:
    print(f'{prob}', end="|")
  r = (input("\n"))
  repetidos = r.split()


for i in Eventos:
    if "/" in i:
        i = i.partition("/")
        x = float(i[0])
        y = float(i[2])
        z = (x/y)
        if rept=="1":
           IE.append(int(repetidos[j])*Calculo_InfoMutua(int(inp), z))
        else:
           IE.append(Calculo_InfoMutua(int(inp), z))
        HE.append(IE[j]*z)
    else:
        i = float(i)
        if rept=="1":
           IE.append(int(repetidos[j])*Calculo_InfoMutua(int(inp), i))
        else:
           IE.append(Calculo_InfoMutua(int(inp), i))
        HE.append(IE[j]*i)
    j+=1


print("Probabilidades: ", Eventos)
print("Info: ", IE)
print("Entropía: ", HE)
print("Info Total: ", sum(IE))
print("Entropía Total: ", sum(HE))
