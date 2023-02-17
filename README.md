# Oppgave: kortstokk(middels / høy måloppnåelse)

> "En kortstokk i Python kan representeres som en liste på følgende måte:
> ["A", "2", "3", . . ., "10", "J", "Q", "K"]
> Sortene representeres som bokstavene K(Kløver), S(Spar), H(Hjerter), R(ruter).
> For eksempel representeres sparess som "SA" og hjerter seks som "H6".
> Dere skal lage en Class som lager en kortstokk med 52 kort representert i en liste.
> Kortstokken skal være stokket(bruk biblioteket «random» for dette).
> I tillegg skal Class'en inneholde funksjon «haand» som deler ut n kort fra kortstokken og
> returnerer disse som en liste(NB. Husk å fjerne disse kortene fra kortstokken).
> Class'en skal inneholde funksjonen «del_ut» som deler ut
> p antall hender med n antall kort i hver hand(returnerer en liste av lister).
> Class'en skal også inneholde funksjonen `__str__` som returnerer en tekst string av resterende kortstokk."

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
> bli presentert med muligheten til å si pass (ikke spille noen kort)."

## Hvorfor har jeg valg å kode slik jeg har kodet?

I denne oppgaven har jeg valgt å bruke objekt orientert programmering mye mer enn jeg testet tidligere.
Det vil si at jeg har laget funksjoner som kun har en oppgave, og som kan brukes flere ganger, istedenfor å ha flere store funksjoner som gjør mye.
Jeg så også en video nylig som handlet om såkalte "Never nesters".
det er kodere som velger å ikke ha loops inne i loops (nesting), bruker "early returns", extraction og aldri bruker mer enn 3-4 nivåer/indents.
Dette er noe jeg har prøvd å følge i denne oppgaven, og jeg synes det er mye mer oversiktlig og ryddig.
link til videoen: https://www.youtube.com/watch?v=CFRhGnuXG-4

jeg bruker også en del "private" funksjoner, som ikke er ment å brukes utenfor klassen, definert ved \_\_funksjonsnavn.
Variablene i klassen er også private, definert ved \_variabelnavn.

Det står ikke i oppgaveteksten at vi skal inkludere muligheten for å plassere flere kort samtidig, så jeg har valgt å ikke inkludere det.
