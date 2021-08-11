

print("\nadivina un numero ")

import random
intentos=1
a=int(input("adivina un numero del 1  al 10: "))
b=int(input("adivina otro numero del 1 al 10: "))

x=random.randint( 1, 10)
y=x
while x==y:
    y=random.randint( 1, 10)


while intentos < 5:
    
   if x == a or x == b:
    
      if y == a or y == b :
          print("\nfelicidades")   
          print("\nel numero de intentos es: " ,intentos)
          break
       
      else :
         print("\nestuvo cerca")
         intentos+=1
         a=int(input("adivina un numero: "))
         b=int(input("adivina otro numero: "))
      
   elif y==a or y == b:
       
       if x ==a or x == b:
           print("\nfelicidades")
           print("\nel numero de intentos es: " ,intentos)
           break
           
       else :
           print("\ncasi sigue intentando ")
           intentos+=1
           a=int(input("adivina un numero: "))
           b=int(input("adivina otro numero: "))
      
   else:
       print("\nfallaste")
       intentos+=1
       a=int(input("adivina un numero: "))
       b=int(input("adivina otro numero: "))
       
        
if intentos == 5: 
   print (f"\ngame over {x} y {y} ")
    

