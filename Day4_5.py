print("JUEGO DEL TESORO")

row1 = ["🔲","🔲","🔲"]
row2 = ["🔲","🔲","🔲"]
row3 = ["🔲","🔲","🔲"]

map = [row1,row2,row3]

print (f"{row1}\n{row2}\n{row3}\n")

position = input ("Donde quieres esconder el tesoro??")

position_a = int(position[0])
position_b = int(position[1])

map[position_b - 1][position_a - 1] = "💰"

print (f"{row1}\n{row2}\n{row3}\n")