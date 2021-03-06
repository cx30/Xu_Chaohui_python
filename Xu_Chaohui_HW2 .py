##Prof G - Header docs should contain separate sections for parameters and what
##Prof G - is returned by the function.

##Prof G - for example

"""
This function ...

Parameters:
    word_list: A list of words
    max_length: The maximum length of the longest word, all words longer than
                max_length will be truncated.
                
Returns:
    list of truncated words
    
"""


### Problem 1 ###
"""
Write a version of a palindrome recogniser that accepts a file
name from the user, reads each line, and prints the line to the
screen if it is a palindrome
"""

##Prof G - Works pretty well but fails a few test cases. Nice handling of mixed
##Prof G - case. THe failed cases are a result of not stripping blanks and
##Prof G - punctuation.
def recogniser(file_name):
    """
    This palindrome recognizser function accepts a file name from the user,reads
    each line and prints the line to the screen if it's a palindrome
    """ 
    text = open(file_name).read() #open the file and make it readable 
    list1 = text.split('\n') #get a list
    for i in range(len(list1)): #use for loop
        reversed_elt = list1[i][::-1] #reverse the element
        lowerCase = reversed_elt.lower() #make sure all the element in the list is lower case
        if lowerCase == list1[i].lower(): #if it's a palindrome
            print(list1[i]) #print the word
            

### Problem 2 ###
"""
According to Wikipedia, a semordnilap is a word or phrase that
spells a different word or phrase backwards. ("Semordnilap" is
itself "palindromes" spelled backwards.) Write a semordnilap
recogniser that accepts a file name (pointing to a list of words)
from the user and finds and prints all pairs of words that are
semordnilaps to the screen. For example, if "stressed" and
"desserts" is part of the word list, the the output should include
the pair "stressed desserts". Note, by the way, that each pair by
itself forms a palindrome
"""

##Prof G - Nice, hanles all test cases.
def semordnilap(file_name):
    """
    This function accepts a file name from the user and finds and prints all pair
    of words that are semordnilaps to the screen
    """
    file = open(file_name) #open a file, and the default file access mode is r
    text = file.read().lower() #read the text and make all the characters lower case
    list1 = text.split() #form a list of words
    new_list = [] #empty list
    for i in range(len(list1)-1): 
        for j in range(i+1,len(list1)): 
            #use for loop and inner loop to compare words
            if list1[i] == list1[j][::-1]: #if the words we compare are semordnilaps
                new_list.append(list1[i]) 
                new_list.append(list1[j])   
                #append the pair of words to the new_list
    print(new_list) #print the new_list with all pairs of words that are semordnilaps
    

### Problem 3 ###
"""
Write a procedure char_freq_table()that, when run in a terminal,
accepts a file name from the user, builds a frequency listing of
the characters contained in the file, and prints a sorted and
nicely formatted character frequency table to the screen
"""

##Prof G - Nice work.
def char_freq_table(file_name):
    """
    This function will accept a file name from the user and build a frequency listing
    of the characters contained in the file. Also it will print a sorted formatted 
    character frequency table to the screen in the order of alphabet
    """
    text = open(file_name).read() #open the file and read byte by byte in the text
    lines = text.lower().replace(" ","") #get rid of white spaces and convert characters to lowercase
    elt = lines.split('\n') #form a list of elements by lines
    d = {}  #create an empty dictionary 
    for i in range(len(elt)): #use for loop to find the element in the list
        for j in range(len(elt[i])): #use inner loop to find the exact character in that element
            if elt[i][j] not in d: #if the character is not in the dictionary 
                d[elt[i][j]] = 1   #append the character as a key to d and set the frequency as 1
            else:
                d[elt[i][j]] = d[elt[i][j]] + 1 #frequency +1
    keys = sorted(d.keys())  #sorting dictionary
    for word in keys: 
        print("%s: %s" % (word, d[word])) #print the new dictionary with sorted characters


### Problem 4 ###
"""
The International Civil Aviation Organization (ICAO) alphabet
assigns code words to the letters of the English alphabet
acrophonically (Alfa for A, Bravo for B, etc.) so that critical
combinations of letters (and numbers) can be pronounced and
understood by those who transmit and receive voice messages by
radio or telephone regardless of their native language, especially
when the safety of navigation or persons is essential. Here is a
Python dictionary covering one version of the ICAO alphabet: d =
{'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta',
'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel',
'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa',
'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango',
'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray',
'y':'yankee', 'z':'zulu'} Your task in this exercise is to write a 
procedure speak_ICAO()able to translate any text (i.e. any string)
into spoken ICAO words. You need to import at least two libraries:
osand time. On a mac, you have access to the system TTS
(Text-To-Speech) as follows:os.system('say'+msg), where msg is the
string to be spoken.
"""
import os
import time

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta',
'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel',
'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa',
'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango',
'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray',
'y':'yankee', 'z':'zulu'} #create the ICAO alphabet dictionary

##Prof G - Doesn't work on my mac. Like several others, the problem is that you
##Prof G - need a space after 'say '. Also, this should handle numbers.
def speak_ICAO(txt_file, pause1, pause2 ):
    """
    This function will pronounce the message using ICAO
    """
    words = txt_file.lower().split() #open the file and make it a list of lower case words
    for word in words: 
        for char in word: 
            if char in d: 
                os.system('say' + d[char]) #access Text-to-speech syetem where d[char] is the string to be spoken
                time.sleep(pause1) #pause between each character and its ICAO
        time.sleep(pause2) #pause between words
    

### Problem 5 ###
"""A hapax legomenon (often abbreviated to hapax) is a word which
occurs only once in either the written record of a language, the
works of an author, or in a single text. Define a function that given
the file name of a text will return all its hapaxes. Make sure your
program ignores capitalization
"""

def hapax(file_name):
    """
    This function will read a given text and return the word that only appear once
    """
    file = open(file_name) #open the file
    text = file.read()  #read the text by bytes
    lowerCase = text.lower() #make sure the text is lowercase only
    words = lowerCase.split() #make a list of words
    freqs = {key: 0 for key in words} #save the words in the dictionary
    for word in words:
        freqs[word] += 1 
    for word in freqs:
        if freqs[word] == 1: #if the word only appear once in the list
            print(word) #print the word
            

### Problem 6 ###
"""
Write a program that given a text file will create a new text file in
which all the lines from the original file are numbered from 1 to n
(where n is the number of lines in the file).
"""

def line_num(file_name):
    """
    This function will write a new text file by adding line number to the original
    text
    """
    file = open(file_name) #open the file
    text = file.readlines() #return a list containing the lines 
    f = open('new_file','w') #create a new file for writing only
    for i in range(len(text)): #use for loop
         f.write(str(i+1) +' ' + text[i]) #add line number at the beginning and make a space between the number and text
    f.close() #close the file so it cannot be read or written anymore
    

### Problem 7 ###
"""
Write a program that will calculate the average word length of a text
stored in a file (i.e the sum of all the lengths of the word tokens in
the text, divided by the number of word tokens). 
"""

def avg_length(file_name):
    """
    This function will calculate the average word length of a text stored in a file
    """
    file = open(file_name) #open the file
    text = file.read() #read the file as text
    list1 = text.split() #form a list
    count = 0 #initialize count
    
    for word in list1: #use for loop 
        count = count + len(word) #count the lengths of the word tokens and store the value in count
    result = count/len(list1) #get the result by dividing count by the number of words in list1
    return result #return the average word length
        


### Problem 8 ###
"""
Write a program able to play the "Guess the number"-game, where
the number to be guessed is randomly chosen between 1 and 20.
(Source: http://inventwithpython.com) This is how it should work
when run in a terminal: >>> import guess_numberHello! What is
your name?TorbjörnWell, Torbjörn, I am thinking of a number
between 1 and 20. Take a guess. 10Your guess is too low.Take
a guess.15Your guess is too low.Take a guess.18Good job,
Torbjörn! You guessed my number in 3 guesses
"""
import random

##Prof G - Why is this not a function?
name = input('What is yout name?\n') 
        #What the guesser enters will be stored as a string in name
print('Well, %s, I am thinking of a number between 1 and 20.' %name) 

number = random.randint(1,20) #generate a random integer between [1,20]
guess = int(input('Take a guess.\n')) 
        #input() function returns what we entered as a string,
        #int is a class that convert an string to an integer
count = 1 #initialize the first guess as count = 1

while number != guess:
    if guess < number: # if the guessed number is smaller than the number generated
        print('Your guess is too low') #tell the guesser that the guess is too low
    elif guess > number:        #else if the guessed number is larger than the number generted
        print('Your guess is too high') #tell the guesser that the guess is too high
    guess = int(input('Take a guess.\n')) #Take another guess 
    count = count + 1 #number of guess +1

print('Good job, %s! You guessed my number in %d guesses!' %(name, count)) 
#if this time the guess is exactly same as the number, print as above


### Problem 10 ###
"""
In a game of Lingo, there is a hidden word, five characters long.
The object of the game is to find this word by guessing, and in
return receive two kinds of clues: 1) the characters that are fully
correct, with respect to identity as well as to position, and 2) the
characters that are indeed present in the word, but which are
placed in the wrong position. Write a program with which one can
play Lingo. Use square brackets to mark characters correct in the
sense of 1), and ordinary parentheses to mark characters correct in
the sense of 2). Assuming, for example, that the program conceals
the word "tiger", you should be able to interact with it in the
following way: >>> import lingo snakeClue: snak(e) fiest
Clue: f[i](e)s(t) timesClue: [t][i]m[e]s tiger Clue:
[t][i][g][e][r] 
"""

##Prof G - NIce but doesn't handle repeated characters. Try "catch".
def lingo(word):
    """
    This function sets a five-letter hidden word and let the player guess the word.
    While playing, if the characters that are fully correct, with respect to identity
    as well as to position, give the clue by using square brackets to mark characters. 
    If the characters that are in the word but which are not in the right position, give 
    player hint by using ordinary parentheses
    """
    
    while True:
        guess = input('Guess a word.\n') #make the player guess a word
        clue ='' #empty string
    
        if len(guess) == len(word):
            for i in range(len(word)): #use for loop
                if word.find(guess[i]) == i: #determine if the character is in the hidden word and the same location
                    clue = clue + '[' + guess[i]+ ']' 
                    #give player the clue if the character guessed is fully correct with respect to
                    #identity as well as to position
                elif guess[i] not in word:  
                    clue = clue + guess[i]
                    #if no characters in the words are guessed right (with respect to identity and location),
                    #nothing happens
                else:
                    clue = clue + '(' + guess[i]+ ')'
                    #if the character in the word guessed is in the hidden word,  give another type of clue
            print(clue) 
            if guess == word:  #when the guess is right
                print('You got it!') #print 'You got it!'
                break
    

### Problem 11 ###
"""
A sentence splitter is a program capable of splitting a text into sentences. The standard set of heuristics for sentence
splitting includes (but isn't limited to) the following rules:
Sentence boundaries occur at one of "."(periods), "?" or "!", except that
a. Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
b. Periods followed by a digit with no intervening whitespace are not sentence boundaries.
c. Periods followed by whitespace and then an upper case letter, but preceded by any of a short list of titles are
   not sentence boundaries. Sample titles include Mr., Mrs., Dr., and so on.
d. Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries (for example,
   www.aptex.com, or e.g).
e. Periods followed by certain kinds of punctuation (notably comma and more periods) are probably not sentence boundaries.
Your task here is to write a program that given the name of a text file is able to write its content with each sentence
on a separate line. Test your program with the following short text: Mr. Smith bought cheapsite.com for 1.5 million dollars,
i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a
probability of .9 it isn't. The result should be:
Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. \n
Did he mind? \n
Adam Jones Jr. thinks he didnt. \n
In any case, this isn't true... \n
Well, with a probability of .9 it isn't.
"""

def sen_splitter(text):
    """
    This function is capable of splitting text into sentences by the rules given above
    """
    text = text.replace('\n',' ') # combine all the lines together and make them one line
    newText=[]   #empty new text
    isDot = False 
    current_sen = '' #create an empty string
    i=0  #initialze i = 0
    while True: 
        if i == len(text):   #if i is not in the range of text
            return newText  # return the output
        elif i == len(text) - 1:    #if i is the last character
            current_sen = current_sen + text[i] #add the character to the currentSen
            newText.append(current_sen) # append the final sentence to the list
        else:
            current_sen= current_sen + text[i]  #add character
            if text[i]=='?': # if it's a ?, sentence boundary occurs
                newText.append(current_sen)
                current_sen = ''
                isDot = False
            elif text[i]=='!': # if it's !, sentence boundary occurs
                newText.append(current_sen)
                current_sen = ''
                isDot = False
            elif text[i] == '.': 
                isDot = True
            elif text[i] == ' ':  #if there is a whitespace after period
                if isDot == True:
                    if text[i+1].islower():
                        isDot = False  #Periods followed by whitespace followed by a lower case letter
                                        #are not sentence boundaries
                    elif text.find('Mr.',i-3) == i-3:
                        isDot = False
                    elif text.find('Dr.',i-3) == i-3:
                        isDot = False
                    elif text.find('Mrs.',i-4) == i-4:
                        isDot = False
                        #Periods followed by whitespace and then an upper case letter,
                        #but preceded by any of a short list of titles are not sentence
                        #boundaries. Sample titles include Mr., Mrs., Dr., and so on.
                    else:
                        newText.append(current_sen) #append currentSen to newTEXT
                        current_sen = ''
        i=i+1


def write_sentence_split(file_name):
    """
    This function open a file and break the sentences in the file and create a file with rewrited 
    setences
    """
    file=open(file_name) # open the file
    text = file.read() # make the file readable and read the file
    file.close() # close the file
    splittedText= sen_splitter(text) # split the sentences and make it a list
    ##Prof G - The next line fails when file_name contains the entire path.
    newFilepath = 'splitted' + file_name # create a new file
    newFile = open(newFilepath, 'w') # open the new file for writing only
    for i in range(len(splittedText)): #use for loop
        newFile.write(splittedText[i]+'\n') # write a sentence in a line into the new file
    newFile.close()  #close the file we just created


    
    




        
    
            
    
            
            
    
            
        

        
        
    
    
        
    
    
       
        
    
    

    
    
    
    
    