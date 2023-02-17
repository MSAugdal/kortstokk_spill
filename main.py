import random
from time import sleep


class Kortstokk:
    # initialiserer kortstokken med 52 kort og stokker kortstokken
    def __init__(self) -> None:
        self._kortstokk = [f"{verdi}{sort}" for verdi in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
                           for sort in ["K", "S", "H", "R"]]
        random.shuffle(self._kortstokk)

    # deler ut n kort fra kortstokken og returnerer den som en liste over kort i "hånden"
    # sjekker om det er nok kort i kortstokken
    # hvis ikke, kastes en ValueError
    # ellers, deler ut n kort fra kortstokken og fjernen kortet fra kortstokken
    # returnerer kortene i hånden -> list
    def haand(self, antallKort) -> list:
        if antallKort > len(self._kortstokk):
            raise ValueError("Ikke nok kort i kortstokken")
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
        hender = [self.haand(kortPerHaand) for _ in range(hender)]
        return hender

    # returnerer en tekst string av resterende kortstokk
    def __str__(self) -> str:
        return ", ".join(self._kortstokk)


class Olsen:
    def __init__(self, kortstokk, spillere, kortPerHaand) -> None:
        self._kortstokk = kortstokk()
        self._haand = self._kortstokk.del_ut(spillere, kortPerHaand)
        self._kortstokk = self._kortstokk._kortstokk
        self._kastehaugen = self._kortstokk.pop()
        # self._kortstokk.remove(self._kastehaugen)
        self._spillere = spillere
        self._spiller = 0
        self._harVunnet = False

        self.__clearTerminal()
        self.__spill()

    def __clearTerminal(self):
        print("\033c")

    def __hasWon(self, spiller):
        if len(self._haand[spiller]) == 0:
            self._harVunnet = True
            self.__clearTerminal()
            print(f"Spiller {spiller + 1} har vunnet!")

    def __getAndCheckInput(self, spiller):
        valg = input("Velg et kort fra hånden din [eks: K2]\n>>> ").upper()
        if not valg[0].isalpha():
            print("Feil syntaks. Prøv igjen")
            sleep(1)
            self.__getAndCheckInput(spiller)
        self.__check_legal_move(valg, spiller)

    def __check_legal_move(self, valg, spiller):
        if valg not in self._haand[spiller]:
            print("Du har ikke dette kortet i hånden din")
            return

    def __make_move(self):
        for spiller in range(self._spillere):
            self._spiller = spiller
            print(f"Spiller {spiller + 1} sin tur")
            print(f"Øverste kort i kastehaugen: {self._kastehaugen}")
            print(f"Spiller {spiller + 1} sin hånd: {self._haand[spiller]}")
            self.__getAndCheckInput(spiller)

    def __spill(self):
        while not self._harVunnet:
            self.__clearTerminal()
            self.__hasWon(self._spiller)
            self.__make_move()


# lager en instans av Olsen
olsen = Olsen(Kortstokk, 2)
'''
Utfordring:
Lag spillet «vri åtter(Olsen)» med følgende regler:
Hver spiller skal få utdelt en hånd med 5 kort fra en stokket kortstokk.
Deretter flippes det øverste kortet fra kortstokken og lager en ny kortstokk der kortene vender oppover.

Hver spiller plasserer et kort oppå den nye kortstokken etter følgende regler:
(i) kort med samme farge som kortet som ligger synlig, eller:
(ii) kort med samme verdi som kortet som ligger synlig, eller:
(iii) kort med verdi åtte kan bestandig spilles. Spilleren som spiller en åtter får da velge fargen på kortet.

En spiller som ikke har noen lovlige kort å spille må trekke inn ett kort.
Dette kan gjøres opp til tre ganger per runde før spilleren må melde pass.

Vinneren av spillet er den som først blir kvitt alle kortene.

Bruk Class kortstokk i implementasjon.
Presenter for hver spiller når det er deres tur samt en liste av hånden deres.
Dere må også presentere for spilleren hvilken kort som ligger øverst på dette tidspunktet.
Undersøk om kortet som spilleren spiller er et lovlig kort,
og tilby spilleren muligheten til å trekke inn ett kort(men bare tre ganger per runde for hver spiller).
Etter at spilleren har trukket inn 3 kort i en runde skal spilleren
bli presentert med muligheten til å si pass (ikke spille noen kort).
'''
