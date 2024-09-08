# Moduuli-6
# Tehtävä 1

import random

# Parametriton funktio, joka palauttaa satunnaisen nopan silmäluvun 1..6
def heita_noppaa():
    return random.randint(1, 6)

# Pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen
def paohjelma():
    silmaluku = 0
    while silmaluku != 6:
        silmaluku = heita_noppaa()
        print(f"Nopan silmäluku: {silmaluku}")

# Kutsutaan pääohjelmaa
paohjelma()
