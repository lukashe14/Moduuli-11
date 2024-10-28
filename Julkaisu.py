class Julkaisu:
    def __init__(self, name):
        self.name = name

class Kirja(Julkaisu):
    def __init__(self, name, kirjoittaja, sivumäärä):
        super().__init__(name)
        self.kirjoittaja = kirjoittaja
        self.sivu_määrä = sivumäärä

    def tulosta_tiedot(self):
        print(f"{self.name} sivu määrä on {self.sivu_määrä} ja sen on kirjoittanut {self.kirjoittaja}.")

class Lehti(Julkaisu):
    def __init__(self, name, päätoimittaja):
        super().__init__(name)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f"{self.name} päätoimittaja on {self.päätoimittaja}.")


