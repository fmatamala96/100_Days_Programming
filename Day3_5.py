altura = int (input ("Cual es su estatura?: ")) 
yes = {"si","SI","sI","Si"}

if altura > 120:

    edad = int (input ("Cual es su edad?: "))

    if edad < 12:
        
        boleto = 5

        foto = (input ("Desearia agregar una foto: "))

        if foto in yes:

            print ("El total es: "+ str(boleto + 3)) 
        
        else:

            print ("El total es: "+ str(boleto))

    elif edad > 12 and edad < 18:
        
        boleto = 7

        foto = (input ("Desearia agregar una foto: "))

        if foto in yes:

            print ("El total es: "+ str(boleto + 3)) 
        
        else:

            print ("El total es: "+ str(boleto))

    elif edad >= 18:
        
        boleto = 12

        foto = (input ("Desearia agregar una foto: "))

        if foto in yes:

            print ("El total es: "+ str(boleto + 3)) 
        
        else:

            print ("El total es: "+ str(boleto))

else:
    print ("Debe crecer un poco mas :c")



