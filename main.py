import translator as tr

t = tr.Translator()

while(True):
    t.printMenu()
    t.loadDictionary("dictionary.txt")

    # Add input control here!
    txtIn = input("Cosa intendi effettuare (1, 2, 3, 4 o 5)? ")

    if int(txtIn) == 1: #Aggiungi una nuova parola al dizionario con relativa traduzione
        aliena = input("Inserisci la parola in lingua aliena: ")
        italiana= input("Inserisci la parola italiana che la traduce: ")
        tupla = (aliena.lower(),italiana.lower())
        t.handleAdd(tupla)

    if int(txtIn) == 2:
        parola = input("Di quale parola intendi cercare la traduzione: ")
        if(parola.isalpha()==True and parola.lower() in t.dizionario.diz.keys()):
            print(f"La traduzione di {parola.lower()} è {t.dizionario.translate(parola.lower())}")
        else:
            print(f"La parola non è contenuta all'interno del mio dizionario")

    if int(txtIn) == 3:
        parolawild=input("Inserisci la parola di cui intendi cercare la traduzione, contenente un carattere speciale: ")
        t.dizionario.translateWordWildCard(parolawild)

    if int(txtIn) == 4:
        for p in t.dizionario.diz.keys():
            print(f"{p} --> {t.dizionario.diz[p]}")

    if int(txtIn) ==5:
        break