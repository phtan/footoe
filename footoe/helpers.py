"""
helper functions
"""

import re

ERROR_MESSAGE_NO_DUPLICATES = "the given list should not have duplicates"
ERROR_MESSAGE_SHOULD_HAVE_COUNTERPART = "the two given lists should contain the same elements/footnotes"

def getAllPreFootnotes(some_text): # type: (str) -> list
    # print("getting all Pre Footnotes...")
    pattern = r"\[\^([^\]]+)\](?!:)" # exclude the character ":" (i.e. colon)
    return re.findall(pattern, some_text) 
    
def getAllPostFootnotes(some_text): # type: (str) -> list
    # print("getting all Post Footnotes...")
    pattern = r"\[\^([^\]]+)\]:"
    return re.findall(pattern, some_text)

def ensureAllUnique(some_list): # type: (list) -> None
    # print("Ensuring unique-ness among Pre Footnotes...")
    
    # A set, in Python, can only have non-duplicates.
    # So we cast some_list into a set, then check if the resulting
    # set has the same number of items/entries as the original list.
    assert len(set(some_list)) == len(some_list), ERROR_MESSAGE_NO_DUPLICATES

def ensureAllPreHasCounterpartAmongPostFootnotes(some_list, another_list): # type: (list, list) -> None
    # print("Ensuring a counterpart, for each Pre, among the Post Footnotes...")
    assert some_list == another_list, ERROR_MESSAGE_SHOULD_HAVE_COUNTERPART

def mapFootnotesToNumbers(some_list): # type: (list) -> dictionary

    # print("Mapping footnotes to numbers...")
    
    # Initialise
    output = {} # an empty dictionary
    numbers = range(1, len(some_list)+1) # override the default starting number (that is, zero)
    
    # Use Dictionary/List Comprehension
    #
    # e.g.
    # >>> d = {n: n**2 for n in range(5)}
    # >>> print d
    # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}    
   
    output = {some_list[n-1]: str(n) for n in numbers} # e.g. {some_list[0]: "1"}
    
    return output
    
def replaceFootnotesWithNumbers(some_text, some_map): # type: (str, dictionary) -> str
    # print("Replacing footnotes with numbers...")
    temp = some_text
    replaced_footnotes = ""
    
    for fn, num in some_map.items():
        # we use buildFootnote; replace only what looks like a footnote
        replaced_footnotes = temp.replace(buildFootnote(fn), buildFootnote(num))
        temp = replaced_footnotes # carry over the replacements from one iteration to the next
        
    return replaced_footnotes
    
def buildFootnote(some_text): # type: (str) -> str
    output = "[^" + some_text + "]"
    return output
