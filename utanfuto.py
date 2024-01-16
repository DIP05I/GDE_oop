class Utanfuto:
    ervenyes_muszaki = "igen"
    def __init__(self,tipus,ar,teherbiras,rendszam,kolcsonozheto = "igen"):
        self.tipus = tipus
        self.ar = ar
        self.teherbiras = teherbiras
        self.rendszam = rendszam

class Redneles:
    def __init__(self,mettol,meddig,rendszam):
        self.mettol = mettol
        self.meddig = meddig
        self.rendszam = rendszam

utanfuto1 = Utanfuto(tipus="1",ar=1500,teherbiras=150,rendszam="ABC-111")
utanfuto2 = Utanfuto(tipus=2,ar=1500,teherbiras=150,rendszam="ABC-131")
utanfuto3 = Utanfuto(tipus=2,ar=1500,teherbiras=150,rendszam="KBC-111")
utanfuto4 = Utanfuto(tipus=2,ar=1500,teherbiras=150,rendszam="ABC-111")
utanfuto5 = Utanfuto(tipus=1,ar=1500,teherbiras=150,rendszam="ALC-111")
utanfuto6 = Utanfuto(tipus=2,ar=1500,teherbiras=150,rendszam="ABC-1V1")

#if utanfuto1.tipus == 1 print("Ponyvás")
#    elif utanfuto1.tipus == 2 print("fékezett")
#    else print("Ponyvás&fékezett")
print("rendszám   teherbítás    típus   kölcsönözhető  ár")
print(utanfuto1.rendszam)
print("teherbírás ", utanfuto1.teherbiras)
print("típus" , utanfuto1.tipus , "1-ponyvás, 2-fékezett, 3 - mindkettő")

print("kölcsönzési ár:", utanfuto1.ar)




