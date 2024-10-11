import lokace


def zmen_lokaci(nova_lokace: lokace.Lokace):
    akt_lokace = nova_lokace

    print(f"Nachážíš se v lokaci {akt_lokace}. Kam půjdeš?")

    for index, sousedni_lokace in enumerate(akt_lokace.hranice):
        print(f"[{index}] {sousedni_lokace}")

    vyber = input("> ")

    try:
        vyber = int(vyber)
    except Exception:
        pass

    if type(vyber) is int and vyber >= 0 and vyber < len(akt_lokace.hranice):
        zmen_lokaci(akt_lokace.hranice[vyber])
    else:
        print("Zkus to znovu.")
        print("___")
        zmen_lokaci(akt_lokace)


zmen_lokaci(lokace.hobitin)
