#!/usr/bin/python
# -*- coding: latin-1 -*-

#Maria Israelsson kv11min 
#Erik Appelblad et08ead
#Hanna Hjärström kv11hhm
#Kurs: 5DA000; uppgift 1

#Informationstext som visas före demonstrationsomgången
try:
    fil = open("info.txt", "r")
    itextdemo = fil.read()
    fil.close()
except IOError:
    print "Infotextfil saknas"
    itextdemo = "Informationstexten kunde inte visas."
    
#Informationstext som visas före testet börjar
try:
    fil2 = open("info_test.txt","r")
    itexttest = fil2.read()
    fil2.close()
except IOError:
    print "Infotextfil2 saknas"
    itexttest = "Informationstexten kunde inte visas."