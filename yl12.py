#Anna muutuja väärtuseks list kolmest oma lemmik puuviljast ja väljasta see
#Väljasta listi esimene väärtus
#Lisa listi lõppu uus puuvili
#Väljasta listi viimane väärtus
#Muuda ühe elemendi väärtust ja väljasta kogu list
#Kontrolli kas väärtus (näiteks õun) eksisteerib listis
#Väljasta listi pikkus
#Eemalda listist element ja väljasta kogu list
#Muuda listi järjekord vastupidiseks
#Sorteeri list ja väljasta
#(jada, list, listi element, listi meetodid)
#https://www.w3schools.com/python/python_lists.asp

top3fruits = ["õun", "banaan", "mango"]
print (top3fruits[0])

top3fruits.append ("apelsin")
print (top3fruits[3])

top3fruits[2] = "ploom"
print (top3fruits)

print (len(top3fruits))

top3fruits.remove("õun")
print (top3fruits)

top3fruits.reverse()
print (top3fruits)

top3fruits.sort()
print (top3fruits)


