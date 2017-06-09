#!/usr/bin/python
# -*- coding: latin-1 -*-

#Maria Israelsson kv11min 
#Erik Appelblad et08ead
#Hanna Hj�rstr�m kv11hhm
#Kurs: 5DA000; uppgift 1

from Tkinter import*
import time
from ordlista import *
from infotext import *

#Vid demonstrationsomg�ngen avaktiveras knappen
#Efter 3000ms anropas Demofunktionen
def startDemo():
    knapp.configure(state=DISABLED,text='2-back')
    label.configure(text='+',font=("Arial",30,"bold"),fg="white", bg='black')
    label.after(3000,Demo)

#infotexten f�rsvinner, knappen byter namn och metod sedan aktiveras updatefunktionen
def startTest():
    knapp.configure(state=DISABLED,command=knapptryckblock)
    label.configure(text='+',font=("Arial",30,"bold"),fg="white", bg='black')
    label.after(3000,update)
    
#Nedr�kning inf�r nya sekvenser med ordlistor    
def counter3():
    knapp.configure(state=DISABLED,text='2-back')
    label.configure(text='3',font=("Arial",30, "bold"),fg="white", bg='black')
    label.after(1000,counter2)
def counter2():
    label.configure(text='2')
    label.after(1000,counter1)
def counter1():
    label.configure(text='1')
    label.after(1000,startTest)

#Efter en knapptryckning avaktiveras knappen tills n�sta ord visas
def knapptryckblock():
    ordObj.facit()
    knapp.configure(state=DISABLED, relief=SUNKEN)    

def avsluta():
    window.destroy()

#Uppdateringsfunktion som h�mtar ord i listan
#Skriver ut infotext efter varje omg�ng i testet
#Aktiveras metoden spara och sparar resultatet fr�n testet
def update():
    knapp.configure(state=NORMAL, relief=RAISED)
    label.configure(text=ordObj.getWord())
    if ordObj.getWord() != "SLUT":
        ordObj.nexta()
        if ordObj.current in [24,48]:
            knapp.configure(state=DISABLED)
            label.configure(text='10 sekunder till n�sta omg�ng')
            label.after(10000,counter3)
        else:
            label.after(1500, update)
    else:
        label.configure(text=ordObj.visaResultat())
        label.after_idle(ordObj.spara)
        knapp.configure(text="Avsluta", state=NORMAL, relief=RAISED, command = avsluta)
        
#Funktion f�r demonstrationsomg�ngen
#De r�tta svaren visas med gr�n text
#N�r omg�ngen �r slut byter knappen namn till 'Starta test'
def Demo():
    if nrObj.getNr() != "SLUT":
        if nrObj.current in [2,6,7,10,11]:
            label.configure(text=nrObj.getNr(),fg='green')
        else:
            label.configure(text=nrObj.getNr(),fg='white')        
        nrObj.nexta()
        label.after(1500, Demo)
    else:
        label.configure(text=itexttest,font=('Arial', 15))
        knapp.configure(state=NORMAL,text='Starta test',command=counter3)
        
#Skapar objekt av klasserna    
ordObj = Ordlista()
nrObj = DemoLista()
window = Tk()

#Programmet visas i helsk�rm
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.overrideredirect(1)
window.geometry("%dx%d+0+0" % (w, h))

#Skapar en svart Canvas
canvas = Canvas (window, width=1000, height=500, bg='black')
canvas.pack(expand=YES, fill=BOTH)

#Visar informationstext
label = Label(canvas, text=itextdemo, wraplength=670, justify = LEFT, font=("Arial",15),fg="white", bg='black')
label.pack(anchor=CENTER)
canvas.create_window(675,400,window=label)

#Knapp f�r att starta demonstrationsomg�ngen
knapp = Button(window, text='Starta demo',relief=RAISED, command=startDemo)
knapp.pack(fill=X)

mainloop()