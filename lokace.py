class Lokace:
    jmeno: str
    uvitaci_text: str
    hranice: list

    # Volá se pří vytváření nové instance
    def __init__(self, jmeno, uvitaci_text=None):
        self.jmeno = jmeno
        self.uvitaci_text = (
            uvitaci_text
            if uvitaci_text is not None
            else f"Nachážíš se v lokaci {jmeno}. Kam půjdeš?"
        )

    # Definuje výstup funkce print(Lokace)
    def __str__(self):
        return self.jmeno


hobitin = Lokace(
    "Hobitín",
    "Stojíš na začátku své cesty ve vesničce Hobitín, obklopený zelenými kopci, kde se nízké, okrouhlé domky hobitů s trávou porostlými střechami schovávají mezi rozkvetlými zahradami. Slunce svítí na barevné záhony květin a kolem tebe je slyšet zpěv ptáků a vzdálený smích místních obyvatel. Vzduch voní čerstvým chlebem a pípou z blízké hospody, kde začíná každé dobré hobití dobrodružství. Otevřené cesty se vinou mezi zahradami a lákají tě, aby ses vydal dál. Ale kam tě nohy zavedou?",
)
brandyvina = Lokace("Most přes Brandyvínu")
belobrazda = Lokace("Bělobrázda")
hurka = Lokace("Hůrka")

hobitin.hranice = [brandyvina, belobrazda]
brandyvina.hranice = [hurka, hobitin, belobrazda]
belobrazda.hranice = [hobitin, brandyvina]
hurka.hranice = [brandyvina]
