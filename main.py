import utanfuto

class Utanfuto:
    ervenyes_muszaki = "igen"
    def __init__(self,tipus,ar,teherbiras,rendszam,kolcsonozheto = "igen"):
        self.tipus = tipus
        self.ar = ar
        self.teherbiras = teherbiras
        self.rendszam = rendszam

class Kolcsonzes:
    def __init__(self,mettol,meddig,rendszam):
        self.mettol = mettol
        self.meddig = meddig
        self.rendszam = rendszam


utanfuto1 = Utanfuto(tipus="ponyvás",ar=1500,teherbiras=150,rendszam="AQC-121")
utanfuto2 = Utanfuto(tipus="fékezett",ar=1500,teherbiras=150,rendszam="ABC-131")
utanfuto3 = Utanfuto(tipus="ponyvás@fékezett",ar=1500,teherbiras=150,rendszam="KBC-541")

print("lehetőségek:")
inputresult = int(input("1- kölcsönzés, 2 - lemondás 3- listázás: "))
if not (isinstance(inputresult, int)):
        raise TypeError("Nem egész számod adtál meg.")




# if inputresult == 2:



# if inputresult == 1:
    #kölcsönöz


if inputresult == 3:
    print(utanfuto1.rendszam)
    print("teherbírás ", utanfuto1.teherbiras)
    print("típus", utanfuto1.tipus)
    print(utanfuto1.teherbiras)
    print(utanfuto1.ar)
    print("érvényes műszaki :", utanfuto1.ervenyes_muszaki)

    print(utanfuto1.rendszam)
    print("teherbírás ", utanfuto1.teherbiras)
    print("típus", utanfuto1.tipus)
    print(utanfuto1.teherbiras)
    print(utanfuto1.ar)
    print("érvényes műszaki :", utanfuto1.ervenyes_muszaki)

    print(utanfuto2.rendszam)
    print("teherbírás ", utanfuto2.teherbiras)
    print("típus", utanfuto2.tipus)
    print(utanfuto2.teherbiras)
    print(utanfuto2.ar)
    print("érvényes műszaki :", utanfuto2.ervenyes_muszaki)

    print(utanfuto3.rendszam)
    print("teherbírás ", utanfuto3.teherbiras)
    print("típus", utanfuto3.tipus)
    print(utanfuto3.teherbiras)
    print(utanfuto3.ar)
    print("érvényes műszaki :", utanfuto3.ervenyes_muszaki)








