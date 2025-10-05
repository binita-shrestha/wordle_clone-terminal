import random
import sys
import time
from colorama import Fore, Style,  init
import nltk
nltk.download('words')
from nltk.corpus import words
#using built-in english-words package to import actual words
#storing the words with five letters 
word_list = [w.lower() for w in words.words() if len(w) == 5 and w.isalpha()] 
#randomly picking a word form the above list
picked_word = random.choice(word_list)
#print(picked_word) to check the game is runnign smoothly
init(autoreset=True) #to change to color of text back to default

#print(Fore.BLUE + "B") testing if the color function works
#game starts
print(Fore.CYAN + "WELCOME TO WORDLE! \n")
print(Fore.CYAN + "Are you ready to guess today's word? \n")
print(Fore.CYAN +"You have 6 attempts. GOOD LUCK! \n")
time.sleep(1) #1 second pause before the player is allowed to enter guesses
count = 0 #initializing count
while count < 6: #maximum of 6 guesses provided
    #getting the guess from the user
    guess = input("Enter your 5-letter word: ").lower()
    #validation check if word is 5-lettered and it is a valid english word
    if len(guess) != 5:
        print(Fore.RED + "Please enter a 5-letter word")
        continue #does not increase the count
    if guess not in word_list:
        print(Fore.RED + "Not in the word list!")
        continue #does not increase the count
    #checking for winning condition
    if guess == picked_word:
        print (f"YOU PICKED THE RIGHT WORD, YOU WIN! The word is {picked_word}")
        break #while loop ends 
    #feedback logic if guessed word does not exactly match the picked word
    feedback = [""]*5 #empty string that will hold our colored letters for each position
    temp_word = list(picked_word) #copy of picked word where we will cross out letters as we match them so duplicates do not confuse users

    for i in range(5): #since it is a 5-lettered word
        
        if guess[i] == picked_word[i]: #identifying green matches
            feedback[i] = Fore.GREEN + guess[i].upper() #stores the exactly matching letter at correct location
            temp_word[i] = None #same letter in the copy of picked word will not be removed to avoid confusion with same occurance of any letters
    for i in range(5):
        if feedback[i] == "": #only cheking in remaining location after identifying green
            if guess[i] in temp_word:
                feedback[i] = Fore.YELLOW + guess[i].upper()
                temp_word[temp_word.index(guess[i])] = None
            else:
                feedback[i] =  Fore.LIGHTBLACK_EX + guess[i].upper()
            
    print("".join(feedback))
    count += 1

else:
    print(f"GAME OVER! THE WORD WAS {picked_word}")

