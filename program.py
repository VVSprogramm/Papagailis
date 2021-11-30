"""
Programma, kura palīdzēs Tev rūpēties par mājdzīvnieku

30.11.2021.

"""

print("Sveiks!")
print("Ja Tev ir mājdzīvnieks un ir radusies situācija, ka kādam ir nepieciešams to pieskatīt... ")
print("Vai arī Tu pieskatīsi kāda mājdzīvnieku....")
print("Šī programma ir priekš tevis!")
print("-"*50)

maj_dz_sr = ["Kaķis","Suns","Papagailis","Bruņurupucis","Zivtiņas"]

print("Izvēlies savu lomu: Īpašnieks(I) vai Pieskatītājs(P)")
loma = input()


if loma == "I":
    print()
elif loma == "P":
    print("Izvēlies mājdzīvnieku:")
    for dz in maj_dz_sr:
        print(dz)
    piesk_dz = input("Ieraksti pieskatāmā dzīvnieka nosaukuma pirmo burtu: ")
    if piesk_dz == "K":
        




