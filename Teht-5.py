#Tehtävä-5

# Funktio, joka poistaa listasta parittomat luvut
def karsi_parittomat(luvut):
    # Käytetään list comprehensionia parillisten lukujen suodattamiseen
    return [luku for luku in luvut if luku % 2 == 0]


# Pääohjelma
def main():
    # Luodaan testilista
    luvut = [4, 5, 6, 3, 2, 11, 10]

    # Kutsutaan funktiota ja tallennetaan tulos
    karsittu_lista = karsi_parittomat(luvut)

    # Tulostetaan alkuperäinen ja karsittu lista
    print(f"Alkuperäinen lista: {luvut}")
    print(f"Karsittu lista (vain parilliset luvut): {karsittu_lista}")


# Kutsutaan pääohjelmaa
if __name__ == "__main__":
    main()
