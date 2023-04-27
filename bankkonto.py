import random
import datetime

# Klassen
class Konto():
    def __init__(self, kontostand, pin, kontonummer, kontoart, inhaber):
        self.__kontostand = kontostand
        self.kontoAuszug = "hallo, ich bin dein Kontoauszug"
        self.__pin = pin
        self.__kontonummer = kontonummer
        self.__kontoart = kontoart
        self.__inhaber = inhaber
        self.__dispo = 500
        self.__limit = 0
        self.__dispolimit = 0
        self.__auszug = []
        self.__transaktionen = []

    class Dispo():
        def __init__(self, kontostand, pin, kontonummer, kontoart, inhaber):
            self.__kontostand = kontostand
            self.kontoAuszug = "hallo, ich bin dein Kontoauszug"
            self.__pin = pin
            self.__kontonummer = kontonummer
            self.__kontoart = kontoart
            self.__inhaber = inhaber
            self.__dispo = 500
            self.__limit = 0
            self.__dispolimit = 0
            self.__auszug = []
            self.__transaktionen = []


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
Konto1 = Konto(1000,1234,1234567, "Giro", "ich")
Konto2 = Konto(12,1001,737828, "Giro", "TaNiHA")
Konto3 = Konto(12000,1003,137828, "Giro", "Tay")
kontoliste = [Konto1,Konto2]
zaehler = 0
zaehlerKonto = 3


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
    Konto = "Konto" + str((random.randint(1,1000)))
    Kontostand = 0
    Pin = int(input("geben sie einen pin mit 4 Zahlen ein, wir empfehlen keine *code muster* zu verwenden"))
    Kontonummer = (random.randint(1000,9999))
    KontoB = int(input("Bite wählen sie zwischen(1) GiroKonto(2) DispoKonto"))
    if KontoB == 1:
        KontoArt = GiroKonto
    if KontoB ==2:
        KontoArt = Dispo


    Inhaber = input("Bitte geben sie ihren Vornamen ein")

    Konto = KontoArt(Kontostand,Pin,Kontonummer,KontoArt,Inhaber)

    kontoliste = [Konto1,Konto2,Konto3,]
    
    #Eingabe der Kontonummer
    
    Kontonummer = input("Bitte geben Sie ihre kontonummer ein: ")
    #prüfe, ob das KOnto existiert
    zaehler = 0
    
    while zaehler < len(kontoliste):
        if int(Kontonummer) == int(kontoliste[zaehler].gibKontonummer()):
            print("Das Konto existiert:")
        zaehler = zaehler + 1 
 #User interface
 #Eingabe pin
pin = input("Bitte geben Sie Ihren Pin ein: ")

if int(pin) == int(kontoliste[zaehler +1].getPin()):
    
    print("Die Anmeldung war erfolgreich")

else:
    print("Du Hurensohn!")

#Test Befehle
Konto1.einzahlen(500)
Konto1.auszahlen(200)
Konto1.getKontoauszug()
