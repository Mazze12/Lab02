import dictionary as dt

class Translator:


    def __init__(self):
        self.dizionario =None

    def printMenu(self):
        print(f"-------------------------------------")
        print(f"     Translator Alien-Italian")
        print()
        print(f"------------------------------------")
        print(f"1. Aggiungi nuova parola")
        print(f"2. Cerca una traduzione")
        print(f"3. Cerca una wildcard")
        print(f"4. Stampa tutto il dizionario")
        print(f"5. Exit")
        print(f"------------------------------------")
        print()

    def loadDictionary(self, filename):
        # dict is a string with the filename of the dictionary
        d = dt.Dictionary(filename)
        self.dizionario = d

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        aliena =entry[0]
        italiana = entry[1]
        self.dizionario.addWord(aliena, italiana)


    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        #non ne ho capito l'utilità
        aliena = query[0]
        italiana =self.dizionario.diz[aliena]
        return italiana

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass