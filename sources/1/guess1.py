#/usr/bin/env python
#coding=utf-8
import random
thenumber=random.randint(1,50)
name=raw_input("Δώσε το όνομα σου:")
print "Έχω σκεφτεί ένα αριθμό από 1 ως το 50"
print "Μπορείς να τον βρεις;"
guess=0
tries=0
while guess!=thenumber:
  tries=tries+1
  guess=input("Δώσε τον αριθμό:")
  if guess>thenumber:
    print"Εδωσες μεγαλύτερο αριθμό!"
  if guess<thenumber:
    print"Έδωσες μικρότερο αριθμό!"
    
print "Συγχαρητηρία ",name," τον βρήκες σε",tries,"προσπάθειες"
if tries==1:
  print "Beginner's luck!"
elif tries<=5:
  print "Είσαι γρήγορος"
elif tries<=10:
  print "Eίσαι ένας βλάκας και μισός"
else: 
  print "My grandmother is faster (and she is dead)"
