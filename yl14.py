#Kirjuta programm, mis küsib kasutajalt failinime kujul “failinimi.ext” 
#(ext - extension - faili laiend) 

filename = input('Name of the file (ex. "failinimi.ext"):')

#ja prindib välja laiendi (“ext”). (str.split)
print ("Faili laiendiks on:", filename.split('.')[-1])
