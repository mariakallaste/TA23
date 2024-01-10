#Kirjuta programm, mis küsib kasutajalt nime, tervitab teda nimepidi, küsib kasutajalt elukoha, kui elukoht on Saaremaa, siis väljastab 
#mingi kommentaari, küsib kasutajalt vanuse, kui vanus on väiksem kui 18, siis ütleb, et kasutaja on liiga noor, et autot juhtida, 
#kui vanus on 18, siis õnnitleb täisealiseks saamise puhul, kui kasutaja on vanem kui 18, siis ütleb, et kasutaja võib autot juhtida. 
#(sõne - string)

name = input("nimi: ")
print("Tere,", name, "!")

location = input("elukoht: ").lower()
if "saaremaa" in location:
    print("RÖÖM!")

age = int(input("vanus:"))
if age < 18:
    print("Oled liiga noor, et autot juhtida.")
elif age == 18:
    print("Palju õnne täisealiseks saamise puhul! Võid autot juhtida.")
else:
    print("Võid autot juhtida.")
