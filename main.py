import lokace


def zpracuj_odpoved(pocet_moznosti: int):
    spravny_input = False

    while spravny_input is not True:
        vyber = input("> ")
        try:
            vyber = int(vyber)
        except Exception:
            pass

        if type(vyber) is int and vyber >= 0 and vyber < pocet_moznosti:
            return vyber
        else:
            print("Zkus to znovu.")
            print("\n")


def zmen_lokaci(nova_lokace: lokace.Lokace):
    akt_lokace = nova_lokace

    print("\n")
    print(akt_lokace.uvitaci_text)

    for index, sousedni_lokace in enumerate(akt_lokace.hranice):
        print(f"[{index}] {sousedni_lokace}")

    vyber = zpracuj_odpoved(len(akt_lokace.hranice))
    zmen_lokaci(akt_lokace.hranice[vyber])


# Start hry
zmen_lokaci(lokace.hobitin)
