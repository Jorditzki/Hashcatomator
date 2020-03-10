################################################
#Hashcatomator - Stand 09.03.2020
#Malte Woischwill
#Script for automated wordlist-attacks on
#True- and Veracrypt volumes via Hashcat
################################################
import os

def hashcat(method, dicLoc, file, rules):
    for dict in os.listdir(wordlistLocation):
        command = ["hashcat64",                 #64-bit Hashcat
                    "--status",                 #automated status updates
                    rules,
                    "-m",method,                #for methods see line 39-50
                    file,
                    str(dicLoc) + "\\" + str(dict)]
        print(" ".join(command))
        os.system(" ".join(command))

while True:
    print("Hashcat True-/Veracrypt Script:")
    print("-"*30)

    #Hashcat directory
    while True:
        hcLoc = input("Hashcat Location: ")
        if os.path.exists(hcLoc):
            break
        else:
            print("Ungueltiger Pfad!")
    #Directory of hash to attack
    while True:
        file = input("Speicherort der Datei: ") + "\\" + input("Dateiname: ")
        if os.path.isfile(file):
            break
        else:
            print("Datei nicht vorhanden!")
    #Wordlist directory
    while True:
        wordlistLocation = input("Speicherort der Wortlisten: ") 
        if os.path.exists(wordlistLocation):
            break
        else:
            print("Ungueltiger Pfad!")    
    #Truecrypt or Veracrypt
    while True:
        hashType = input("(T)ruecrypt oder (V)eracrypt?: ").lower()
        if hashType in ["t", "v"]:
            break
        else:
            print("Ungueltige Auswahl!")
    print("""Moegliche Regeln:
             [1]best64
             [2]combinator
             [3]generated
             [4]leetspeak
             [5]rockyou-3000""")

    ruleChoice = input("Welche Regeln anwenden? (Zahlen hintereinander angeben):")
    rules = ""

    for rule in str(ruleChoice):
        rules += "-r rules\\"
        if rule in ["1"]:
            rules += "best64"
        elif rule  in ["2"]:
            rules += "combinator"
        elif rule in ["3"]:
            rules += "generated"
        elif rule in ["4"]:
            rules += "leetspeak"
        elif rule in ["5"]:
            rules += "rockyou-3000"
        rules += ".rule "
    

    os.chdir(hcLoc)
    

    if hashType in ["t"]:
        try:
            for i in range(1,5):        #Hashalgorythm
                for j in range(1,4):    #Encryptionalgorithm
                    hashcat("62"+ str(i) + str(j), wordlistLocation, file, rules)
        except:
            print("\nKontrollieren Sie die Pfadangaben!\n")
            continue
    elif hashType in ["v"]:
        for i in range(1,8):            #Hashalgorithm
            for j in range(1,4):        #Encryptionalgorithm
                hashcat("137"+ str(i) + str(j), wordlistLocation, file, rules)
    if input("Vorgaenge abgeschlossen!\nErneut ausführen? ") == "n":
        break
