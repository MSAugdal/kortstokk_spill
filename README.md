# Python innlevering: Lag et spill

## Oppgaven blir vurdert ut fra følgende kriterier:

-   Struktur, kommentarer og lesbarhet på koden
-   Egen forståelse av koden
-   Hvorvidt programmet fungerer som forventet
-   Brukervennlighet
-   Hvorvidt koden inneholder uhensiktsmessige kodelinjer (DRY-prinsippet)
-   Korrekt innlevering

## Oppgave: kortstokk(middels / høy måloppnåelse)

> En kortstokk i Python kan representeres som en liste på følgende måte:  
> ["A", "2", "3", . . ., "10", "J", "Q", "K"]  
> Sortene representeres som bokstavene K(Kløver), S(Spar), H(Hjerter), R(ruter).  
> For eksempel representeres sparess som "SA" og hjerter seks som "H6".  
> Dere skal lage en Class som lager en kortstokk med 52 kort representert i en liste.  
> Kortstokken skal være stokket(bruk biblioteket «random» for dette).  
> I tillegg skal Class'en inneholde funksjon «haand» som deler ut n kort fra kortstokken og
> returnerer disse som en liste(NB. Husk å fjerne disse kortene fra kortstokken).  
> Class'en skal inneholde funksjonen «del_ut» som deler ut
> p antall hender med n antall kort i hver hand(returnerer en liste av lister).  
> Class'en skal også inneholde funksjonen **`__str__`** som returnerer en tekst string av resterende kortstokk.

## Utfordring: Lag spillet «vri åtter(Olsen)» med følgende regler:

> Hver spiller skal få utdelt en hånd med 5 kort fra en stokket kortstokk.  
> Deretter flippes det øverste kortet fra kortstokken og lager en ny kortstokk der kortene vender oppover.
>
> Hver spiller plasserer et kort oppå den nye kortstokken etter følgende regler:  
> (i) kort med samme farge som kortet som ligger synlig, eller:  
> (ii) kort med samme verdi som kortet som ligger synlig, eller:  
> (iii) kort med verdi åtte kan bestandig spilles. Spilleren som spiller en åtter får da velge fargen på kortet.
>
> En spiller som ikke har noen lovlige kort å spille må trekke inn ett kort.  
> Dette kan gjøres opp til tre ganger per runde før spilleren må melde pass.
>
> Vinneren av spillet er den som først blir kvitt alle kortene.
>
> Bruk Class kortstokk i implementasjon.  
> Presenter for hver spiller når det er deres tur samt en liste av hånden deres.  
> Dere må også presentere for spilleren hvilken kort som ligger øverst på dette tidspunktet.  
> Undersøk om kortet som spilleren spiller er et lovlig kort,  
> og tilby spilleren muligheten til å trekke inn ett kort(men bare tre ganger per runde for hver spiller).  
> Etter at spilleren har trukket inn 3 kort i en runde skal spilleren  
> bli presentert med muligheten til å si pass (ikke spille noen kort).

## Hva gjør applikasjonen min?

Applikasjonen er en versjon av kortspillet "Olsen" eller "Vri åtter".  
Det er ment som et svar på oppgaveteksten jeg skrev inn ovenfor.  
Du kan definere antall spillere ved å skrive inn antall spillere når du "caller" Olsen classen.  
Når du definerer antall hender/spillere kaller Olsen classen Kortstokk classen med antall hender og kort per hånd.  
Programmet lager antall definerte hender med antall definerte kort per hånd og starter spillet.
Spilleren blir presentert med hånden sin, kastehaugen og muligheten til å trekke kort eller passere.

## Hvorfor har jeg valgt å kode slik jeg har kodet?

I denne oppgaven har jeg valgt å bruke objekt orientert programmering mye mer enn jeg testet tidligere.  
Det vil si at jeg har laget funksjoner som kun har en oppgave, og som kan brukes flere ganger, istedenfor å ha flere store funksjoner som gjør mye.  
Jeg så også en video nylig som handlet om såkalte "Never nesters".  
det er kodere som velger å ikke ha loops inne i loops (nesting), bruker "early returns", extraction og aldri bruker mer enn 3-4 nivåer/indents.  
Dette er noe jeg har prøvd å følge i denne oppgaven, og jeg synes det er mye mer oversiktlig og ryddig.  
link til videoen nederst i dokumentet.

jeg bruker også en del "private" funksjoner, som ikke er ment å brukes utenfor klassen, definert ved **`__funksjonsnavn`**.  
Variablene i klassen er også private, definert ved **`_variabelnavn`**.

Det står ikke i oppgaveteksten at vi skal inkludere muligheten for å plassere flere kort samtidig, så jeg har valgt å ikke inkludere det.

Modulene Time og Numpy ble brukt for å få progerammet til å vente og for å shuffle kortstokken.

## Utfordringer på veien til Olsen

Selve programmet og logikken bak hvordan det skal fungere er ganske rett frem:
_Lag hender med et gitt antall kort, lag en kastehaug, en kortstokk og la spilleren trekke, passere og legge ned kort._  
Selv om det ofte ser ut til å være ganske rett frem å programmere det, ender det ofte opp med å være litt mer komplisert😅

Her lister jeg opp et par av utfordringene jeg møtte på under utviklingen:

-   Hvordan skal jeg holde styr på hvor mange ganger spilleren har trukket inn et kort?
-   Hvordan skal jeg strukturere programmet slik at det fungerer med stilen jeg har valgt å bruke?
-   Hva skal være en egen modul og hva kan være bakt sammen?
-   Logikken bak spillet. hvordan skal alt struktureres og hvordan skal "flyten" av spillet være?

Alle utfordringer ovenfor ble etter hvert løst, og programmet er på et punkt hvor jeg føler meg veldig fornøyd med det.

## Hvordan kan du bruke programmet?

Måten du bruker programmet Olsen på er følgende:

1. Last ned alle filene tilhørende programmet (.py filer)
2. Åpne **`main.py`**
3. I linjen: **`Olsen(Kortstokk, 2, 5)`** endrer du **`2`** til antall spillere i spillet, og **`5`** til hvilket som helst antall kort per hånd
4. Pass på at antall hender \* antall kort per hånd ikke er mer enn 52 (Antall kort i kortstokken)
5. **Have fun!** 🥳

## Credits where credits due

Video om "never nesting": https://www.youtube.com/watch?v=CFRhGnuXG-4  
Artikkel om "early return pattern": https://medium.com/swlh/return-early-pattern-3d18a41bba8  
Artikkel om hvordan skrive README: https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/
