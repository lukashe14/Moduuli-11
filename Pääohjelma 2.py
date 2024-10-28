from Auto import *

def main():
    sähköauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)


    sähköauto.kiihdytä(100)
    polttomoottoriauto.kiihdytä(90)

    sähköauto.kulje(3)
    polttomoottoriauto.kulje(3)

    print(f"Sähköauton matkamittarilukema on {sähköauto.kuljettu_matka} km")
    print(f"Polttomoottori matkamittarilukema on {polttomoottoriauto.kuljettu_matka} km")


if __name__ == '__main__':
    main()