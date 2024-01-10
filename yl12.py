#(jada, list, listi element, listi meetodid)
#https://www.w3schools.com/python/python_lists.asp

#Anna muutuja väärtuseks list kolmest oma lemmik puuviljast ja väljasta see
top3fruits = ["õun", "banaan", "mango"]
print (top3fruits)

#Väljasta listi esimene väärtus
print (top3fruits[0])

#Lisa listi lõppu uus puuvili
top3fruits.append ("apelsin")

#Väljasta listi viimane väärtus
print ("Viimane:len(top3fruits)-1")

#Muuda ühe elemendi väärtust ja väljasta kogu list
top3fruits[2] = "ploom"
print (top3fruits)

#Kontrolli, kas väärtus, nt. "õun", eksisteerib listis
test= input("kontrolli, kas listis sisaldub 'õun': ")
if test in top3fruits:
 print ("On listis")
else:
 print ("Ei ole listis")


#Väljasta listi pikkus
print (len(top3fruits))

#Eemalda listist element ja väljasta kogu list
top3fruits.remove("õun")
print (top3fruits)

#Muuda listi järjekord vastupidiseks
top3fruits.reverse()
print (top3fruits)

#Sorteeri list ja väljasta
print (sorted(top3fruits))



