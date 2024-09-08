#Tehtävä-3
# Funktio, joka muuntaa gallonat litroiksi
def gallonat_litroiksi(gallons):
    return gallons * 3.785

# Pääohjelma
def main():
    while True:
        # Kysytään käyttäjältä gallonamäärä
        gallonat = float(input("Anna bensiinin määrä gallonina (syötä negatiivinen luku lopettaaksesi): "))

        # Jos käyttäjä syöttää negatiivisen luvun, lopetetaan ohjelma
        if gallonat < 0:
            print("Ohjelma lopetettu.")
            break

        # Muutetaan gallonat litroiksi
        litrat = gallonat_litroiksi(gallonat)
        print(f"{gallonat} gallonaa on {litrat:.2f} litraa.")

# Kutsutaan pääohjelmaa
if __name__ == "__main__":
    main()
