import main
import utanfuto

utanfuto1 = Utanfuto(tipus="1",ar=1500,teherbiras=150,rendszam="ABC-111")
utanfuto2 = Utanfuto(tipus=2,ar=1500,teherbiras=150,rendszam="ABC-131")
utanfuto3 = Utanfuto(tipus=2,ar=1500,teherbiras=150,rendszam="KBC-111")
utanfuto4 = Utanfuto(tipus=2,ar=1500,teherbiras=150,rendszam="ABC-111")
utanfuto5 = Utanfuto(tipus=1,ar=1500,teherbiras=150,rendszam="ALC-111")
utanfuto6 = Utanfuto(tipus=2,ar=1500,teherbiras=150,rendszam="ABC-1V1")

print("rendszám   teherbítás    típus                kölcsönözhető  ár")
print(utanfuto1.rendszam , "  " , utanfuto1.teherbiras, utanfuto1.teherbiras, utanfuto1.ar)