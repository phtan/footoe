"""
helper functions
"""

import re

ERROR_MESSAGE_NO_DUPLICATES = "the given list should not have duplicates"

def getAllPreFootnotes(some_text): # type: (str) -> list
    print("getting all Pre Footnotes...")
    pattern = r"\[\^([^\]]+)\](?!:)" # exclude the character ":" (i.e. colon)
    return re.findall(pattern, some_text) 
    
def getAllPostFootnotes(some_text): # type: (str) -> list
    print("getting all Post Footnotes...")

def ensureAllUnique(some_list): # type: (list) -> None
    print("Ensuring unique-ness among Pre Footnotes...")
    
    # A set, in Python, can only have non-duplicates.
    # So we cast some_list into a set, then check if the resulting
    # set has the same number of items/entries as the original list.
    assert len(set(some_list)) == len(some_list), ERROR_MESSAGE_NO_DUPLICATES

def ensureAllPreHasCounterpartAmongPostFootnotes(some_list): # type: (list) -> None
    print("Ensuring a counterpart, for each Pre, among the Post Footnotes...")

def convertToNumbers(some_list): # type: (list) -> list
    print("Numbering Pre Footnotes...")
    
def replacePreFootnotesWithNumbers(some_text, some_list): # type: (str, list) ->  None
    print("Replacing Pre Footnotes with numbers...")
    
def getMapOfReplacements(some_list, list_of_numbers): # type: (list, list) -> dict
    print("Getting a map of replacements among Pre Footnotes...")

def replacePostFootnotesWithNumbers(some_dict, some_list): # type: (dict, list) -> None
    print("Replacing Post Footnotes with numbers...")
    # for element in some_dict:
    #    replaceAmongPostFootnotes(some_list, element.old, element.new)

    