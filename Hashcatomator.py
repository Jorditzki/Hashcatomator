################################################
#Hashcatomator - Stand 09.03.2020
#Malte Woischwill
#Script for automated wordlist-attacks on
#True- and Veracrypt volumes via Hashcat
################################################
import os

def hashcat(method, dicLoc, file):
    for dict in os.listdir(wordlistLocation):
        command = ["hashcat64",                 #64-bit Hashcat
                    "--status",                 #automated status updates
                    "-r rules/best64.rule",
                    "-r rules/generated.rule",
                    "-m",method,                #for methods see line 39-50
                    file,
                    str(dicLoc) + "\\" + str(dict)]
        print(" ".join(command))
        os.system(" ".join(command))

while True:
    print("Hashcat True-/Veracrypt Script:")
    print("-"*30)
    hcLoc = input("Hashcat Location: ")         #CMD is gonna switch do HC directory
    file = input("Speicherort der Datei: ") + "\\" + input("Dateiname: ")
    while True:
        hashType = input("(T)ruecrypt oder (V)eracrypt?: ").lower()
        if hashType in ["t", "v"]:
            break
        else:
            print("Ungültige Auswahl!")
    #Work your way through all given Wordlists
    wordlistLocation = input("Speicherort der Wortlisten: ") 


    try:
        os.chdir(hcLoc)
    except:
        print("Ungültiger Pfad für Hashcat!")
        continue

    if hashType in ["t"]:
        try:
            for i in range(1,5):        #Hashalgorythm
                for j in range(1,4):    #Encryptionalgorithm
                    hashcat("62"+ str(i) + str(j), wordlistLocation, file)
        except:
            print("\nKontrollieren Sie die Pfadangaben!\n")
            continue
    elif hashType in ["v"]:
        for i in range(1,8):            #Hashalgorithm
            for j in range(1,4):        #Encryptionalgorithm
                hashcat("137"+ str(i) + str(j), wordlistLocation, file)
    if input("Nochmal? ") == "n":
        break
