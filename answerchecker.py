def answerCheckerAdd():
  numOne = int(input("Enter first number you are going to add: "))
  numTwo = int(input("Enter second number you are going to add: "))
  print(numOne, "+", numTwo, "=")
  numThree = int(input("Enter your answer: "))
  if numThree == numOne + numTwo:
    print("Correct!")
    userChoice = input("Would you like to check another problem? \n1. Yes \n2. No \n")
    if userChoice == "1":
      from main import mainMenu
      mainMenu()
    elif userChoice == "2":
      pass
    else:
      print("Error")
      from main import mainMenu
      mainMenu()
  elif numThree != numOne + numTwo:
    print("Wrong, try again!")
    print(numOne, "+", numTwo, "=")
    numThree = int(input("Enter your answer: "))
    if numThree == numOne + numTwo:
      print("Correct!")
      userChoice = input("Would you like to check another problem? \n1. Yes \n2. No \n") 
      if userChoice == "1":
        
        from main import mainMenu
        mainMenu()
      elif userChoice == "2":
        pass
      else:
        print("Error")
        from main import mainMenu
        mainMenu()
    elif numThree != numOne + numTwo:
      print("Wrong")
      print(numOne, " + ", numTwo, " = ", (numOne + numTwo))
      userChoice = input("Would you like to check another problem? \n1. Yes \n2. No \n") 
      if userChoice == "1":
        from main import mainMenu
        mainMenu()
      elif userChoice == "2":
        pass
      else:
        print("Error")
        from main import mainMenu
        mainMenu()
    else:
      print("Error")
  else:
    print("Error")
  

def answerCheckerSub():
  numOne = int(input("Enter first number you are going to subtract: "))
  numTwo = int(input("Enter second number you are going to subtract: "))
  print(numOne, "-", numTwo, "=")
  numThree = int(input("Enter your answer: "))
  if numThree == numOne - numTwo:
    print("Correct!")
    userChoice = input("Would you like to check another problem? \n1. Yes \n2. No \n")
    if userChoice == "1":
        from main import mainMenu
        mainMenu()
    elif userChoice == "2":
      pass
    else:
      print("Error")
      from main import mainMenu
      mainMenu()
  elif numThree != numOne - numTwo:
    print("Wrong, try again!")
    print(numOne, "-", numTwo, "=")
    numThree = int(input("Enter your answer: "))
    if numThree == numOne - numTwo:
      print("Correct!")
      userChoice = input("Would you like to check another problem? \n1. Yes \n2. No \n") 
      if userChoice == "1":
        from main import mainMenu
        mainMenu()
      elif userChoice == "2":
        pass
      else:
        print("Error")
        from main import mainMenu
        mainMenu()
    elif numThree != numOne - numTwo:
      print("Wrong")
      print(numOne, " - ", numTwo, " = ", (numOne - numTwo))
      userChoice = input("Would you like to check another problem? \n1. Yes \n2. No \n") 
      if userChoice == "1":
        from main import mainMenu
        mainMenu()
      elif userChoice == "2":
        pass
      else:
        print("Error")
        from main import mainMenu
        mainMenu()
    else:
      print("Error")
  else:
    print("Error")
  


def answerCheckerMulti():
  numOne = int(input("Enter first number you are going to multiply: "))
  numTwo = int(input("Enter second number you are going to multiply: "))
  print(numOne, "*", numTwo, "=")
  numThree = int(input("Enter your answer: "))
  if numThree == numOne * numTwo:
    print("Correct!")
    userChoice = input("Would you like to check another problem? \n1. Yes \n2. No \n")
    if userChoice == "1":
        from main import mainMenu
        mainMenu()
    elif userChoice == "2":
      pass
    else:
      print("Error")
      from main import mainMenu
      mainMenu()
  elif numThree != numOne * numTwo:
    print("Wrong, try again!")
    print(numOne, "*", numTwo, "=")
    numThree = int(input("Enter your answer: "))
    if numThree == numOne * numTwo:
      print("Correct!")
      userChoice = input("Would you like to check another problem? \n1. Yes \n2. No \n") 
      if userChoice == "1":
        from main import mainMenu
        mainMenu()
      elif userChoice == "2":
        pass
      else:
        print("Error")
        from main import mainMenu
        mainMenu()
    elif numThree != numOne * numTwo:
      print("Wrong")
      print(numOne, " * ", numTwo, " = ", (numOne * numTwo))
      userChoice = input("Would you like to check another problem? \n1. Yes \n2. No \n") 
      if userChoice == "1":
        from main import mainMenu
        mainMenu()
      elif userChoice == "2":
        pass
      else:
        print("Error")
        from main import mainMenu
        mainMenu()
    else:
      print("Error")
  else:
    print("Error")
  


def answerCheckerDiv():
  numOne = int(input("Enter first number you are going to divide: "))
  numTwo = int(input("Enter second number you are going to divide: "))
  print(numOne, "/", numTwo, "=")
  numThree = int(input("Enter your answer: "))
  if numThree == numOne / numTwo:
    print("Correct!")
    userChoice = input("Would you like to check another problem? \n1. Yes \n2. No \n")
    if userChoice == "1":
        from main import mainMenu
        mainMenu()
    elif userChoice == "2":
      pass
    else:
      print("Error")
      from main import mainMenu
      mainMenu()
  elif numThree != numOne / numTwo:
    print("Wrong, try again!")
    print(numOne, "/", numTwo, "=")
    numThree = int(input("Enter your answer: "))
    if numThree == numOne / numTwo:
      print("Correct!")
      userChoice = input("Would you like to check another problem? \n1. Yes \n2. No \n") 
      if userChoice == "1":
        from main import mainMenu
        mainMenu()
      elif userChoice == "2":
        pass
      else:
        print("Error")
        from main import mainMenu
        mainMenu()
    elif numThree != numOne / numTwo:
      print("Wrong")
      print(numOne, " / ", numTwo, " = ", (numOne / numTwo))
      userChoice = input("Would you like to check another problem? \n1. Yes \n2. No \n") 
      if userChoice == "1":
        from main import mainMenu
        mainMenu()
      elif userChoice == "2":
        pass
      else:
        print("Error")
        from main import mainMenu
        mainMenu()
    else:
      print("Error")
  else:
    print("Error")
  
