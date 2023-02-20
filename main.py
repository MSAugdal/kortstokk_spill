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
    # initialiserer klassen med en kortstokk, antall spillere og antall kort per hånd
    # kortstokken blir delt ut til alle spillere
    # det øverste kortet i kortstokken blir lagt i kastehaugen
    # spiller 0 sin tur
    # harVunnet blir satt til False
    # terminalen blir tømt
    # spillet starter
    def __init__(self, kortstokk, spillere, kortPerHaand) -> None:
        self._kortstokk = kortstokk()
        self._haand = self._kortstokk.del_ut(spillere, kortPerHaand)
        self._kortstokk = self._kortstokk._kortstokk
        self._kastehaugen = self._kortstokk.pop()
        self._spillere = spillere
        self._spiller = 0
        self._harVunnet = False

        self.__clearTerminal()
        self.__spill()

    # tømmer terminalen med en escape sequence
    # \033c er ESC c i ASCII, og vil tømme terminalen
    def __clearTerminal(self):
        print("\033c")

    # sjekker om spilleren har vunnet
    # hvis spilleren har vunnet, blir harVunnet satt til True
    # terminalen blir tømt
    # spilleren som har vunnet blir printet ut
    def __hasWon(self, spiller):
        if len(self._haand[spiller]) == 0:
            self._harVunnet = True
            self.__clearTerminal()
            print(f"Spiller {spiller + 1} har vunnet!")

    # sjekker om inputen er gyldig (eks: K2, H10, S3, RQ og ikke K22, H1 eller 1K)
    # sjekker at første karakter er en bokstav
    # hvis gyldig, sjekker den om spilleren har kortet i hånden
    # hvis inputen ikke er gyldig, blir spilleren bedt om å prøve igjen
    def __getAndCheckInput(self, spiller):
        valg = input("Velg et kort fra hånden din [eks: K2]\n>>> ").upper()
        if not valg[0].isalpha():
            print("Feil syntaks. Prøv igjen")
            sleep(1)
            self.__getAndCheckInput(spiller)
        self.__check_legal_move(valg, spiller)

    # sjekker om spilleren har kortet i hånden
    # fjerner kortet fra hånden og legger det i kastehaugen hvis spilleren har kortet
    # hvis ikke, blir spilleren bedt om å prøve igjen
    def __check_legal_move(self, valg, spiller):
        if valg not in self._haand[spiller]:
            print("Du har ikke dette kortet i hånden din")
            sleep(1)
            self.__getAndCheckInput(spiller)
        self._haand[spiller].remove(valg)
        self._kastehaugen = valg

    # forteller spilleren at det er deres tur
    # printer ut øverste kort i kastehaugen
    # printer ut spillerens hånd
    # kaller på __getAndCheckInput for å få input fra spilleren
    def __make_move(self):
        for spiller in range(self._spillere):
            self._spiller = spiller
            print(f"Spiller {spiller + 1} sin tur")
            print(f"Øverste kort i kastehaugen: {self._kastehaugen}")
            print(f"Spiller {spiller + 1} sin hånd: {self._haand[spiller]}")
            self.__getAndCheckInput(spiller)

    # starter spillet så lenge harVunnet er False
    def __spill(self):
        while not self._harVunnet:
            self.__clearTerminal()
            self.__hasWon(self._spiller)
            self.__make_move()


# lager en instans av Olsen
olsen = Olsen(Kortstokk, 2)
