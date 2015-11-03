#
# Βρες τον αριθμό. Απόπειρα 1
#
import random
thenumber = random.randint(1,50)
print "Έχω σκεφτεί ένα αριθμό από το 1 ως το 50."
print "Μπορείς να τον βρεις;"
guess = 0
while guess != thenumber:
  guess=input("Δώσε τον αριθμό: ")
  if guess > thenumber:
    print "Έδωσες μεγαλύτερο αριθμό!"
  if guess < thenumber:
    print "Έδωσες μικρότερο αριθμό!"
  if guess == thenumber:
    print "Τον βρήκες!!!"

#
# Βρες τον αριθμό. Απόπειρα 2
#
import random
thenumber = random.randint(1,50)
print "Έχω σκεφτεί ένα αριθμό από το 1 ως το 50."
print "Μπορείς να τον βρεις;"
guess = 0
while guess != thenumber:
  guess=input("Δώσε τον αριθμό: ")
  if guess > thenumber:
    print "Έδωσες μεγαλύτερο αριθμό!"
  if guess < thenumber:
    print "Έδωσες μικρότερο αριθμό!"
print "Τον βρήκες!!!"

name = input("Δώσε το όνομα σου: ")

print "Συγχαρητήρια", name, "τον βρήκες!"

name = raw_input("Δώσε το όνομα σου: ")

#
# Βρες τον αριθμό. Απόπειρα 3
#
import random
thenumber = random.randint(1,50)
name = raw_input("Δώσε το όνομα σου: ")
print "Έχω σκεφτεί ένα αριθμό από το 1 ως το 50."
print "Μπορείς να τον βρεις;"
guess = 0
tries = 0
while guess != thenumber:
  tries = tries + 1
  guess=input("Δώσε τον αριθμό: ")
  if guess > thenumber:
    print "Έδωσες μεγαλύτερο αριθμό!"
  if guess < thenumber:
    print "Έδωσες μικρότερο αριθμό!"
print "Συγχαρητήρια", name, "τον βρήκες σε", tries, "προσπάθειες!"



tries += 1

if tries == 1:
  print "Beginner's luck!"
if tries <= 5:
  print "Είσαι γρήγορος!"
if tries > 5:
  print "Η γιαγιά μου παίζει πιο καλά!"


if tries == 1:
  print "Beginners luck!"
if (tries >= 5 and tries !=1):
  print "Είσαι γρήγορος!"
if tries > 5:
  print "Η γιαγιά μου παίζει πιο καλά!"


if tries == 1:
  print "Beginners luck!"
elif tries <= 5:
  print "Είσαι γρήγορος!"
else:
  print "Η γιαγιά μου παίζει πιο καλά!"


shoppinglist = [ "Cheese" , "Rice", "Coffee", "Milk", "Camba" ]


for element in shoppinglist:
  print element


shoppinglist = [ "Cheese", "Rice", "Coffee", "Milk", "Camba" ]
element = raw_input("What are you buying today? ")
if element in shoppinglist:
  print "Yes, this is on the list"
else:
  print "Not on the list, you don't need it"

for i in [1,2,3,4,5,6,7,8,9,10]:
  print i

for i in range(1,1001):
  print i
