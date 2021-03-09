#guess_the_game:
#This game picks a word from random list which is saved in String_List.txt file
#The user has to input one character at a time and complete the sequence. The maximum number of guesses is 10.

import random

def checkChar(newFlag, currentWord, inputChar):
'''
This function will check if the inserted character is present in the word or not
'''
  k=0
  while(k < len(currentWord)):
    if newFlag[k] == 'T':
      pass
    else:
      SearchFlag = 'F'
      if currentWord[k] != inputChar:
        newFlag[k] = 'F'
      else:
        newFlag[k] = 'T'
    k += 1
    
 
def displayWord(newFlag, currentWord):
'''
This function will display the word and the positions pending to be guessed will be displayed as '_'
'''
  m = 0
  
  while(m < len(currentWord)):
    if newFlag[m] == 'F':
      print("_ ", end="")
    else:
      print((currentWord[m] + " "), end="")
    m += 1
    
    
def getStringList():
'''
This function chooses a random word from the String_List.txt file in same Games folder
'''
  with open('String_List.txt', 'r') as open_file:
    stringList = (open_file.read()).split('\n')
  return stringList

if __name__ == '__main__':
  stringList = getStringList()
  
  maxguess = 10
  currentWord = random.choice(stringList)
  wordLength = len(currentWord)
  randomDigitLoc = random.randInt(0, wordLength-1)
  randomChar = currentWord[randomDigitLoc]
  newFlag = [None]*wordLength
  SearchFlag = 'T'
  
  #To fill in the start char as a hint
  checkChar(newFlag, currentWord, randomChar)
  print("***********WELCOME TO GUESS THE WORD GAME************")
  displayWord(newFlag, currentWord)
  selected = [None]
  selected.append(randomChar)
  i = 0
  
  while(i < maxguess):
    print("Attempts left : ", (maxguess - i))
    inputChar = (input("Enter the char : ")).upper()[0]
    if selected.count(inputChar) > 0:
      print("This letter is already guessed use some different letter")
    else:
      checkChar(newFlag, currentWord, inputChar)
      displayWord(newFlag, currentWord)
      selected.append(inputChar[0])
      if newFlag.count('T') == len(currentWord):
        print("You Won!!!")
        break
      i += 1
  else:
    print("You couldn't guess the word : ", currentWord)
