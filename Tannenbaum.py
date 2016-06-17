# Autor: Aman
# Tannenbaum

#Version 1

#Variablen
l = int(input("Eingabe: "))

sterne = "**"
stern = "*"
sterne_anzahl = 0
loop = 0
out = "*"
var1 = l
FILLER1 = ""
FILLER = ' '

def stamm():
    var2 = l//4
    countFILLER = len(FILLER1)
    for loop in range(0, var2):
        
        print(str((" " * (countFILLER - var2 // 2)) + (stern * var2)))
    

while loop<l:

    var1 = var1 -1

    if loop==0:
        FILLER1 = FILLER * var1
        print(FILLER * var1 + "W")
    else:
        while sterne_anzahl<loop:
            out = out + sterne
            sterne_anzahl = sterne_anzahl + 1
    if(loop%3 == 0):
        print(FILLER * (var1 - 1) + "I" + out + "I")
    else: 
        print(FILLER * var1 + out)
    loop =loop + 1

    
stamm()

