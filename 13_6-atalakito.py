# -*- coding: Utf-8 -*-
# A 13.6-os struktúrát alakítja át egy soros,
# excelben kezelhetőre.

import os, platform


# Képernyő törlés
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

ForrasF = raw_input("\n" + "A forras file neve: ")
ffile = open(ForrasF, 'r')
# CelF = raw_input("A cél file neve: ")
CelF = ""

# Fejléc manipulálás
for i in range(1, 11):
    sor = ""
    sor = ffile.readline().replace("\n", ";")
    if i == 4:
        for j in range(24, 42):
            CelF = CelF + sor[j]

# A tételkód lesz a file neve
cfile = open(CelF.strip() + ".txt", 'w')
# cfile.write("Szülő tétel: " + CelF + "\n")

#Fejléc kiiratása a file-ba
cfile.write("Szint" + ";" + "Beepulo tetel" + ";" + "Megnevezes" + ";" + "Beepulo" + ";" + "ME" + ";" + "Fn  T Ki" + ";" + "\n")

# Itt indul a feldolgozás izzasztó folyamata...
while True:
    keres = ""
    sor = ""
    sor = ffile.readline().replace("\n", ";")
    if not sor:
        break
    if sor[0:1] != " " and sor[8:9] != " " and sor[27:28] != " " and sor[0:1] != ";":
        cfile.write("\n" + sor[0:7].strip() + ";" + sor[8:25].strip() + ";" + sor[27:52].strip() + ";" + sor[53:65].strip() + ";" + sor[65:67].strip() + ";" + sor[69:78].strip() + ";")
    if sor[8:9] == " " and sor[27:28] != " ":
        cfile.write(sor[27:52].strip() + ";")
#    if sor == ";":
#        cfile.write("...azta...")


# File-ok bezárása
cfile.write("\n" + "\n" + "\n" + "Vegeztem a feldolgozassal...")
ffile.close()
cfile.close()

# Képernyő kiiratás, ha végzett  feldolgozással
print("\n" + "Kesz a feldolgozas, beemelheto Excelbe, --- >")
print("            tagolt, pontosvesszovel elvalasztott..." + "\n")
print("\n")
print("Az elkeszult file neve: " + CelF.strip() + ".txt" + "\n")
print("\n")
raw_input("Kilepes <ENTER> billentyu lenyovasaval lehetseges...")
