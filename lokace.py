class Lokace:
    jmeno: str
    hranice: list

    # Volá se pří vytváření nové instance
    def __init__(self, jmeno):
        self.jmeno = jmeno

    # Definuje výstup funkce print(Lokace)
    def __str__(self):
        return self.jmeno


hobitin = Lokace("Hobitín")
brandyvina = Lokace("Most přes Brandyvínu")
belobrazda = Lokace("Bělobrázda")
hurka = Lokace("Hůrka")

hobitin.hranice = [brandyvina, belobrazda]
brandyvina.hranice = [hurka, hobitin, belobrazda]
belobrazda.hranice = [hobitin, brandyvina]
hurka.hranice = [brandyvina]
