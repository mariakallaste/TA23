#Kirjutada programm, mis kontrollib, kas antud positiivne täisarv on liig- või lihtaasta number. 
#Aasta on liigaasta kui ta jagub neljasajaga või jagub neljaga ja ei jagu sajaga.

year = int(input("Sisesta aasta: "))
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print(str(year) + "on liigaasta")
else:
    print(str(year), "on lihtaasta")

