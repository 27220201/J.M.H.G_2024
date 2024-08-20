cadena = input ("ingrese una cadena: ")
x = True 
for i in range (len(cadena) // 2):
    if cadena[i] != cadena[-i -1]:
        x = False
        break
if x:
    print("la cadena es un palindromo")
else:
    print("la cadena no es un palindromo")