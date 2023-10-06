# Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud arvust maksimumi 
# (ära kasuta max funktsiooni). (loogikatehted - logic operators)

a = int(input("Sisesta arv a: "))
b = int(input("Sisesta arv b: "))
c = int(input("Sisesta arv c: "))

if a > b and a > c:
    print ("maksimum on", a)

elif b > c:
    print ("maksmimum on", b)

else: 
    print ("maksmimum on", c)


