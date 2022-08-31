print("Bienvenido a la calculadora del amor")
test = ['t','r','u','e','l','o','v','e']
name1 = input("Cual es tu nombre?\n")
name2 = input("Cual es el nombre de la otra persona?\n")

name3 = (name1.lower() + name2.lower())
total = 0

#for n in test:
#    total += name3.count(n)
    

#print (total)

t = name3.count("t")
r = name3.count("r")
u = name3.count("u")
e = name3.count("e")

true = t+r+u+e

l = name3.count("l")
o = name3.count("o")
v = name3.count("v")
e = name3.count("e")

love = l+o+v+e

print (str(true) + str(love))
