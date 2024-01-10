#(stringi meetodid, list)

#Kirjuta programm, mis küsib kasutajalt sisendina stringi.
string = input('sisend:')

#Eemalda selle sisendi algusest ja lõpust tühikud.
string = string.strip()

#String peab vastama tingimustele, et selles on vähemalt seitse sümbolit 
#ja et sümbolite arv on paarituarvuline.
if len(string) >= 7 and len(string) % 2 == 1:
 
 #Väljasta selle stringi kolm keskmist sümbolit.
 middle = len(string) // 2
 
 #print (f'sisendi kolm keskmist sümbolit:{string[middle -1], string[middle], string[middle +1]}')

 print(string[middle-1: middle+2])


else:
 print ('Sisend peab sisaldama vähemalt seitset sümbolit ja sümbolite arv peab olema paarituarvuline')
