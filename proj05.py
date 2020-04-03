# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 02:11:38 2019

@author: kazid
"""
#Define character variable
def contains_invalid_characters(word):
    contains_in_valid=False
    #using for loop
    for c in word:
        #coditional statement that return true
        if c in "~`!@#$%^&()-_=+\|]}[{;:'\",</?ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890":
            contains_in_valid= True
            #if the result comes true, then return function
    return contains_in_valid
#while True the statement, Enter your fisrt Gibberish sylabble
while True:
        first_gibb = input("Enter your first Gibberish syllable (Add * for the vowel substitute): ")
        if contains_invalid_characters(first_gibb):
            #enter only letter or wildcard
            while True:
                first_gibb=""
                first_gibb=input("Syllable must only contain letters or wilcard ('*'): ")
                #if enter proper input, user continue the program
                if contains_invalid_characters(first_gibb):
                    continue
                else:
                    break
                #enter the second Gibberish syllable

        second_gibb=input("Enter the second Gibberish syllable (* for vowel substitute): ")
        if contains_invalid_characters(second_gibb):
            while True:
                #should only enter the valid input 
                second_gibb=input("Syllable must only contain letters or wilcard ('*'): ")
                if contains_invalid_characters(second_gibb):
                    continue
                else:
                    break
#after enter two syllables, user propt to enter a word to translatet into Gibberish
        word = input("Please enter a word you want to translate")
        first_segment=""
        second_segment=""
        current_index=-1
        #conditional statement to make the syllable into Gibberish word
        for c in word:
            current_index+=1
            if c in 'aeiou' and '*' in first_gibb:
                first_segment+=c+first_gibb.strip('*')+c
                second_segment=word[current_index+1:]
                break
            elif c in 'aeiou' and '*' not in first_gibb:
                first_segment += first_gibb
                second_segment = word[current_index+1:]
                break
            else:
                first_segment+=c

        if '*' in second_gibb:
            second_segment = second_segment.replace('a','a'+second_gibb.strip('*')+'a')
            second_segment = second_segment.replace('e', 'e'+second_gibb.strip('*')+'e')
            second_segment = second_segment.replace('i', 'i'+second_gibb.strip('*')+'i')
            second_segment = second_segment.replace('o', 'o'+second_gibb.strip('*')+'o')
            second_segment = second_segment.replace('u', 'u'+second_gibb.strip('*')+'u')
        else:
            second_segment = second_segment.replace('a', second_gibb.strip('*'))
            second_segment = second_segment.replace('e', second_gibb.strip('*'))
            second_segment = second_segment.replace('i', second_gibb.strip('*'))
            second_segment = second_segment.replace('o', second_gibb.strip('*'))
            second_segment = second_segment.replace('u', second_gibb.strip('*'))
            
        #Priting the Gibberish word from the user's input
        print("Your final word:\n",first_segment+second_segment)

        #Ask user if they want to play again or not
        playAgain=input("Play again?(y/n): ")
        if playAgain=='y' or playAgain=='yes':
            #Gibberish will continue for user
            continue
        #Gibberish will prompt a thank you message for playing
        elif playAgain=='n' or playAgain=='no':
            print("Thanks for playing.")
            break
        else:
            while True:
                ##Ask user if they want to play again or not
                playAgain = input("Please enter y to continue or n to quit: ")
                if playAgain == 'y' or playAgain == 'yes':
                    continue
                elif playAgain == 'n' or playAgain == 'no':
                    #Gibberish will prompt a thank you message for playing
                    print("Thanks for playing.")
                    break
            break