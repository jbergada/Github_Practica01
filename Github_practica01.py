#Bloc02 ->Python Github_Practica01.py

import math
PI = math.pi  


def quadrat():
    pass

def triangle():
    pass

def rectangle():
    pass

def paralellogram():
    pass

def rombe():
    pass

def estel():
    pass

def _trapezi():
    pass

def cercle():
    print("Càlcul del àrea i el perímetre d'un cercle ")
    radi = float(input("radi = "))
    area = math.pow(radi, 2) * PI
    perimetre = 2 * PI * radi
    return area, perimetre

def poligon():
    pass

def corona():
    pass

def sector():
    pass

def tronc_con():
    print("Càlcul àrea i volum d'un tronc de con" )
    R = float(input("Radi major = "))
    r = float(input("radi menor = "))
    h = float(input("altura = "))
    g = float(input("generatriu = "))
    area = PI * (g * (r+R)+(r*r)+math.pow(R,2))
    volum = PI * h * ((R*R)+(r*r)+(R*r))/3
    return area, volum
    


# Programa principal

print("             Menú               ")
print("================================")
print("")
print("1. Àrea i perímetre d'un quadrat ")
print("2. Àrea i perímetre d'un triangle ")
print("3. Àrea i perímetre d'un rectangle ")
print("4. Àrea i perímetre d'un paral·lelogram ")
print("5. Àrea i perímetre d'un rombe ")
print("6. Àrea i perímetre d'un estel ")
print("7. Àrea i perímetre d'un trapezi ")
print("8. Àrea i perímetre d'un cercle ")
print("9. Àrea i perímetre d'un polígon regular ")
print("10. Àrea i perímetre d'una corona circular ")
print("11. Àrea i perímetre d'un sector circular ")
print("")
print("12. Àrea i volum d'un cub ")
print("13. Àrea i volum d'un cilindre ")
print("14. Àrea i volum d'un ortoedre ")
print("15. Àrea i volum d'un prisma recte ")
print("16. Àrea i volum d'un con ")
print("17. Àrea i volum d'un tronc de con ")
print("18. Àrea i volum d'una esfera ")
print("19. Àrea i volum d'una piràmide ")
print("20. Àrea i volum d'un tetraedre regular ")
print("21. Àrea i volum d'un octaedre regular ")
print("22. Àrea i volum d'un tronc de piràmide ")
print("23. Àrea i volum d'un casquet esfèric ")
print("24. Àrea i volum d'un fus -falca esfèrica- ")
print("25. Àrea i volum d'una zona o segment esfèric ")
print("")
print("==============================================")

menu = int(input("escull un element del menú: "))

if menu == 1 :
    pass
elif menu == 2 :
    pass
elif menu == 3 :
    pass
elif menu == 4 :
    pass
elif menu == 5 :
    pass
elif menu == 6 :
    pass
elif menu == 7 :
    pass
elif menu == 8 :
    area,perimetre = cercle()
    print("L'àrea és: ", area)
    print("El perímetre és: ", perimetre)
elif menu == 9 :
    pass
    """ menu < 10:
    print("El perímetre és: ", perimetre)
    elif menu>=10:
    """
elif menu == 10 :
    pass
elif menu == 11 :
    pass
elif menu == 12 :
    pass
elif menu == 13 :
    pass
elif menu == 14 :
    pass
elif menu == 15 :
    pass
elif menu == 16 :
    pass
elif menu == 17 :
    area,volum = tronc_con()
    print("L'àrea és  ", area)
    # para ver más adelante
    # unidad = unicode(u"cm \U+00B3").encode("utf8")
    print("El volum en cm és  ",volum, "cm3.")
elif menu == 18 :
    pass
elif menu == 19 :
    pass
elif menu == 20 :
    pass
elif menu == 21 :
    pass
elif menu == 22 :
    pass
elif menu == 23 :
    pass
elif menu == 24 :
    pass
elif menu == 25 :
    pass



# Git commands

# git status
# git add . -> afegeix tots els arxius
# git commit -m "Descriu el que hem fet"
# git push -> pujar al repositori