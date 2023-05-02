exercise=int(input("Que ejercicio desea revisar 1.   2.  3.  4.  5.  6.  7.  8.  9.  10.  11.  12.  13.  14,"))

if exercise==1:
  #Area de un triangulo
  base = int (input("Ingrese por favor la base del triangulo:")) 
  height = int (input("Ingrese por favor la altura del triangulo:")) 
  area = (base * height )/2 
  print("El area del triangulo es:", area )

elif exercise==2:
  #Suma de numeros
  num1=int(input("Ingrese un numero"))
  num2=int(input("Ingrese otro numero"))
  add=(num1 + num2) 
  print ("la suma de los dos numeros ingresados fue:", add) 
  
elif exercise==3:
  #Elevado al cuadrado
  num=int(input("Ingrese el numero que desee elevar al cuadrado"))
  empowerment=num**2
  print("El numero ingresado elevado al cuadrado es:",empowerment)

elif exercise==4:
  #Suma de numeros
  num1= 1234
  num2= 532
  add=num1+num2
  print("la suma de 1234 + 532 es:",add)

elif exercise==5:
  #Resta de numeros
  num1= 1234
  num2= 532
  subtraction=num1-num2
  print("la resta de 1234 - 532 es:",subtraction)

elif exercise==6:
  #Multiplicacion de numeros
  num1= 1234
  num2= 532
  multiplication=num1*num2
  print("la multiplicacion de 1234 * 532 es:",multiplication)

elif exercise==7:
  #Division de numeros
  num1= 1234
  num2= 532
  division=num1/num2
  print("la division de 1234 / 532 es:",division)

elif exercise==8:
  #Modulo de numeros
  num1= 1234
  num2= 532
  module=num1%num2
  print("El modulo de 1234 % 532 es:",module)

elif exercise==9:
  #Euros a dolares
  euro=float(input("Ingrese la cantidad de euros que quiera convertir a dolares"))
  conver=euro*1.10
  print("Los euros ingresados corresponden a:",conver,"dolares")

elif exercise==10:
  #Area de un rectangulo
  long = int (input("Ingrese por favor el largo del rectangulo:")) 
  width= int (input("Ingrese por favor el ancho del rectangulo:")) 
  area = long * width
  print("El area del rectangulo es:", area )

elif exercise==11:
  #Area y perimetro de un cuadrado
  sides=int(input("Ingrese lado del cuadrado"))
  area=sides*sides
  perimeter=sides*4
  #area
  print("El area del cuadrado es:",area, "y el perimetro es:",perimeter)

elif exercise==12:
  #Area y volumen de un cilindro 
  radio=int(input("Ingrese el radio del cilindro"))
  height=int(input("Ingrese la altura"))
  #area
  area=2*3.1416*radio*height+(2*3.1416*radio*2)
  print("el area del cilindro es:",area)
  #volumen
  volume=3.1416*radio*2*height
  print("El volumen del cilindro es:",volume)

elif exercise==13:
  #Leer radio
  rad=int(input("Ingrese el radio de la circunferencia"))
  #Calcular longitud
  lenght=2*3.1416*rad
  print("la longitud de la circunferencia es:", lenght)
  #calcular Area
  area=3.1416*rad**2
  print("El area de su circulo es:",area)

elif exercise==14:
  #Promedio de numeros
  num1=int(input("Ingrese el primer numero "))
  num2=int(input("ingrese el segundo numero "))
  num3=int(input("ingrese el tercer numero "))
  promedio=(num1+num2+num3)/3
  print("El promedio de los tres numeros ingresados es:", promedio)
