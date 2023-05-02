import random
import datetime

def vdir(obj):
    return [x for x in dir(obj) if not x.startswith('__')]

# Parent class
class Konto():
    def __init__(self, kontostand, pin, kontonummer, kontoart, vorname, nachname):
        self.__kontostand = kontostand
        self.kontoAuszug = "hallo, ich bin dein Kontoauszug"
        self.__pin = pin
        self.__kontonummer = kontonummer
        self.__kontoart = kontoart
        self.__vorname = vorname
        self.__nachname = nachname
        self.__dispo = 500
        self.__limit = 0
        self.__dispolimit = 0
        self.__auszug = []
        self.__transaktionen = []
    
    #Funktionen der Parent class

    def überweisen(Konto, betrag, Konto2):
        print("Ihr jetziger Kontostand beträgt:", str(Konto.getKontostand()))
        Konto2.einzahlen(betrag)
        Konto.auszahlen(betrag)
        print("Sie haben", betrag, "€ überwiesen")
        print("Ihr neuer Kontostand ist:", str(Konto.getKontostand()))

    def einzahlen(self, betrag):
        if betrag < 0:
            print("Der Betrag darf kein Minus enthalten")
        else:
            pass
            print("Ihr jetziger Kontostand beträgt:", str(self.getKontostand()))
            self.__kontostand = self.__kontostand + betrag
            print("Sie haben", betrag, "€ eingezahlt")
            print("Ihr neuer Kontostand ist:", str(self.getKontostand()))
            jetzt = datetime.datetime.now().strftime("%d.%m %H:%M")
            self.__transaktionen.append(["einzahlung", betrag, "Um ", jetzt])
        
    def auszahlen(self, betrag):
        print("Ihr jetziger Kontostand beträgt:", str(self.getKontostand()))
        self.__limit = self.__limit + betrag
        if betrag < 0:
            print("Der Betrag darf kein Minus enthalten")
        else:
            pass
            Wert = self.__kontostand - betrag
            if Wert < 0 and self.__limit > 999:
                print("Der eingegebene Wert ist größer als ihr Kontostand oder sie haben ihr Limit erreicht")
            else:
                self.__kontostand = self.__kontostand - betrag
                jetzt = datetime.datetime.now().strftime("%d.%m %H:%M")
                self.__transaktionen.append(["Auszahlung", betrag, "Um ", jetzt])
                print("Es wurden ", betrag, " € ausgezahlt!")
                print("Ihr neuer Kontostand ist:", str(self.getKontostand()))

    def getKontoauszug(self):
          print("----- Kontoauszug -----")
          for transaktion in self.__transaktionen:
               print("- " + str(transaktion[0]) + ": " + str(transaktion[1]) + " EUR " + str(transaktion[2]) + str(transaktion[3]))
          print("-----------------------")
        
    def setPin(self, neuerpin):
        self.__pin = neuerpin
       
    def getPin(self):
        return(self.__pin)
         
    def setKontostand(self, neuer_Kontostand):
        self.__kontostand = neuer_Kontostand
        
    def getKontostand(self):
        return self.__kontostand

    def setKontonummer(self, Kontonummer):
        self.__kontonummer = Kontonummer
        
    def getKontonummer(self):
        return self.__kontonummer

#Child classes
class Giro(Konto):
    def __init__(self, kontostand, pin, kontonummer, kontoart, vorname, nachname):
        #Callt das innit der Konto Klasse
        super().__init__(kontostand,pin,kontonummer,kontoart,vorname,nachname)

class Dispo():
    def __init__(self, kontostand, pin, kontonummer, kontoart, vorname, nachname):
        #Callt das innit der Konto Klasse
        super().__init__(kontostand,pin,kontonummer,kontoart,vorname,nachname)
        self.__dispolimit = 0
        self.__dispo = 500
        self.__limit = 0
        self.__dispolimit = 0

class Sparbuch():
    def __init__(self, kontostand, pin, kontonummer, kontoart, vorname, nachname):
        #Callt das innit der Konto Klasse
        super().__init__(kontostand,pin,kontonummer,kontoart,vorname,nachname)
        self.__dispo = 500
        self.__limit = 0
        self.__dispolimit = 0
        self.__auszug = []
        self.__transaktionen = []
        self.__zinssatz = 3.5


#Funktionen
    def überweisen(Konto, betrag, Konto2):
        print("Ihr jetziger Kontostand beträgt:", str(Konto.getKontostand()))
        Konto2.einzahlen(betrag)
        Konto.auszahlen(betrag)
        print("Sie haben", betrag, "€ überwiesen")
        print("Ihr neuer Kontostand ist:", str(Konto.getKontostand()))

    def einzahlen(self, betrag):
        if betrag < 0:
            print("Der Betrag darf kein Minus enthalten")
        else:
            pass
            print("Ihr jetziger Kontostand beträgt:", str(self.getKontostand()))
            self.__kontostand = self.__kontostand + betrag
            print("Sie haben", betrag, "€ eingezahlt")
            print("Ihr neuer Kontostand ist:", str(self.getKontostand()))
            jetzt = datetime.datetime.now().strftime("%d.%m %H:%M")
            self.__transaktionen.append(["einzahlung", betrag, "Um ", jetzt])
        
    def auszahlen(self, betrag):
        print("Ihr jetziger Kontostand beträgt:", str(self.getKontostand()))
        self.__limit = self.__limit + betrag
        if betrag < 0:
            print("Der Betrag darf kein Minus enthalten")
        else:
            pass
            Wert = self.__kontostand - betrag
            if Wert < 0 and self.__limit > 999:
                print("Der eingegebene Wert ist größer als ihr Kontostand oder sie haben ihr Limit erreicht")
            else:
                self.__kontostand = self.__kontostand - betrag
                jetzt = datetime.datetime.now().strftime("%d.%m %H:%M")
                self.__transaktionen.append(["Auszahlung", betrag, "Um ", jetzt])
                print("Es wurden ", betrag, " € ausgezahlt!")
                print("Ihr neuer Kontostand ist:", str(self.getKontostand()))

    def getKontoauszug(self):
          print("----- Kontoauszug -----")
          for transaktion in self.__transaktionen:
               print("- " + str(transaktion[0]) + ": " + str(transaktion[1]) + " EUR " + str(transaktion[2]) + str(transaktion[3]))
          print("-----------------------")
        
    def setPin(self, neuerpin):
        self.__pin = neuerpin
       
    def getPin(self):
        return(self.__pin)
         
    def setKontostand(self, neuer_Kontostand):
        self.__kontostand = neuer_Kontostand
        
    def getKontostand(self):
        return self.__kontostand

    def setKontonummer(self, Kontonummer):
        self.__kontonummer = Kontonummer
        
    def getKontonummer(self):
        return self.__kontonummer


#Probe Konten
Konto1 = Konto(1000,1234,1234567, "Giro", "ich", "Lange")
Konto2 = Konto(12,1001,737828, "Giro", "TaNiHA", "Dachner")
Konto3 = Konto(12000,1003,137828, "Giro", "Tay", "Herbst")
kontoliste = [Konto1,Konto2,Konto3]
zaehler = 0
zaehlerKonto = 2


#Anmeldung und Kontoerstellung
while(True):
    print("Bitte geben sie alle Informationen fuer ihr Bankkonto an :")

    auswahl = input("Wollen Sie ein Konto erstellen? (j/n) ")
    if (auswahl == "j"):
        print("Vielen dank, dass sie sich für uns entschieden haben,")
        print("Wir werden sie nun durch die erstellung ihres eigenen Kontos führen")

    else:
        print("Sind sie sich sicher?")
        antwort = input("Möchten sie die Erstellung ihres Kontos wiederholen?:")
        if antwort == "j":
            pass
        else:
            break
    
    Kontostand = 0
    Pin = int(input("geben sie einen pin mit 4 Zahlen ein, wir empfehlen keine *code muster* zu verwenden: "))
    Kontonummer = (random.randint(1000,9999))
    KontoB = int(input("Bite wählen sie zwischen GiroKonto(1) DispoKonto(2) Sparbuch(3): "))

    KontoZahl = "Konto" + str((random.randint(1,1000)))
    print(KontoZahl)
    if KontoB == 1:
        KontoArt = Giro

    if KontoB ==2:
        KontoArt = Dispo

    if KontoB ==3:
        KontoArt = Sparbuch

    vorname = input("Bitte geben Sie Ihren Vornamen ein: ")
    zinssatz= 3.5
    nachname = input("Bitte geben Sie Ihren Nachnamen ein: ")

    if KontoB == 1:
        print(KontoZahl)
        KontoZahl = KontoArt(Kontostand,Pin,Kontonummer,KontoArt,nachname,vorname)
        print("Wilkommen bei Tammo inc, Ihre Kontonummer ist", Kontonummer, " Und sie sind", "Ihr Passwort lautet", Pin)
        kontoliste.append(KontoZahl) # Fügt den Kontonamen zur Kontoliste hinzu
    if KontoB == 2:
        KontoZahl = KontoArt(Kontostand,Pin,Kontonummer,KontoArt,nachname,vorname)
        print("Wilkommen bei Tammo inc, Ihre Kontonummer ist", Kontonummer, " Und sie sind", KontoZahl, "Ihr Passwort lautet", Pin)
        kontoliste.append(KontoZahl) # Fügt den Kontonamen zur Kontoliste hinzu

    if KontoB ==3:
        KontoZahl = KontoArt(Kontostand,Pin,Kontonummer,KontoArt,nachname,vorname,zinssatz)
        print("Wilkommen bei Tammo inc, Ihre Kontonummer ist", Kontonummer, " Und sie sind", KontoZahl, "Ihr Passwort lautet", Pin)
        kontoliste.append(KontoZahl) # Fügt den Kontonamen zur Kontoliste hinzu

    

 #Eingabe pin
pin = input("Bitte geben Sie Ihren Pin ein: ")

#prüfe, ob das Konto existiert
login = False
currentKonto = None
for x in kontoliste:
    if int(pin) == int(x.getPin()):
        login = True
        currentKonto = x
        
if(login):
    print("Die Anmeldung war erfolgreich")
    #Test Befehle
    Konto1.einzahlen(500)
    Konto1.auszahlen(200)
    Konto1.getKontoauszug()

    #User interface
    while(True):
        print("Welche option möchten sie ausführen? \n""Geld einzahlen (1) \n""Geld auszahlen (2) \n""Geld überweisen (3) \n""Kontoauszug ausgeben (4) \n""Kontostand abrufen (5) \n""Kontonummer ausgeben (6) \n""Abmelden (7)")
        antwortEingabe = int(input("Bitte wählen sie eine option aus: "))
        if antwortEingabe == 1:
            b = int(input("Bitte geben sie ihren gewünschten wert ein: "))
            x.einzahlen(b)
            antwort2 = input("Wollen sie noch eine weitere Aktion ausführen? (j/n): ")
        if antwortEingabe == 2:
            b = int(input("Bitte geben sie ihren gewünschten wert ein: "))
            x.auszahlen(b)
            antwort2 = input("Wollen sie noch eine weitere Aktion ausführen? (j/n): ")
            if antwort2 == "j":
                pass
            else:
                break
        if antwortEingabe == 3:
            b = input("Bitte geben sie das Konto des Empfängers an: ")
            x.überweisen(b)
            antwort2 = input("Wollen sie noch eine weitere Aktion ausführen? (j/n): ")
            if antwort2 == "j":
                pass
            else:
                break
        if antwortEingabe == 4:
            x.getKontoauszug()
            antwort2 = input("Wollen sie noch eine weitere Aktion ausführen? (j/n): ")
            if antwort2 == "j":
                pass
            else:
                break
        if antwortEingabe == 5:
            x.getKontostand()
            antwort2 = input("Wollen sie noch eine weitere Aktion ausführen? (j/n): ")
            if antwort2 == "j":
                pass
            else:
                break
        if antwortEingabe == 6:
            x.getKontonummer()
            antwort2 = input("Wollen sie noch eine weitere Aktion ausführen? (j/n): ")
            if antwort2 == "j":
                pass
            else:
                break
        if antwortEingabe == 7:
            break
    
 
else:
    print("Du Hurensohn!")
    
