#CTS 285
#M2HW1 - ANSWER CHECKER FIRST SPRINT
#CARLOS CASTILLA VIRELLES
#10.3.2022
def answerCheckerAdd():
  numOne = int(input("Enter first number you are going to add: "))
  numTwo = int(input("Enter second number you are going to add: "))
  print(numOne, "+", numTwo, "=")
  numThree = int(input("Enter your answer: "))
  if numThree == numOne + numTwo:
    print("Correct!")
    userChoice = input("Would you like to check another problem? \n1. Yes \n2. No \n")
    if userChoice == "1":
      answerCheckerAdd()
    elif userChoice == "2":
      pass
    else:
      print("Error")
      answerCheckerAdd()
  elif numThree != numOne + numTwo:
    print("Wrong, try again!")
    print(numOne, "+", numTwo, "=")
    numThree = int(input("Enter your answer: "))
    if numThree == numOne + numTwo:
      print("Correct!")
      userChoice = input("Would you like to check another problem? \n1. Yes \n2. No \n") 
      if userChoice == "1":
        answerCheckerAdd()
      elif userChoice == "2":
        pass
      else:
        print("Error")
        answerCheckerAdd()
    elif numThree != numOne + numTwo:
      print("Wrong")
      print(numOne, " + ", numTwo, " = ", (numOne + numTwo))
      userChoice = input("Would you like to check another problem? \n1. Yes \n2. No \n") 
      if userChoice == "1":
        answerCheckerAdd()
      elif userChoice == "2":
        pass
      else:
        print("Error")
        answerCheckerAdd()
    else:
      print("Error")
  else:
    print("Error")
  
answerCheckerAdd()

##TODO:
##ADD FUNCTIONS FOR SUBTRACTION, DIVISION, MULT, AND DATABANK