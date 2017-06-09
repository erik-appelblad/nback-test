#!/usr/bin/python
# -*- coding: latin-1 -*-

#Maria Israelsson kv11min 
#Erik Appelblad et08ead
#Hanna Hj�rstr�m kv11hhm
#Kurs: 5DA000; uppgift 1

from random import choice

#F�rst slumpas om ord eller pseudoord, sedan slumpas vilken av de 6 olika listorna som skall k�ras i de tv� olika kategorierna
class Ordlista:
    def __init__(self):
        self.ordlistor = [["ord123.txt","ord231.txt","ord312.txt","ord213.txt","ord321.txt","ord132.txt"],["pseudo123.txt","pseudo231.txt","pseudo312.txt","pseudo213.txt","pseudo321.txt","pseudo132.txt"]]
        self.filnamn = choice(choice(self.ordlistor))
        try:
            fil = open(self.filnamn, "r")
            self.olista = fil.readlines()
            fil.close()
        except IOError:
            self.olista = ["SLUT"]
            print "Ordlistor saknas"
        
        self.current = 0
        self.correct = 0
        self.fel = 0
        self.resultat = ""
        self.correctLista = []
        self.felLista = []
    
        #Facit som kollar om nuvarande ordet �r samma som det 2steg tidigare i listan om anv�ndaren trycker p� knappen, svaret sparas till en lista
    def facit(self):
        if len(self.olista) > self.current:
            if self.olista[self.current-1] == self.olista[self.current-3]:
                self.correct = self.correct + 1
                self.correctLista.append(str(self.current))
            else:
                self.fel = self.fel + 1
                self.felLista.append(str(self.current))
    
#G�r s� att current, som anv�nds som index, �kar med 1
    def nexta(self):
        self.current = self.current + 1

#Visar antalet r�tt och fel
    def visaResultat(self):
        self.resultat = self.resultat + "Testet �r klart.\nTack f�r din medverkan!"
        return self.resultat        
        
#Skickar nuvarande ordet fr�n ordlistan till update, s� l�nge det finns ord i listan. Annars returneras slut
    def getWord(self):
        if len(self.olista) > self.current:
            return self.olista[self.current].strip()
        else:
            return "SLUT"
        
#Sparar r�tt och fel till csv-fil, samt vilken ordlista FP har f�tt se
    def spara(self):
        sparFil = open('data.csv', 'a')
        sparFil.write(str(self.correct)+";"+str(self.fel)+";"+self.filnamn+";"+str(self.correctLista)+";"+str(self.felLista))
        sparFil.write("\n")
        sparFil.close()
        
#Klassen f�r demonstrationsomg�ngen
class DemoLista:
    def __init__(self):
        try:
            fil = open("demosiffror.txt", "r")
            self.nrlista = fil.readlines()
            fil.close()        
        except IOError:
            self.nrlista = ["SLUT"]
            print "Demosiffror saknas"   
            
        self.current = 0
    
#G�r s� att current, som anv�nds som index, �kar med 1
    def nexta(self):
        self.current = self.current + 1        
        
#Skickar nuvarande siffra fr�n lista till demo. N�r listan �r slut returneras slut
    def getNr(self):
        if len(self.nrlista) > self.current:
            return self.nrlista[self.current].strip()
        else:
            return "SLUT"