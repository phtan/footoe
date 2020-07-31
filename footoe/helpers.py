"""
helper functions
"""

import re

ERROR_MESSAGE_NO_DUPLICATES = "the given list should not have duplicates"
ERROR_MESSAGE_SHOULD_HAVE_COUNTERPART = "the two given lists should contain the same elements/footnotes"

def getAllPreFootnotes(some_text): # type: (str) -> list
    print("getting all Pre Footnotes...")
    pattern = r"\[\^([^\]]+)\](?!:)" # exclude the character ":" (i.e. colon)
    return re.findall(pattern, some_text) 
    
def getAllPostFootnotes(some_text): # type: (str) -> list
    print("getting all Post Footnotes...")
    pattern = r"\[\^([^\]]+)\]:"
    return re.findall(pattern, some_text)

def ensureAllUnique(some_list): # type: (list) -> None
    print("Ensuring unique-ness among Pre Footnotes...")
    
    # A set, in Python, can only have non-duplicates.
    # So we cast some_list into a set, then check if the resulting
    # set has the same number of items/entries as the original list.
    assert len(set(some_list)) == len(some_list), ERROR_MESSAGE_NO_DUPLICATES

def ensureAllPreHasCounterpartAmongPostFootnotes(some_list, another_list): # type: (list, list) -> None
    print("Ensuring a counterpart, for each Pre, among the Post Footnotes...")
    assert some_list == another_list, ERROR_MESSAGE_SHOULD_HAVE_COUNTERPART

def mapFootnotesToNumbers(some_list): # type: (list) -> dictionary

    print("Mapping footnotes to numbers...")
    # Initialise
    output = {} # an empty dictionary
    count = 1
    
    
    # Here's a "magic constant"
    step = 1
    
    # now iterate over the given list
    for i in some_list:
        number = str(count)
        output[i] = number
        count += step
    
    return output
    
def replaceFootnotesWithNumbers(some_text, some_map): # type: (str, dictionary) -> str
    print("Replacing footnotes with numbers...")

    