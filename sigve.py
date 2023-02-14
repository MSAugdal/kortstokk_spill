from random import choice
alternativ = ["stein", "saks", "papir"]
ai_valg = choice(alternativ)
bruker_valg = input("Skriv inn stein, saks eller papir: ")
if bruker_valg == ai_valg:
    print("Uavgjort!")
elif bruker_valg == "stein" and ai_valg == "saks":
    print("Du vant!")
