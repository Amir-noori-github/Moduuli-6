# Tehtävä-4
# Funktio, joka laskee listan lukujen summan
def laske_summa(luvut):
    return sum(luvut)

# Pääohjelma
def main():
    # Luodaan testilista
    luvut = [4, 6, 1, 2, 9]

    # Kutsutaan funktiota ja tallennetaan tulos
    summa = laske_summa(luvut)

    # Tulostetaan summan tulos
    print(f"Listan {luvut} lukujen summa on {summa}.")


# Kutsutaan pääohjelmaa
if __name__ == "__main__":
    main()
