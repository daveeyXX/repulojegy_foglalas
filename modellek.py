from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def info(self):
        pass

class BelfoldiJarat(Jarat):
    def info(self):
        return f"Belföldi Járat | Szám: {self.jaratszam} | Cél: {self.celallomas} | Ár: {self.jegyar} Ft"

class NemzetkoziJarat(Jarat):
    def info(self):
        return f"Nemzetközi Járat | Szám: {self.jaratszam} | Cél: {self.celallomas} | Ár: {self.jegyar} Ft"

class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def hozzaad_jarat(self, jarat):
        self.jaratok.append(jarat)

    def get_jarat(self, jaratszam):
        for j in self.jaratok:
            if j.jaratszam == jaratszam:
                return j
        return None
