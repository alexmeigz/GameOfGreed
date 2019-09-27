import random

overallscore = 0
currentscore = 0
isgameover = False
tokens = 3

def newGame():
   '''initializes new game'''
   global overallscore
   global isgameover
   global tokens

   overallscore = 0
   isgameover = False
   tokens = 3
   print("New Game Started!")

   newRound()

def rollDie():
   '''rolls a fair, six-sided die'''
   return random.randrange(1, 7)

def newRound():
   '''starts a new round upon inserting token'''
   global currentscore
   global tokens

   tokens -= 1
   print("Token inserted!")
   currentscore = rollDie()
   currentscore += rollDie()

   print("New Round! Starting Current Score:", currentscore)

def rollAgain():
   '''User chooses to be greedy'''
   global overallscore
   global currentscore
   global isgameover
   
   x = rollDie()
   print("You rolled a...", x)
   if x == 2:
     print("Oh no! Your round's score becomes a 0 and your round ends! \n")
     print("Your current overall score:", overallscore)
     if tokens == 0:
       gameOver()
     else:
       newRound()
   else:
     currentscore += x
     print("New Current Score:", currentscore)


def gameOver():
   '''Ending game state'''
   global isgameover
   isgameover = True
   print("Game Over! Your final score is...", overallscore, "!")

'''initializes new game'''
newGame()

#loop to allow continuous user input
while True:
   x = input("\n  Action? ")
   
   if x in "nN":
       if not isgameover:
           print("You already have an active game!")
       else:
           newGame()
   elif isgameover:
      print("You already lost!")
   elif x in "rR":
       rollAgain()
   elif x in "sS":
      print("Your current score of", currentscore, "has been added to your overall score!")
      overallscore += currentscore
      print("Your new overall score:", overallscore, "\n")
      if tokens == 0:
         isgameover = True
         gameOver()
      else: 
         newRound()
   elif x.upper() == "STOP":
      print("Game of Greed has stopped running!")
      break
   else:
       print('''You may only input R, S, or N; Type R to roll again, S to stop rolling, and N to start a new game''')



