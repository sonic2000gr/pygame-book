#
# The Python Adventure
# Based on an idea published in Pixel Magazine
# issue 18, January 1986
#
# Download this source file from http://pygamegr.wordpress.com
#

def getInput(moves,room):
  directions = ["Βόρεια","Νότια","Ανατολικά","Δυτικά"]
  destinations = moves[room]
  possiblemoves = []
  index = 0
  print "Έξοδοι:",
  for i in destinations:
    if i!=-1:
      print directions[index],
      possiblemoves.append(directions[index])
    index +=1
  print "\n"
  userinput=""
  while userinput not in possiblemoves:
    userinput=raw_input("Που θες να πας; ")
  return directions.index(userinput)

def main():
  # Room descriptions

  rooms = [ "Βρισκεσαι στον κήπο. Παντού σκοτάδι.",
            "Βρίσκεσαι στο μπάνιο. Ακούς θόρυβο.",
            "Βρίσκεσαι στο χωλ. Παραλίγο να σκοντάψεις. Σκάλα ανατολικά",
            "Βρισκεσαι στην αποθήκη. Η ατμόσφαιρα είναι αποπνικτική. Σκάλα Δυτικά, Μονοπάτι Νότια.",
            "Έφτασες στο καθιστικό. Βρήκες τον πατέρα σου.",
            "Βρίσκεσαι στο σαλόνι. Ακούγεται μουσική.",
            "Βρίσκεσαι στην τραπεζαρία. Τα πάντα είναι ανάστατα.",
            "Βρίσκεσαι στο διάδρομο. Είναι σκοτεινά. Σκάλα Νότια",
            "Είσαι στη κουζίνα. Ακούς φωνές.",
            "Είσαι στον πάνω διάδρομο. Παντού ησυχία. Σκάλα Βόρεια.",
            "Είσαι στο δωμάτιο του αδερφού σου. Ο αδερφός σου σε μαρτυρά!",
            "Είσαι στο δωμάτιο των γονέων σου. Η μητέρα σου σε έπιασε.",
            "Είσαι στο δωμάτιο σου. Είσαι ασφαλής." ]

  #
  # The following list contains lists :)
  # The list's index denotes the current room.
  # Each single list contains four numbers:
  # First number -> Destination room if North (0)
  # Second number -> Destination room if South(1)
  # Third number -> Destination room if East (2)
  # Fourth number -> Destination room if West (3)
  #
  # Destination is set to -1 if it does not exist
  #

  moves = [   [-1,2,-1,-1],
              [-1,-1,2,-1],
              [0,5,3,1],
              [-1,8,-1,2],
              [-1,6,5,-1],
              [2,8,-1,4],
              [4,7,-1,-1],
              [6,9,8,-1],
              [5,-1,-1,7],
              [7,11,12,10],
              [-1,-1,9,-1],
              [9,-1,-1,-1],
              [-1,-1,-1,9] ]

  # When player reaches any of the following room(s),
  # he wins the game

  winrooms = [ 12 ]

  # When player reaches any of the following rooms,
  # he loses

  lossrooms = [ 4, 10, 11 ]

  # Startup room
  # Doesn't have to be 0, but must not be a winning or losing room

  room = 0

  print "The Adventure!"
  print "=============="

  endgame = False
  while not endgame:
    print rooms[room]
    if room in winrooms:
      print "Κέρδισες! Η περιπέτεια τελείωσε."
      endgame = True
    elif room in lossrooms:
      print "Έχασες! Η περιπέτεια τελείωσε."
      endgame = True
    else:
      direction = getInput(moves, room)
      destinations = moves[room]
      room = destinations[direction]

# Start program
if __name__ == "__main__":
    main()
