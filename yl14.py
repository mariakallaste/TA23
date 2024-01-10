#Kirjuta programm, mis küsib kasutajalt failinime kujul “failinimi.ext” (ext - extension - faili laiend) ja prindib välja laiendi (“ext”). (str.split)

filename = input('name of the file:')

print(filename.split('.')[1])
