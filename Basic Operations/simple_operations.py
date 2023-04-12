print( " Welcome to the calculator, here you will make simple operations ")
print( " ------------------------------------ ")
choose = float(input("wich operation will be make? (type the number, for choose the wanted operation 1.Addition, 2.Subtraction 3.Multiplication 4.Division )"))

if choose == 1:
 print("You chose Addition ")
 print( " ------------------------------------ ")
  
 n1 = float(input("type the first value:"))
 n2 = float(input("Type the second value:"))
 plus = n1 + n2
 print (" Your result is:", plus)
 
elif choose == 2: 
 print("You chose Subtraction")
 print( " ------------------------------------ ")

 n1 = float( input("digite o primeiro valor:"))
 n2 = float(input("digite o segundo valor:"))
 substract = n1 - n2
 print (" Your result is :", substract)

elif choose == 3:
 print("You chose Multiplication ")
 print( " ------------------------------------ ")

 n1 = float(input("type the first value:"))
 n2 = float(input("Type the second value:"))
 multP = n1 * n2
 print (" Your result is :", multP)

elif choose == 4: 
 print("You chose Division")
 print( " ------------------------------------ ")

 n1 = float(input("type the first value:"))
 n2 = float(input("Type the second value:"))
 divis = n1/n2
 print (" Your result is :", divis)


else:
 print("Bact to the begin")
