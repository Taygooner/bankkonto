Python Bankkonto
Dieses Python-Programm ermöglicht es, Bankkonten zu erstellen, Einzahlungen und Auszahlungen durchzuführen, Überweisungen zwischen Konten zu tätigen, den Kontostand abzufragen und den Kontoauszug anzuzeigen. Das Programm verwendet die Klasse "Konto" und enthält Funktionen wie "einzahlen", "auszahlen", "überweisen", "getKontoauszug" und mehr.

Klassen
Konto
Die Konto-Klasse ist die Hauptklasse, die alle Eigenschaften eines Bankkontos definiert. Die folgenden Attribute werden definiert:

kontostand: Kontostand des Kontos
kontoAuszug: Text, der den Kontoauszug des Kontos darstellt
pin: PIN des Kontos
kontonummer: Kontonummer des Kontos
kontoart: Art des Kontos (z.B. "Giro")
inhaber: Name des Kontoinhabers
dispo: Dispositionskredit des Kontos
limit: Grenzwert für Auszahlungen
dispolimit: Dispositionskredit-Limit des Kontos
auszug: Liste aller Kontoauszüge
transaktionen: Liste aller Transaktionen
Dispo
Die Dispo-Klasse erweitert die Konto-Klasse und definiert zusätzliche Eigenschaften für Konten mit einem Dispositionskredit.

Funktionen
einzahlen(self, betrag)
Diese Funktion ermöglicht es dem Benutzer, Geld auf das Konto einzuzahlen. Der betrag Parameter muss größer als 0 sein.

auszahlen(self, betrag)
Diese Funktion ermöglicht es dem Benutzer, Geld von seinem Konto abzuheben. Der betrag Parameter muss größer als 0 sein. Wenn der Kontostand und das Limit des Kontos ausreichen, wird das Geld abgehoben und eine Transaktion wird zur transaktionen Liste hinzugefügt.

überweisen(Konto, betrag, Konto2)
Diese Funktion ermöglicht es dem Benutzer, Geld zwischen zwei Konten zu überweisen.

getKontoauszug(self)
Diese Funktion gibt den Kontoauszug des Kontos aus, einschließlich aller Transaktionen.

setPin(self, neuerpin)
Diese Funktion ändert die PIN des Kontos auf neuerpin.

getPin(self)
Diese Funktion gibt die PIN des Kontos zurück.

setKontostand(self, neuer_Kontostand)
Diese Funktion ändert den Kontostand des Kontos auf neuer_Kontostand.

getKontostand(self)
Diese Funktion gibt den Kontostand des Kontos zurück.

setKontonummer(self, Kontonummer)
Diese Funktion ändert die Kontonummer des Kontos auf Kontonummer.

getKontonummer(self)
Diese Funktion gibt die Kontonummer des Kontos zurück.

Verwendung
Das Programm enthält einige Beispielkonten in der kontoliste, die für Tests verwendet werden können. Der Benutzer kann neue Konten erstellen und diese anschließend verwenden. Das Programm fordert den Benutzer auf, alle notwendigen Informationen für das neue Konto einzugeben, einschließlich Kontostand, PIN, Kontonummer, Kontotyp und Kontoinhabername.