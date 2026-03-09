class Dictionary:
    #il dizionario è composto solo da un attributo che rappresenta il dizionario
    #nel quale in chiave avrò le varie parole aliene e come valori corrispondenti le
    #rispettive parole italiane
    def __init__(self, filename):
        dizionario = self.leggi_file(filename)
        self.diz=dizionario #il valore inserito sarà un dizionario contenente i vari valori

    def leggi_file(self, filename):
        dizionario={}
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                parole = line.strip().split(" ")
                aliena = parole[0]
                italiana = parole[1]
                dizionario[aliena] = italiana
        return dizionario

    def addWord(self, aliena, italiana):
        if(aliena.lower() not in self.diz.keys()):
            self.diz[aliena] = italiana
            #Aggiungo anche la parola nel file di testo
            with open('dictionary.txt', 'a', encoding='utf-8') as f:
                f.write(f"{aliena.lower()} {italiana.lower()}\n")
        else:
            self.addWordExist(aliena, italiana)
            print(f"Le varie traduzioni della parola inserita sono: ")
            for trad in self.diz[aliena]:
                print(trad)

    def addWordExist(self, aliena, italiana):
        with open('dictionary.txt', 'a', encoding='utf-8') as f:
            f.write(f"{aliena.lower()} {italiana.lower()}\n")
        #devo inserire all'interno del dizionario la parola associandola a quella gia esistente
        if type(self.diz[aliena])==str and italiana != self.diz[aliena]:
            lista = self.diz[aliena].split("-")
            lista.append(italiana)
            self.diz[aliena]=lista
        elif type(self.diz[aliena])!= str and italiana not in self.diz[aliena]: #Il valore è gia stato convertito in stringa
            self.diz[aliena].append(italiana)

    def translate(self, aliena):
        return self.diz[aliena]

    def translateWordWildCard(self, pattern):
        """
        Cerca parole nel dizionario che corrispondono al pattern con wildcard '?'
        '?' può rappresentare qualsiasi lettera dell'alfabeto
        """
        risultati = []
        traduzioni= []
        for parola in self.diz.keys():
            if len(parola) != len(pattern):
                continue

            corrisponde = True
            for i in range(len(pattern)):
                if pattern[i] != '?' and pattern[i].lower() != parola[i].lower():
                    corrisponde = False
                    break
            if corrisponde:
                risultati.append(parola)
                traduzioni.append(self.diz[parola])
        #giunti a questo punto avremo una lista che contiene tutte le paroleche corrispondono
        for corr in range(len(risultati)):
            print(f"{risultati[corr]} --> {traduzioni[corr]}")

