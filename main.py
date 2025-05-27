from modellek import BelfoldiJarat, NemzetkoziJarat, LegiTarsasag
from foglalaskezelo import JegyFoglalas, FoglalasKezelo

def elore_betoltes():
    airline = LegiTarsasag("SkyFly")
    airline.hozzaad_jarat(BelfoldiJarat("B123", "Budapest", 15000))
    airline.hozzaad_jarat(BelfoldiJarat("B456", "Debrecen", 12000))
    airline.hozzaad_jarat(NemzetkoziJarat("N789", "London", 45000))

    kezelo = FoglalasKezelo()
    kezelo.foglalas_hozzaad(JegyFoglalas("Anna", airline.get_jarat("B123")))
    kezelo.foglalas_hozzaad(JegyFoglalas("Béla", airline.get_jarat("B456")))
    kezelo.foglalas_hozzaad(JegyFoglalas("Csaba", airline.get_jarat("N789")))
    kezelo.foglalas_hozzaad(JegyFoglalas("Dóra", airline.get_jarat("B123")))
    kezelo.foglalas_hozzaad(JegyFoglalas("Erika", airline.get_jarat("N789")))
    kezelo.foglalas_hozzaad(JegyFoglalas("Ferenc", airline.get_jarat("B456")))

    return airline, kezelo

def menu():
    print("\nRepülőjegy Foglalási Rendszer")
    print("1. Jegy foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása")
    print("0. Kilépés")

def main():
    airline, kezelo = elore_betoltes()
    
    while True:
        menu()
        valasz = input("Válassz egy lehetőséget: ")

        if valasz == "1":
            nev = input("Név: ")
            print("\nElérhető járatok:")
            for j in airline.jaratok:
                print(j.info())
            jaratszam = input("Foglalni kívánt járatszám: ")
            jarat = airline.get_jarat(jaratszam)
            if jarat:
                foglalas = JegyFoglalas(nev, jarat)
                ar = kezelo.foglalas_hozzaad(foglalas)
                print(f"Sikeres foglalás! Ár: {ar} Ft")
            else:
                print("Hibás járatszám!")

        elif valasz == "2":
            nev = input("Név: ")
            jaratszam = input("Törlendő foglalás járatszáma: ")
            if kezelo.foglalas_torol(nev, jaratszam):
                print("Foglalás törölve.")
            else:
                print("Nincs ilyen foglalás.")

        elif valasz == "3":
            print("\nAktív foglalások:")
            for f in kezelo.listaz_foglalasok():
                print(f)

        elif valasz == "0":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()
