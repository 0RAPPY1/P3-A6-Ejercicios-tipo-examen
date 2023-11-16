'''
Utilizando la función randint( ) , genera un número entre 1 y 10. 

Realiza un juego cuyo objetivo es adivinar el número generado en menos de 3 intentos. Necesitas un ciclo para preguntar por el número, si el número es adivinado se sale del ciclo o si las 3 oportunidades se agotaron. 

Al final debes de reportar si lo logró y en cuantos intentos, o si perdió
'''

import random

o = 0  #Oportunidades
numero = random.randint(1, 10)

print('Hola tienes 3 intentos para adivinar el nuemro')

while o<3:
  o+=1
  
  print(' ')
  print(f'Intento: {o}')
  P = int(input('Coloca un numero del 1 al 10: '))
  if P == numero:
    print(f"Ganaste, tu numero {P} es correcto")
    print(f'Lo lograste en intento {o}')
    break
  elif P < numero:
    print('Tu numero es menor')
  elif P > numero:
    print('Tu numero es mayor')
  else:
    print('Tu numero debe de ser del 1 al 10')
  if o == 3:
    print(" ")
    print('Tus intentos se acabaron')
    if P!=numero:
      print(f"Perdiste, tu numero {P} es incorrecto")
      print(f'Intentos: {o}')
    
