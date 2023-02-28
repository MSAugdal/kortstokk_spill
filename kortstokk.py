import random


class Kortstokk:
    # initialiserer kortstokken med 52 kort og stokker kortstokken
    def __init__(self) -> None:
        self._kortstokk = [f"{sort}{verdi}" for verdi in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
                           for sort in ["K", "S", "H", "R"]]
        random.shuffle(self._kortstokk)

    # deler ut n kort fra kortstokken og returnerer den som en liste over kort i "hånden"
    # sjekker om det er nok kort i kortstokken
    # hvis ikke, kastes en ValueError
    # ellers, deler ut n kort fra kortstokken og fjernen kortet fra kortstokken
    # returnerer kortene i hånden -> list
    def __haand(self, antallKort) -> list:
        hand = [self._kortstokk.pop() for _ in range(antallKort)]
        return hand

    # deler ut p antall hender med n antall kort per hånd
    # sjekker om det er nok kort i kortstokken for å dele ut
    # hvis ikke, kastes en ValueError
    # ellers, deler ut n antall hender med n antall kort per hånd
    # returnerer hender -> 2D-list
    def del_ut(self, hender, kortPerHaand) -> list:
        if hender * kortPerHaand > len(self._kortstokk):
            raise ValueError("produkt av hender og kortPerHaand er større enn antall kort i kortstokken")
        hender = [self.__haand(kortPerHaand) for _ in range(hender)]
        return hender

    # returnerer en tekst string av resterende kortstokk
    def __str__(self) -> str:
        return ", ".join(self._kortstokk)
