'''
Programa de calcular probabilidad de lanzar moneda
'''


import math

continuar = True

def calc_prob(tipo, x, n):
  P=0
  #print(f'TIPO: {tipo}\n X: {x}\n N: {lanzamientos}')
  if tipo=="A":
    P = (math.factorial(n)/(math.factorial(x)*(math.factorial(n-x))))*(pow(0.5, x))*(pow(0.5, n-x))

  elif tipo=="B":
    for i in range(x, n+1):
      P = P + (math.factorial(n)/(math.factorial(i)*(math.factorial(n-i))))*(pow(0.5,i))*(pow(0.5, n-i))

  elif tipo=="C":
    for i in range(0, x+1):
      P = P + (math.factorial(n)/(math.factorial(i)*(math.factorial(n-i))))*(pow(0.5,i))*(pow(0.5, n-i))
  P=P*100
  return print("PROBABILIDAD: ", P)






while continuar:
  toss = input("\nLANZAR MONEDA? 1-SI 2-NO\n")

  if toss=="2":
    continuar = False
    break

  else:
    lanzamientos = input("Cuántos lanzamientos?\n")
    tipo_prob = input("Probabilidad de que caiga cara \nA-Exactamente \nB-Al menos \nC-A lo mucho ... \nCuántas veces?\n")
    tipo_prob = tipo_prob.split()
    calc_prob(tipo_prob[0], int(tipo_prob[1]), int(lanzamientos))






