#!/usr/bin/python
# -*- coding: latin-1 -*-

#Maria Israelsson kv11min 
#Erik Appelblad et08ead
#Hanna Hjärström kv11hhm
#Kurs: 5DA000; uppgift 1

from random import choice

#Först slumpas om ord eller pseudoord, sedan slumpas vilken av de 6 olika listorna som skall köras i de två olika kategorierna
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
    
        #Facit som kollar om nuvarande ordet är samma som det 2steg tidigare i listan om användaren trycker på knappen, svaret sparas till en lista
    def facit(self):
        if len(self.olista) > self.current:
            if self.olista[self.current-1] == self.olista[self.current-3]:
                self.correct = self.correct + 1
                self.correctLista.append(str(self.current))
            else:
                self.fel = self.fel + 1
                self.felLista.append(str(self.current))
    
#Gör så att current, som används som index, ökar med 1
    def nexta(self):
        self.current = self.current + 1

#Visar antalet rätt och fel
    def visaResultat(self):
        self.resultat = self.resultat + "Testet är klart.\nTack för din medverkan!"
        return self.resultat        
        
#Skickar nuvarande ordet från ordlistan till update, så länge det finns ord i listan. Annars returneras slut
    def getWord(self):
        if len(self.olista) > self.current:
            return self.olista[self.current].strip()
        else:
            return "SLUT"
        
#Sparar rätt och fel till csv-fil, samt vilken ordlista FP har fått se
    def spara(self):
        sparFil = open('data.csv', 'a')
        sparFil.write(str(self.correct)+";"+str(self.fel)+";"+self.filnamn+";"+str(self.correctLista)+";"+str(self.felLista))
        sparFil.write("\n")
        sparFil.close()
        
#Klassen för demonstrationsomgången
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
    
#Gör så att current, som används som index, ökar med 1
    def nexta(self):
        self.current = self.current + 1        
        
#Skickar nuvarande siffra från lista till demo. När listan är slut returneras slut
    def getNr(self):
        if len(self.nrlista) > self.current:
            return self.nrlista[self.current].strip()
        else:
            return "SLUT"