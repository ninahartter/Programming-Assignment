# -*- coding: utf-8 -*-
"""
Programming Assignment 
1) Basic Python: Scrambled Text

Created on Thu Feb 27 17:41:10 2020
@author: Nina

This program defines 4 different functions that all scramble a piece of text in
a different way. 

- reorder_middle(): Randomly reorders all but the first and last letters of 
each word.

- reorder_complete(): Randomly reorders all letters of each word.

- reorder_size(): Randomly reorders all letters of each word that are shorter 
than a given number of letters.

- random_upper_lower(): Randomly makes some letters of each word upper and some
lower case.

- backwards(): Spells each word backwards.

"""

import random
import re


# %% Define reorder_middle() function

def reorder_middle(text):
    
    """Randomly reorders all but the first and last letters of each word.
    
    Example:
    >>> reorder_middle('I would like some icecream please.')
    ['I wluod lkie smoe iaecrcem paesle'] 
    
    Arguments:
        text: A string
        
    Returns:
        A string containing the shuffled words.
    
    Raises:
        ValueError: If the text entered only consists of numbers.
    
    """
# Raises a Value Error if the text entered only consists of numbers.
    if text.isnumeric() is True:
        raise ValueError('Enter some words please.')

# Creates a list in which each punctuation sign and each word is a separate
# item. Source: https://stackoverflow.com/questions/367155/splitting-a-string-
# into-words-and-punctuation
    original = re.findall(r"[\w]+|[^\s\w]", text)

# Loops through this list and if the item consists of letters, its position is
# saved under the variable 'position'. Then a list of characters for this item
# is created.           
    for item in original:
        if item.isalpha() is True:
            position = original.index(item)
            char_list = list(item)
            
# Checks whether a word (which is split into characters) is longer than three 
# characters (as only then the word changes if the letters are reordered). 
# If this is the case, three separate variables containing the first and the 
# last letter and the middle part of each word are created.
            if len(char_list) > 3:         
                first_letter = char_list[0]           
                last_letter = char_list[-1]
                middle_part = char_list[1:-1]
                  
# Shuffles the characters of the middle part of the word and joins the characters
# together into a string.
                random.shuffle(middle_part)
                middle_part = ''.join(middle_part)
    
# Combines the first letter, the middle part and the last letter.       
                item_changed = first_letter + middle_part + last_letter          
    
# Loops through the position of items in the 'original' list and if the index
# of an item is the same as the position of the changed word, the original word
# is replaced by the changed word.
                for index, item in enumerate(original):
                    if index == position:
                        original[index] = item_changed
            
# Joins the items of the original list together, so the output becomes a string.      
    shuffled_output = ' '.join(original)

# Removes the whitespaces before punctuation. 
# Source: https://stackoverflow.com/questions/18878936/how-to-strip-whitespace-
# from-before-but-not-after-punctuation-in-python
    shuffled_output = re.sub(r'\s([?.,!"](?:\s|$))', r'\1', shuffled_output)
        
    return(shuffled_output)
                        

# %% Define reorder_complete() function

def reorder_complete(text):
    
    """Randomly reorders all letters of each word.
    
    Example:
    >>> reorder_complete('I would like some icecream please.')
    ['I oludw leki osme reacmiec laseep.'] 
    
    Arguments:
        text: A string
        
    Returns:
        A string containing the shuffled words.  
    
    Raises:
        ValueError: If the text entered only consists of numbers.
    
    """
# Raises a Value Error if the text entered only consists of numbers.
    if text.isnumeric() is True:
        raise ValueError('Enter some words please.')

# Creates a list in which each punctuation sign and each word is a separate
# item. Source: https://stackoverflow.com/questions/367155/splitting-a-string-
# into-words-and-punctuation
    original = re.findall(r"[\w]+|[^\s\w]", text)

# Loops through this list and if the item consists of letters, its position is
# saved under the variable 'position'. Then a list of characters for this item
# is created.       
    for item in original:
        if item.isalpha() is True:
            position = original.index(item)
            char_list = list(item) 
              
# Shuffles the characters of the word and joins the characters together into a 
# string.
            random.shuffle(char_list)

# The letters in the 'char_list' are joined together into a string.    
            item_changed = ''.join(char_list)   

# Loops through the position of items in the 'original' list and if the index
# of an item is the same as the position of the changed word, the original word
# is replaced by the changed word.
            for index, item in enumerate(original):
                if index == position:
                    original[index] = item_changed
            
# Joins the items of the original list together, so the output becomes a string.      
    shuffled_output = ' '.join(original)

# Removes the whitespaces before punctuation. 
# Source: https://stackoverflow.com/questions/18878936/how-to-strip-whitespace-
# from-before-but-not-after-punctuation-in-python
    shuffled_output = re.sub(r'\s([?.,!"](?:\s|$))', r'\1', shuffled_output)
        
    return(shuffled_output)
    
    
# %% Define reorder_size() function
    
def reorder_size(text, number):
    
    """Randomly reorders all letters of each word that are shorter than a given
    number of letters.
    
    Example:
    >>> reorder_size('I would like some icecream please.',5)
    ['I would kiel eoms icecream please.'] 
    
    Arguments:
        text: A string
        number: an integer. Only words that are shorter than this number are 
        shuffled. 
        
    Returns:
        A string containing the shuffled words.
    
    Raises:
        ValueError: If the text entered only consists of numbers.
        ValueError: If the number entered is not positive.   
        
    """
# Raises a Value Error if the text entered only consists of numbers.
    if text.isnumeric() is True:
        raise ValueError('Enter some words please.')
        
# Raises a Value Error if the number entered is not positive.
    if number < 0:
        raise ValueError('Enter a positive number please.')

# Creates a list in which each punctuation sign and each word is a separate
# item. Source: https://stackoverflow.com/questions/367155/splitting-a-string-
# into-words-and-punctuation
    original = re.findall(r"[\w]+|[^\s\w]", text)

# Loops through this list and if the item consists of letters, its position is
# saved under the variable 'position'. Then a list of characters for this item
# is created.       
    for item in original:
        if item.isalpha() is True:
            position = original.index(item)
            char_list = list(item)

# Checks whether number of characters of each word is shorter than the number
# given.            
            if len(char_list) < number:
              
# Shuffles the characters of the word and joins the characters together into a 
# string.
                random.shuffle(char_list)

# The letters in the 'char_list' are joined together into a string.        
                item_changed = ''.join(char_list)   

# Loops through the position of items in the 'original' list and if the index
# of an item is the same as the position of the changed word, the original word
# is replaced by the changed word.
                for index, item in enumerate(original):
                    if index == position:
                        original[index] = item_changed

# Joins the items of the original list together, so the output becomes a string.      
    shuffled_output = ' '.join(original)

# Removes the whitespaces before punctuation. 
# Source: https://stackoverflow.com/questions/18878936/how-to-strip-whitespace-
# from-before-but-not-after-punctuation-in-python
    shuffled_output = re.sub(r'\s([?.,!"](?:\s|$))', r'\1', shuffled_output)
        
    return(shuffled_output)  


# %% Define random_upper_lower() function
    
def random_upper_lower(text):
    
    """Randomly makes some letters of each word upper and some lower case.
    
    Example:
    >>> random_upper_lower('I would like some icecream please.')
    ['i WOuLd liKE SoMe iCeCREam pleAse.'] 
    
    Arguments:
        text: A string
        
    Returns:
        A string containing the changed words.
        
    Raises:
        ValueError: If the text entered only consists of numbers.
        
    """
# Raises a Value Error if the text entered only consists of numbers.
    if text.isnumeric() is True:
        raise ValueError('Enter some words please.')

# Creates a list in which each punctuation sign and each word is a separate
# item. Source: https://stackoverflow.com/questions/367155/splitting-a-string-
# into-words-and-punctuation
    original = re.findall(r"[\w]+|[^\s\w]", text)

# Loops through this list and if the item consists of letters, its position is
# saved under the variable 'position'. Then a list of characters for this item
# is created.       
    for item in original:
        if item.isalpha() is True:
            position = original.index(item)
            char_list = list(item)


# Creates a new list which will contain the changed characters of each word.
            char_list_changed = []

# Loops through each letter of the list of characters and checks whether it is
# upper- or lower- case. Then a list of an upper- and lower-case version of the
# same letter is created and from this list a random choice is added to the 
# 'char_list_changed'.
            for letter in char_list:
                if letter.isupper():
                    letters = [letter,letter.lower()]
                    char_list_changed.append(random.choice(letters))
                else:
                    letters = [letter,letter.upper()]
                    char_list_changed.append(random.choice(letters))                   

# The letters in the 'char_list_changed' are joined together into a string.       
                item_changed = ''.join(char_list_changed)   
    
# Loops through the position of items in the 'original' list and if the index
# of an item is the same as the position of the changed word, the original word
# is replaced by the changed word.
                for index, item in enumerate(original):
                    if index == position:
                        original[index] = item_changed

# Joins the items of the original list together, so the output becomes a string.      
    shuffled_output = ' '.join(original)

# Removes the whitespaces before punctuation. 
# Source: https://stackoverflow.com/questions/18878936/how-to-strip-whitespace-
# from-before-but-not-after-punctuation-in-python
    shuffled_output = re.sub(r'\s([?.,!"](?:\s|$))', r'\1', shuffled_output)
        
    return(shuffled_output)


# %% Define backwards() function

def backwards(text):
    
    """Spells each word backwards.
    
    Example:
    >>> backwards('I would like some icecream please.')
    ['I dluow ekil emos maerceci esaelp.'] 
    
    Arguments:
        text: A string
        
    Returns:
        A string containing the reversed words. 
    
    Raises:
        ValueError: If the text entered only consists of numbers.    
    
    """
# Raises a Value Error if the text entered only consists of numbers.
    if text.isnumeric() is True:
        raise ValueError('Enter some words please.')

# Creates a list in which each punctuation sign and each word is a separate
# item. Source: https://stackoverflow.com/questions/367155/splitting-a-string-
# into-words-and-punctuation
    original = re.findall(r"[\w]+|[^\s\w]", text)

# Loops through this list and if the item consists of letters, its position is
# saved under the variable 'position'. Then a list of characters for this item
# is created.       
    for item in original:
        if item.isalpha() is True:
            position = original.index(item)
            char_list = list(item) 
            
# Reverses the order of the letters in 'char_list'.              
            char_list.reverse()

# The letters in the 'char_list' are joined together into a string.    
            item_changed = ''.join(char_list)   

# Loops through the position of items in the 'original' list and if the index
# of an item is the same as the position of the changed word, the original word
# is replaced by the changed word.
            for index, item in enumerate(original):
                if index == position:
                    original[index] = item_changed

# Joins the items of the original list together, so the output becomes a string.      
    shuffled_output = ' '.join(original)

# Removes the whitespaces before punctuation. 
# Source: https://stackoverflow.com/questions/18878936/how-to-strip-whitespace-
# from-before-but-not-after-punctuation-in-python
    shuffled_output = re.sub(r'\s([?.,!"](?:\s|$))', r'\1', shuffled_output)
        
    return(shuffled_output)


# %% Testing
    
if __name__ == '__main__': 
    print(reorder_middle('The weather looks nice today, right?'))    
    print(reorder_complete('The weather looks nice today, right?'))    
    print(reorder_size('The weather looks nice today, right?',5))   
    print(random_upper_lower('The weather looks nice today, right?'))    
    print(backwards('The weather looks nice today, right?'))
    
    
# %% Issues for improvment
    
"""
- When using double quotation marks in the text, the output of the functions
will not have the quotation marks framing the word anymore, as the program is 
told to remove the whitespace before punctuation. 

- There might be a more parsimonious way to directly make changes to the words
rather than saving their position in the 'original' list and then replacing 
them by the changed words

"""



