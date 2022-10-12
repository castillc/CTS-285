import answerchecker as ac
def mainMenu():
  print("Menu:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")
  userInput = input()
  if userInput == ("1"):
    ac.answerCheckerAdd()
  elif userInput == ("2"):
    ac.answerCheckerSub()
  elif userInput == ("3"):
    ac.answerCheckerMulti()
  elif userInput == ("4"):
    ac.answerCheckerDiv()
  elif userInput == ("5"):
    print("Exiting")
  else:
    print("Error,  value must be 1-5")
    

mainMenu()