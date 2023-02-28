from time import sleep


class Olsen:
    # initialiserer klassen med en kortstokk, antall spillere og antall kort per hånd
    # kortstokken blir delt ut til alle spillere
    # det øverste kortet i kortstokken blir lagt i kastehaugen
    # spiller 0 sin tur
    # draws blir satt til en dictionary med spiller som nøkkel og antall draws som verdi
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
        self._draws = {spiller: 0 for spiller in range(spillere)}

        self.__clearTerminal()
        self.__make_move()

    # tømmer terminalen med en escape sequence
    # \033c er ESC c i ASCII, og vil tømme terminalen
    def __clearTerminal(self) -> None:
        print("\033c")

    # bytter sort til det øverste kortet i kastehaugen ved å endre den første bokstaven i kortet i kastehaugen
    def __byttSort(self, kort) -> None:
        self.__clearTerminal()
        print(f"kortet du spilte var: {kort}")
        nySort = input("Skriv inn en ny sort [K, S, H, R]: ").upper()
        if nySort not in ["K", "S", "H", "R"]:
            print("Ugyldig valg...")
            sleep(1)
            self.__byttSort(kort)
            return
        self._kastehaugen = nySort + "8"

    # sjekker om spilleren har kortet i hånden
    # fjerner kortet fra hånden og legger det i kastehaugen hvis spilleren har kortet
    # forrige spilte kort blir lagt til i kortstokken slik at den aldri går tom for kort
    # hvis ikke, blir spilleren bedt om å prøve igjen
    # sjekker om kortet er et 8, og kaller funksjonen "_byttSort" hvis det er det
    def __checkMove(self, valg, spiller) -> None:
        if valg not in self._haand[spiller]:
            self.__clearTerminal()
            print("Du har ikke dette kortet i hånden din")
            sleep(1)
            self.__getAndCheckInput(spiller)
            return
        if valg[0] != self._kastehaugen[0]:
            if valg[1:] == self._kastehaugen[1:]:
                self._kortstokk.insert(0, self._kastehaugen)
                self._kastehaugen = self._haand[spiller].pop(self._haand[spiller].index(valg))
            self.__clearTerminal()
            print(f"Du kan ikke spille {valg}")
            sleep(1)
            self.__clearTerminal()
            return
        if valg[1] == "8":
            self.__byttSort(valg)
            return
        self._kortstokk.insert(0, self._kastehaugen)
        self._kastehaugen = self._haand[spiller].pop(self._haand[spiller].index(valg))

    # legger til et kort i hånden til spilleren som skrev inn "draw" ved å trekke fra kortstokken
    def __draw(self, spiller) -> None:
        self._haand[spiller].append(self._kortstokk.pop())
        self._draws[spiller] += 1

    # viser alle muligheter til spilleren (trekke kort, spille kort og pass)
    # om kortstokken er tom, kan ikke spilleren trekke kort
    # forteller spilleren om det er mulig å trekke kort eller ikke og hvor mange ganger spilleren kan trekke kort
    # forteller spilleren at det er mulig å passere om draw er skrevet 3 ganger
    def __showOptions(self, spiller) -> None:
        print(f"Spiller {spiller + 1} sin tur")
        print(f"Øverste kort i kastehaugen: {self._kastehaugen}")
        print(f"Spiller {spiller + 1} sin hånd: [{', '.join(self._haand[spiller])}]")
        if len(self._kortstokk) == 0:
            print("Kortstokken er tom, du kan ikke trekke inn et kort")
            return
        if self._draws[spiller] < 3:
            print(f"Du kan trekke inn et kort med 'draw' ({3 - self._draws[spiller]} ganger igjen)")
            return
        print(f"Du kan passere med 'pass'")

    # tømmer terminalen og viser alle muligheter til spilleren
    # henter input fra spilleren
    # sjekker om input er tom
    # sjekker om input er "draw" og sier at kortstokken er tom om kortstokken er tom
    # sjekker om inputen er "draw" og kaller funksjonen "_draw" med spiller som argument
    # sjekker om inputen er "pass" og tømmer terminalen for å la spillet fortsette om draws == 3
    # sjekker om inputen er gyldig (eks: K2, H10, S3, RQ og ikke K22, H1 eller 1K)
    # sjekker at første karakter er en bokstav, og at andre karakter er en bokstav eller tall
    # hvis inputen ikke er gyldig, blir spilleren bedt om å prøve igjen
    # hvis gyldig, kaller den funksjonen "_checkMove" med inputen og spiller som argument
    def __getAndCheckInput(self, spiller) -> None:
        self.__clearTerminal()
        self.__showOptions(spiller)
        valg = input("Skriv et valg [eks: K2, draw eller pass]\n>>> ").upper()
        if len(valg) == 0:
            self.__clearTerminal()
            print("Du må skrive noe")
            sleep(1)
            self.__getAndCheckInput(spiller)
            return
        if valg == "DRAW" and len(self._kortstokk) == 0:
            self.__clearTerminal()
            print("Kortstokken er tom, du kan ikke trekke inn et kort")
            sleep(1)
            self.__getAndCheckInput(spiller)
            return
        if valg == "DRAW" and self._draws[spiller] < 3:
            self.__draw(spiller)
            self.__getAndCheckInput(spiller)
            return
        if valg == "PASS" and self._draws[spiller] == 3:
            self.__clearTerminal()
            print(f"Spiller {spiller + 1} har passert")
            sleep(1)
            self.__clearTerminal()
            return
        if not valg[0] in ["K", "S", "H", "R"] or not valg[1:] in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
            self.__clearTerminal()
            print("Feil syntaks. Prøv igjen")
            sleep(1)
            self.__getAndCheckInput(spiller)
            return
        self.__checkMove(valg, spiller)

    # sjekker om spilleren har vunnet
    # hvis spilleren har vunnet blir terminalen tømt og spilleren som har vunnet blir printet ut
    # spillet avsluttes
    def __hasWon(self, spiller) -> None:
        if len(self._haand[spiller]) == 0:
            self.__clearTerminal()
            print(f"Spiller {spiller + 1} har vunnet!")
            sleep(3)
            quit()

    # forteller spilleren at det er deres tur
    # printer ut øverste kort i kastehaugen
    # printer ut spillerens hånd
    # kaller på __getAndCheckInput for å få input fra spilleren
    def __make_move(self) -> None:
        for spiller in range(self._spillere):
            self.__hasWon(spiller)
            self.__clearTerminal()
            self.__getAndCheckInput(spiller)
            self._draws[spiller] = 0
        self.__make_move()
