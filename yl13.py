#Küsi kasutajalt lemmikloom. Väljasta selle muutuja esimene täht.
#Koosta list, mis koosneb kolmest loomast.
#Lisa selle listi lõppu kasutaja sisestatud lemmikloom.
#Väljasta see lemmikloomade list.
#Väljasta listi viimase elemendi viimane täht.
#(sõne kui list, mitmemõõtmeline ilist - multi dimensional)


pet = input('lemmikloom: ')
print(pet[0])

petlist = ["kass", "hiir", pet]
print(petlist)
print(petlist[2][-1])

