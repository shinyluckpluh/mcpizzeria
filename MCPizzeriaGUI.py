# Dit bestand zorgt voor de gebruikersinterface (GUI)van onze programma.
# Vul hier de naam van je programma in:
#
#
# Vul hier jullie namen in: komt later wel
#
#
#


### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import MCPizzeriaSQL


### ---------  Functie definities  -----------------
def zoekKlant():
 #haal de ingevoerde_klantnaam op uit het invoerveld
 # en gebruik dit om met SQL de klant in database te vinden
 gevonden_klanten = MCPizzeriaSQL.zoekKlantInTabel(ingevoerde_klantnaam.get())
 print(gevonden_klanten) # om te testen
 
 invoerveldKlantnaam.delete(0, END) #invoerveld voor naam leeg maken
 invoerveldKlantNr.delete(0, END) #invoerveld voor klantNr leeg maken
 for rij in gevonden_klanten: #voor elke rij dat de query oplevert
     #toon klantnummer, de eerste kolom uit het resultaat in de invoerveld
     invoerveldKlantNr.insert(END, rij[0])
     #toon klantAchternaam, de tweede kolom uit het resultaat in de invoerveld
     invoerveldKlantnaam.insert(END, rij[1]) 

def zoekPizza():
 #haal de ingevoerde_klantnaam op uit het invoerveld
 # en gebruik dit om met SQL de klant in database te vinden
 print(ingevoerde_pizzanaam.get())
 gevonden_pizzas = MCPizzeriaSQL.zoekPizzaInTabel(ingevoerde_pizzanaam.get())
 print(gevonden_pizzas) # om te testen
 
 invoerveldPizzanaam.delete(0, END) #invoerveld voor naam leeg maken
 listboxMenu.delete(1,END)

 for rij in gevonden_pizzas: #voor elke rij dat de query oplevert
     #toon klantAchternaam, de tweede kolom uit het resultaat in de invoerveld
     listboxMenu.insert(END, rij) 

def toonMenuInListbox():
 listboxMenu.delete(1, END) #maak de listbox leeg
 
 pizza_tabel = MCPizzeriaSQL.vraagOpGegevensPizzaTabel()
 for regel in pizza_tabel:
    listboxMenu.insert(END, regel) #voeg elke regel uit resultaat in listboxMenu

### functie voor het selecteren van een rij uit de listbox en deze in een andere veld te plaatsen
def haalGeselecteerdeRijOp(event):
 #bepaal op welke regel er geklikt is
 geselecteerdeRegelInLijst = listboxMenu.curselection()[0]
 #haal tekst uit die regel
 geselecteerdeTekst = listboxMenu.get(geselecteerdeRegelInLijst)
 #verwijder tekst uit veld waar je in wilt schrijven, voor het geval er al iets staat
 invoerveldGeselecteerdePizza.delete(0, END)
 #zet tekst in veld
 invoerveldGeselecteerdePizza.insert(0, geselecteerdeTekst) 

#voeg de bestelling van klant met gekozen pizza en aantal toe
#in de winkelwagentabel
#en toon de bestelling in de listbox op het scherm
def voegToeAanWinkelWagen():
 klantNr = invoerveldKlantNr.get()
 gerechtID = geselecteerdePizza.get()
 aantal = aantalGeslecteerdePizza.get()
 MCPizzeriaSQL.voegToeAanWinkelWagen(klantNr, gerechtID, aantal)
 winkelwagen_tabel = MCPizzeriaSQL.vraagOpGegevensWinkelWagenTabel()
 listboxWinkelwagen.delete(0, END) #listbox eerst even leeg maken
 for regel in winkelwagen_tabel:
     listboxWinkelwagen.insert(END, regel)


### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Pizzeria")



knopSluit = Button(venster, text="sluiten", width=12, command=venster.destroy)
knopSluit.grid(row=20, column=3)

labelIntro = Label(venster, text="Welkom!")
labelIntro.grid(row=0, column=0, sticky="W")

labelKlantnaam = Label(venster, text= "Klantnaam:")
labelKlantnaam.grid(row = 1, column = 0)

ingevoerde_klantnaam = StringVar()
invoerveldKlantnaam = Entry(venster, textvariable=ingevoerde_klantnaam)
invoerveldKlantnaam.grid(row=1, column=1, sticky="W")

invoerveldKlantNr = Entry(venster)
invoerveldKlantNr.grid(row=2, column=1, sticky="W")

knopZoekOpKlantnaam = Button(venster, text = "Zoek Klant", width = 12, command= zoekKlant)
knopZoekOpKlantnaam.grid(row=1, column=3)

labelPizzanaam = Label(venster, text= "Pizzanaam:")
labelPizzanaam.grid(row= 3, column= 0)

ingevoerde_pizzanaam = StringVar()
invoerveldPizzanaam = Entry(venster, textvariable=ingevoerde_pizzanaam) #pas aan
invoerveldPizzanaam.grid(row= 3, column= 1, sticky='W')

knopZoekOpPizzanaam = Button(venster, text = "Zoek Pizza", width = 12, command = zoekPizza )
knopZoekOpPizzanaam.grid(row= 4, column=  3)

labelMogenlijkheden = Label(venster, text= "Mogenlijkheden:")
labelMogenlijkheden.grid(row= 5, column= 0)

listboxMenu = Listbox(venster, height = 6, width = 50)
listboxMenu.grid(row= 5, column= 1, rowspan = 6, columnspan = 2, sticky='W' )
listboxMenu.insert(0, "ID Gerecht Prijs")
listboxMenu.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)

scrollbarlistboxMenu = Scrollbar(venster)
scrollbarlistboxMenu.grid(row=5, column=2, rowspan=6, sticky="E")
listboxMenu.config(yscrollcommand=scrollbarlistboxMenu.set)
scrollbarlistboxMenu.config(command=listboxMenu.yview)

KnopToonPizzas = Button(venster, text = "Toon alle pizza's", width = 12, command= toonMenuInListbox)
KnopToonPizzas.grid(row = 5, column = 3)

labelGekozenPizza = Label(venster, text= "Gekozen pizza:")
labelGekozenPizza.grid(row = 12, column = 0)

geselecteerdePizza = StringVar()
invoerveldGeselecteerdePizza = Entry(venster, textvariable= geselecteerdePizza)
invoerveldGeselecteerdePizza.grid(row = 12, column = 1, sticky= "W")

labelAantal = Label(venster, text = "Aantal:")
labelAantal.grid(row = 13, column = 0)

aantalGeslecteerdePizza= IntVar()
aantalGeslecteerdePizza.set(1)
KeuzeMenuAantal = OptionMenu(venster, aantalGeslecteerdePizza, 1,2,3)
KeuzeMenuAantal.grid(row=13, column =1)

knopVoegToeAanWinkelWagen = Button(venster, text = "Voeg toe", width = 12, command = voegToeAanWinkelWagen)
knopVoegToeAanWinkelWagen.grid(row = 13, column = 3)

labelBestelling = Label(venster, text = "Bestelling:")
labelBestelling.grid(row = 14, column = 0)

listboxWinkelwagen = Listbox(venster, height = 5, width = 50)
listboxWinkelwagen.grid(row= 14, column= 1, rowspan = 6, columnspan = 2, sticky='W' )

scrollbarlistboxWinkelwagen = Scrollbar(venster)
scrollbarlistboxWinkelwagen.grid(row=14, column=2, rowspan=6, sticky="E")
listboxWinkelwagen.config(yscrollcommand=scrollbarlistboxWinkelwagen.set)
scrollbarlistboxWinkelwagen.config(command=listboxWinkelwagen.yview)





#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
