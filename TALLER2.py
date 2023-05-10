exercise=int(input("Que ejercicio desea revisar 17.   18.  19.  20.  21.  22.  23.  24.  25.  26.  27.  28.  29,"))

if exercise==17:
  number= int(input('ingrese un numero entero '))
  if(number > 0):
    print('El numero '+(number)+' es positivo')
  else:
    print('El numero '+str(number)+' es negativo')

elif exercise==18:
  number1= int(input("Ingrese un numero ")) 
  number2= int(input("Ingrese otro numero  "))
  if (number1>number2):
    print("El numero",number1,"es mayor que el numero", number2)
  elif (number1<number2):
    print("El numero:",number1,"es menor que el numero", number2)

elif exercise==19:
  number1=float(input("Ingrese un numero "))
  number2=float(input("Ingrese otro numero "))
  number3=float(input("Ingrese el ultimo numero "))
  if (number1>number2>number3):
    print("El numero",number1,"es mayor, y el numero",number3,"es el menor")
  elif(number1>number3>number2):
    print("El numero",number1,"es mayor, y el numero",number2,"es el menor")
  elif(number2>number1>number3):
    print("El numero",number2,"es mayor, y el numero",number3,"es el menor")
  elif(number3>number1>number2):
    print("El numero",number3,"es mayor, y el numero",number2,"es el menor")
  elif(number2>number3>number1):
    print("El numero",number2,"es mayor, y el numero",number1,"es el menor")
  else:
    print("El numero",number3,"es el mas grande y el numero",number1,"es el mas pequeño")

elif exercise==20:
  name=str(input("Señor trabajador ingrese por favor su nombre "))
  h_normal=float(input("Ingrese las horas laboradas normalmente "))
  h_extra=float(input("Ingrese las horas extra que ha realizado "))
  salary=(h_normal*4)+(h_extra*8)
  print("Señor/a",name,"Su sueldo de este mes es de $",salary,"pesos ya que cuenta con",h_normal,"horas laboradas y ",h_extra,"horas extras")

elif exercise==21:
  numberA=float(input("Ingrese un numero"))
  numberB=float(input("Ingrese otro numero"))
  if (numberA>numberB):
    addition=numberB+numberA
    print("La resta de lo numeros es",numberA-numberB)
  elif(numberB>numberA):
   print("La suma de los numeros es",numberB+numberA)

elif exercise==22:
  number1=float(input("Ingrese un numero "))
  number2=float(input("Ingrese otro numero "))
  if (number2>2):
   print("El resultado de la division es",number1/number2)
  elif (number2==0):
    print("La division no fue un exito ya que no es posible realizarse")

elif exercise==23:
  number=int(input("Ingrese un numero del 1-7 "))
  if number==1:
   print("Lunes")
  elif number==2:
   print("Martes")
  elif number==3:
   print("Miercoles")
  elif number==4:
   print("Jueves")
  elif number==5:
   print("Viernes")
  elif number==6:
   print("Sabado")
  elif number==7:
   print("Domingo")
        
  
elif exercise==24:
 side1=int(input("Ingrese el valor de un lado del triangulo ")) 
 side2=int(input("Ingrese el segundo valor de un lado del triangulo ")) 
 side3=int(input("Ingrese el tercer valor de un lado del triangulo ")) 
 if side1== side2 and side1==side3:
  print("El triagunlo por tener sus tres lados iguales corresponde a un Equilatero")
 else:
  print("El triagunlo no es Equilatero")

elif exercise==25:
 number1=float(input("Ingrese un número "))
 number2=float(input("Ingrese otro numero "))
 if (number1<0 or number2<0):
  print("La suma de los dos numeros es",number1+number2)
 elif(number1>0 or number2>0):
    print("la multiplicación de los dos numeros es ",number1*number2)


elif exercise ==26:
  day=int(input("Ingrese el dia de su nacimiento "))
  month=int(input("Ingrese el mes de su nacimiento "))
  if (month == 1 and day>=20) or (month ==2 and day <=18):
    print("ACUARIO")
  elif (month == 2 and day>=19)or (month ==3 and day <=20):
    print("PISCIS")
  elif (month == 3 and day>=21) or(month ==4 and day <=19):
    print("ARIES")
  elif (month == 4 and day>=20) or(month==5 and day <=20):
    print("TAURO")
  elif (month == 5 and day>=21)or (month==6 and day<=20):
    print("GEMINIS")
  elif (month ==6 and day>=21)or (month==7 and day <=22):
    print("CANCER")
  elif (month ==7 and day>=23) or(month==8 and day <=22):
   print("LEO")
  elif (month ==8 and day>=23) or(month==9 and day <=22):
   print("VIRGO")
  elif (month ==9 and day>=23) or(month==10 and day <=22):
   print("LIBRA")
  elif (month ==10 and day>=23)or (month==11 and day <=21):
   print("ESCORPIO")
  elif (month ==11 and day>=22)or (month==12 and day <=21):
   print("SAGITARIO")
  elif (month ==12 and day>=22)or (month==13 and day <=19):
   print("CAPRICORNIO")

elif exercise==27:
  base=float(input("Ingrese la base del cuadrilatero  "))
  height=float(input("Ingrese la altura del cuadrilatero  "))
  if (base==height): 
   perimeter=base*4
   area=base*height
   print("Esta figura es un cuadrado su area es de",area,"y su perimetro de",perimeter)
  elif (base != height):
   perimeter1 = (base*2)+(height*2)
   area1 = (base*height)
   print("La figura es un rectangulo y su area es de",area1,"y su perimetro de",perimeter1)

elif exercise==28:
  sale=float(input("Ingrese el precio de la venta realizada "))
  #discount 5%
  if (sale < 100):
   discount= sale*5/100
   price=sale-discount
   print("El descuento realizado fue del 5% que tiene valor de ",discount,"es decir que su compra final equivale a ",price)
  elif (sale >100 or sale==100) and (sale < 200):
   discount2=sale*10/100
   prince2=sale-discount2
   print("El descuento realizado fue del 10% que tiene valor de ",discount2,"es decir que su compra final equivale a ",prince2)
  elif (sale >200 or sale ==200):
   discount3=sale*15/100
   prince3=sale-discount3
   print("El descuento realizado fue del 15% que tiene valor de ",discount3,"es decir que su compra final equivale a ",prince3)

elif exercise==29:
  year=int(input("Ingrese un año"))
  if not(year%4 and year %100 or not year %400):
   print("El año ingresado",year,"es bisiesto:  ")
  else:
   print("El año ingresado",year,"no es bisiesto")

                   



    

  
  







 
