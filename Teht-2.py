# Tehtävä-2
import random
# Funktio, joka palauttaa satunnaisen luvun väliltä 1..max_silmäluku
def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

# Pääohjelma, jossa kysytään käyttäjältä tahkojen määrä ja heitellään noppaa
def paohjelma():
    tahkot = int(input("Anna nopan tahkojen määrä: "))
    silmaluku = 0
    maksimi_silmaluku = tahkot

    while silmaluku != maksimi_silmaluku:
        silmaluku = heita_noppaa(tahkot)
        print(f"Nopan silmäluku: {silmaluku}")
# Kutsutaan pääohjelmaa
paohjelma()
