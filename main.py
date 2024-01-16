import datetime
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

# értékadások

utanfuto1 = Utanfuto(tipus="ponyvás",ar=1500,teherbiras=150,rendszam="AQC-121")
utanfuto2 = Utanfuto(tipus="fékezett",ar=1500,teherbiras=150,rendszam="ABC-131")
utanfuto3 = Utanfuto(tipus="ponyvás@fékezett",ar=1500,teherbiras=150,rendszam="KBC-541")

kolcsonzes1 = Kolcsonzes(mettol="2024-02-22",meddig="2024-02-26",rendszam="AQC-121")
kolcsonzes1 = Kolcsonzes(mettol="2024-03-12",meddig="2024-04-26",rendszam="ABC-541")

print("lehetőségek:")
inputresult = int(input("1- kölcsönzés, 2 - lemondás 3- listázás: "))
if not (isinstance(inputresult, int)):
        raise TypeError("Nem egész számod adtál meg.")




if inputresult == 2:
    print("Mikori foglalást szeretné lemondani? ")
    lemodasdatum = datetime.date.fromisoformat(input("formátum 2024-01-16"))




if inputresult == 1:
    print("Mikori szeretne foglalni? ")
    mettol = datetime.date.fromisoformat(input("formátum 2024-01-16 "))
    print("Meddig? ")
    meddig = datetime.date.fromisoformat(input("formátum 2024-01-16 "))
    print("Melyik rendszámú autót? ")
    auto = str(input("formátum AAA-123"))



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








