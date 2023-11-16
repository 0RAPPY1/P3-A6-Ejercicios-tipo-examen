'''
Objetivo. Algoritmo de taquilla de concierto.

Realiza un algoritmo para calcular el costo de los boletos a un concierto para “n” asistentes. 



Calcular el costo total tomando las siguientes consideraciones:

 Costo por lugar:   Zona 1 - $ 2000,  Zona 2 - $ 1000  Zona 3 - $ 700
 Cupones de cortesía  por persona:  Platino 500, Oro 300 y Plata 200


Nota 1: Estos cupones son válidos solamente de lunes a jueves.



El algoritmo  debe pedir como entrada: el nombre del cliente,  la zona, el día de la semana, y el tipo de cupón de cada asistente (si es que tiene cupón).

Nota 2. El ciclo se finalizará si ya no hay clientes que atender, por tanto, pregunta si hay un cliente más en la fila. 



La salida debe tener:

El nombre del asistente y el costo total

  El algoritmo también debe de acumular la venta total de los “n” boletos  y reportar el resultado al final.
'''

boletos = 0
clientes = 0

while True:
  boletos2 = 0
  clientes += 1
  print(' ')
  nombre = input("Coloca tu nombre: ")
  print(f"Hola {nombre}")
  print(" ")
  print("Estas son las zonas que estan:")
  print("1) Zona1 = $2000")
  print("2) Zona2 = $1000")
  print("3) Zona3 = $7000")
  Z = input("Cual zona eligues? (1, 2 o 3)") #Pregunta la zona

  if Z == "1":
    boletos2 += 2000
  elif Z == '2':
    boletos2 += 1000
  elif Z == '3':
    boletos2 += 7000

  

  D = input('Que dias es hoy? ').lower() #Dias
  if D in ['viernes', 'sabado', 'domingo']:
    print("Esos dias no hay cumpones validos")
  elif D in ['lunes','martes','miercoles','jueves']:
    print(" ")
    C = input("Cuentas con un cupon?(Si/No)").lower() #cupones
    if C == 'si':
      CT = input('Que cupon tienes (1) Platino, 2) Oro, 3) Plata): ') #Cuantos cupones tiene
      if CT == '1':
        boletos2 -= 500
      elif CT == '2':
        boletos2 -= 300
      elif CT == '3':
       boletos2 -= 200
      else:
        print(f'{CT} no es valido')
    else:
      print(f'OK respondiste {C}')
  else:
   print(f'{D} no existe')
  
  boletos += boletos2

  print(' ')
  print(f'Nombre: {nombre}')
  print(f'A pagar: {boletos2}')

  OT = input('Hay alguien mas? (Si/No): ').lower() #Otro
  if OT != "si":
    break
  else:
    print(' ')

print(' ')
print('Reporte del dia:')
print(f'Total de clientes: {clientes}')
print(f'Total de ganancias: {boletos}')
