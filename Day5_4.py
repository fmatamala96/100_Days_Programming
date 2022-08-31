#numeor divisible por 3 es fizz
#numeor divisible por 3 es buzz
#numeor divisible por 3 y 5 es fizzbuzz


for x in range(1,101):

    if x % 3 == 0 and x % 5 != 0:
        print("Fizz")
    elif x % 5 == 0 and x % 3 != 0:
        print("Buzz")
    elif x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    else:
        print (x)  


""" 
Este codigo podria funcionar solo si FizzBuzz va primero ya que si el numero cumple con algun if antes este bucle pasara al siguiente
for x in range(1,101):

    if x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    else:
        print (x)   
""" 

