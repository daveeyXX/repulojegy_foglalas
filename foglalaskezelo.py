class JegyFoglalas:
    def __init__(self, nev, jarat):
        self.nev = nev
        self.jarat = jarat

    def info(self):
        return f"{self.nev} - {self.jarat.jaratszam} ({self.jarat.celallomas}) - {self.jarat.jegyar} Ft"

class FoglalasKezelo:
    def __init__(self):
        self.foglalasok = []

    def foglalas_hozzaad(self, foglalas):
        self.foglalasok.append(foglalas)
        return foglalas.jarat.jegyar

    def foglalas_torol(self, nev, jaratszam):
        for f in self.foglalasok:
            if f.nev == nev and f.jarat.jaratszam == jaratszam:
                self.foglalasok.remove(f)
                return True
        return False

    def listaz_foglalasok(self):
        if not self.foglalasok:
            return ["Nincs aktív foglalás."]
        return [f.info() for f in self.foglalasok]
