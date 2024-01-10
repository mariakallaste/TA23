#(sõne kui list, mitmemõõtmeline ilist - multi dimensional)

#Küsi kasutajalt lemmikloom. Väljasta selle muutuja esimene täht.
pet = input('lemmikloom: ')
print(pet[0])

#Koosta list, mis koosneb kolmest loomast.
#Lisa selle listi lõppu kasutaja sisestatud lemmikloom.
#petlist = ["kass", "hiir", "hobune", pet]

petlist = ["kass", "hiir", "hobune"]
petlist.append(pet)

#Väljasta see lemmikloomade list.
print(petlist)

#Väljasta listi viimase elemendi 2 viimast tähte
print(petlist[-1][-1: -3: -1:])

