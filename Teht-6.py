# Tehtävä-6
import math

# Funktio, joka laskee pizzan yksikköhinnan euroina per neliömetri
def laske_yksikkohinta(halkaisija, hinta):
    # Lasketaan pizzan säde (halkaisija jaetaan kahdella)
    sade = halkaisija / 2
    # Lasketaan pizzan pinta-ala (A = π * r^2) neliömetreinä
    pinta_ala = math.pi * (sade / 100) ** 2
    # Lasketaan yksikköhinta (euroa per neliömetri)
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta

# Pääohjelma
def main():
    # Kysytään käyttäjältä ensimmäisen pizzan halkaisija ja hinta
    halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
    hinta1 = float(input("Anna ensimmäisen pizzan hinta (euroa): "))

    # Kysytään käyttäjältä toisen pizzan halkaisija ja hinta
    halkaisija2 = float(input("Anna toisen pizzan halkaisija (cm): "))
    hinta2 = float(input("Anna toisen pizzan hinta (euroa): "))

    # Lasketaan molempien pizzojen yksikköhinnat
    yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

    # Tulostetaan yksikköhinnat
    print(f"Ensimmäisen pizzan yksikköhinta on {yksikkohinta1:.2f} euroa/m².")
    print(f"Toisen pizzan yksikköhinta on {yksikkohinta2:.2f} euroa/m².")

    # Vertaillaan pizzojen yksikköhintoja ja ilmoitetaan, kumpi on edullisempi
    if yksikkohinta1 < yksikkohinta2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif yksikkohinta1 > yksikkohinta2:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Molemmat pizzat antavat yhtä hyvän vastineen rahalle.")

# Kutsutaan pääohjelmaa
if __name__ == "__main__":
    main()
