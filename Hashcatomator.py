################################################
#Hashcat Dictionary Script - Stand 09.03.2020
#Malte Woischwill
#Script für systematischen Wordlist-Attacks auf
#True- und Veracrypt Volumes mittels Hashcat
################################################
import os

def hashcat(method, dicLoc, file):
    for dict in os.listdir(wordlistLocation):
        command = ["hashcat64",     #64-bit Hashcat
                    "--status",     #selbstständiges Update der Comandozeile
                    "-a","0",       #strait Attack
                    "-m",method,    #für Methoden siehe Zeile 39-50
                    file,
                    str(dicLoc) + "\\" + str(dict)]
        print(" ".join(command))
        os.system(" ".join(command))

while True:
    print("Hashcat True-/Veracrypt Script:")
    print("-"*30)
    hcLoc = input("Hashcat Location: ") #CMD muss im Hashcat Verzeichnis laufen
    file = input("Speicherort der Datei: ") + "\\" + input("Dateiname: ")
    while True:
        hashType = input("(T)ruecrypt oder (V)eracrypt?: ").lower()
        if hashType in ["t", "v"]:
            break
        else:
            print("Ungültige Auswahl!")
    #Alle Wortlisten in dem Ordner werden nacheinander abgearbeitet
    wordlistLocation = input("Speicherort der Wortlisten: ") 


    try:
        os.chdir(hcLoc)
    except:
        print("Ungültiger Pfad für Hashcat!")
        continue

    if hashType in ["t"]:
        try:
            for i in range(1,5):        #Hashalgorythmen
                for j in range(1,4):    #Verschlüsselungsalgorithmen
                    hashcat("62"+ str(i) + str(j), wordlistLocation, file)
        except:
            print("\nKontrollieren Sie die Pfadangaben!\n")
            continue
    elif hashType in ["v"]:
        for i in range(1,8):            #Hashalgorithmen
            for j in range(1,4):        #Verschlüsselungsalgorithmen
                hashcat("137"+ str(i) + str(j), wordlistLocation, file)
    if input("Nochmal? ") == "n":
        break