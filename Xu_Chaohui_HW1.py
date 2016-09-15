"""
@author: Chaohui Xu
Homework 1 Group F
"""

### Problem 1 ###
def my_max(a,b):
    """
    This function takes two numbers as arguments and returns largest of them
    """
    if a < b:         #if b is larger than a 
        print(b, 'is larger than', a)   #then print 'b is larger than a'
    elif a == b:        #else if a is equal to b
        print(a, 'is equal to', b)  #print 'a is equal to b'
    else:  #otherwise
        print(a, 'is larger than', b)  #print 'a is larger than b')
#Example        
my_max(9,20)



### Problem 2 ###
def max_of_three(a, b, c):
    """
    This function takes three numbers as arguments and returns the largest of them
    """
    if b < a:    #First comparing a and b, if b < a
       t = a     #store the value of a in t
    elif a < b:  #else if a < b
        t = b    #store the value of b in t
    if t > c:    #Comparing the value c and t passed from any situation above, if t > c
        return t #t is the largest number, return t
    else:        #Otherwise
        return c #return c
#Example
max_of_three(9,21,8)
    


### Problem 3 ###
def length(string):
    """
    This function computes the length of a given list or string
    """
    l = 0    #initialize l
    for x in string: #use for loop 
        l = l + 1  #store l+1 in l, iterate till the end of the list or string
    return l   #obtain the value of the length of the list or string
#Example
length('I am testing!')



### Problem 4 ###
def vowel(char):
    """
    This function takes a character and returns True if it's a vowel, False otherwise
    """
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u': #if the character is a vowel
        return True   #return True
    else:   
        return False   #Otherwise, return False
        
#Example
vowel('a')
        



### Problem 5 ###
def translate(text):
    """
    This function will translate  a text into rövarspråke. 
    That is double every consonant and place an occurence of "o" in between
    """
    cons = 'bcdfghjklmnpqrstvwxz'  #define all the consonants
    a = ''      #create a null string
    for i in text : #use for loop
        if i in cons:   #if i is consonant
            a = a + i + 'o' + i  #double i and place an "o" in between, and a becomes a new string
        else:
            a = a + i  #if i is a vowel, add i to the string without doing anything else
    return a #return the translated string 
    
#Example
translate('this is fun')
    



### Problem 6 ###
def my_sum(number):
    """
    This function sums all the numbers in a list of numbers
    """
    total1 = 0   #initialize total1
    for i in number: #use for loop
        total1 = total1 + i #add each i for i in number 
    return total1  #return the sum of all numbers in the list
#Example
my_sum([2,5,9,1])

def multiply(multiplier):
    """This function multiplies all the numbers in a list of numbers
    """
    total2 = 1 #initialize total2
    for m in multiplier:    #use for loop
        total2 = total2 * m #multiply each m for m in the list
    return total2 #return the result
#Example
multiply([2,9,8])

    


### Problem 7 ###
def reverse(text):
    """
    This function return the reversal of a string
    """
    l = len(text) #initialize l, which is the length of the input text
    a = '' #create a empty string
    for i in range(len(text)): #use for loop
        a = a + text[l - i - 1] #put each character in the new string backwards
    return a  #return the reversed string
#Example 
reverse('I am testing')




### Problem 8 ###
def is_palindrome(text):
    """
    This function will recognize palindromes and return True if it's palindrome
    """
    lowerCase = text.lower()   #convert the text to lowercase 
    reversedString = lowerCase[::-1] #reverse a string
    if lowerCase == reversedString:  #if the converted imput string and the reversed string looks exactly the same
        return True #return True
    else:
        return False #otherwise, return False
#Example
is_palindrome('Civic')
        
        


### Problem 9 ###
def is_member(value,array):
    """
    This function takes a value a and a list of values x. If x is a member of a, return True.
    Otherwise, False.
    """
    for item in array: #use for loop
        if item == value: #if the element in array is same as the value 
            return True     #return True
    return False  #otherwise, return False
#Example
is_member(4,[4,5,7,6])

            
    

### Problem 10 ###
def overlapping(list1,list2):
    """
    This function takes two lists and returns True if they have at least one 
    member in common, False otherwise.
    """
    for item1 in list1: #use for loop
        for item2 in list2: #use nested for loop
            if item1 == item2:  #compare the element in two lists, if they have at least one member in  common
                return True   #return True
    return False #otherwie, return False

#Example
overlapping([4,5,6],[9,7,8])
    
    

### Problem 11 ###
def generate_n_chars(n, c):    
    """
    This function takes an integer n and a character c and returns a string n 
    characters long
    """
    char = ''   #create an empty string
    for i in range(n):  #use for loop 
        char = char + c #put each character in the string
    return char     #return c that is n characters long
    
#Example
generate_n_chars(7,'#')
    


### Problem 12 ###
def histogram(numbers):
    """
    This function takes a list of integers and prints a histogram to the screen
    """
    a = '' #create an empty string
    for n in numbers: #use for loop
        a = a + n * '*' + ' ' #print '*' n times and store the new string in a
    return a #generate the histogram

#Example
histogram([2,10,4])

        

### Problem 13 ###
def max_in_list(list1):
    """
    This function will return the largest number from a list of numbers
    """    
    currentMax = list1[0] #set the fisrt number in the list to be the currentMax 
    for number in list1: #use for loop
        if number > currentMax: #if the number in the list is larger than currentMax
            currentMax = number #the new number takes the place as being the largest one and store the new value in currentMax
    return currentMax #return the largest number in the list

#Example
max_in_list([1,2,4,3,5])
    


### Problem 14 ###
def map_to_lengths(words):
    """
    This function maps a list of words into a list of integers representing the 
    lengths of the corresponding words
    """
    return list(map(len,words)) #use len() function to map the list of words to a list of 
                                #integers representing the lengths of the corresponding words
#Example
map_to_lengths(['how','I','met','your','mother'])
    


### Problem 15 ###
def find_longest_word(words):
    """
    This function takes a list of words and returns the length of the longest one
    """
    return max(list(map(len,words))) #use len() function to map the list of words to a list of 
                                    #integers representing the lengths of the corresponding words   
                                    #,and use max() function to get the largest number

#Example
find_longest_word(['Hilary','Clinton','is','the','right','and','responsible','choice','for','the','election'])


### Problem 16 ###
def filter_long_words(list1, number):
    """
    This function takes a list of words and an integer n and returns the list of words
    that are longer than n. In my function, I defined the list as list1 and n as number.
    """
    listwords = []  #create a new list
    for i in range(len(list1)): #use for loop
        if len(list1[i]) > number: #if the length of the word in list is larger than the number we set
            listwords = listwords + [list1[i]] #append the word to the list
    return listwords #return the list of words in which the length is larger than the integer n

#Example
filter_long_words(['elephant','panda','cat','lion','antelope','dog'],3)
            
            
        
    
    








        
        
        
    
    



   
   
   
    
    
    
    
    
    
    

    
    






  
    
        
    

    
    





