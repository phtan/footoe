import sys
import argparse

from helpers import getAllPreFootnotes, ensureAllUnique
from helpers import ensureAllPreHasCounterpartAmongPostFootnotes
from helpers import convertToNumbers, replacePreFootnotesWithNumbers
from helpers import getMapOfReplacements, getAllPostFootnotes
from helpers import replacePostFootnotesWithNumbers

def getTextFromFile():
    """
    self-explanatory.
    
    Returns:
        some_text(str)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
    "file_name",
    help="the file containing the text you want to convert/process",
    type=str
    )
    args = parser.parse_args()
    
    f = open(args.file_name, "r")
    return f.read()
  
def convert(your_text):
    """
    Changes foot-notes into numbered foot-notes
    Args:
        your_text (str): a certain text
    Returns:
        str

    """
    print(f"Hello world, I plan to convert the following text: {your_text}")
    
    ### Terminology
    # Given a four-line text that looks like the (somewhat mal-formed)
    # following:
    # ===
    # Hola mundo [^1]. Hello world. [^2].
    # 
    # [^a]: Spanish
    # [^b]: English
    # ===
    # I refer to [^1] and [^2] as Pre Footnotes, and
    # [^a] and [^b] as Post Footnotes
    
    pre = getAllPreFootnotes(your_text)
    post = getAllPostFootnotes(your_text)
    
    ensureAllUnique(pre) # make sure no duplicates occur
    ensureAllUnique(post)
    # TODO: update Readme to reflect the above expectation of no duplicates
    
    ensureAllPreHasCounterpartAmongPostFootnotes(pre, post) # defensive coding
    
    a_map = mapFootnotesToNumbers(pre) # I suppose either pre or post would work as an argument, given the checks above
    
    converted_text = replaceFootnotesWithNumbers(a_map, your_text)
    
    return converted_text

def writeToFile(converted_text):
     # TODO
    print("hello, here's a TODO")
    
def main():
    text = getTextFromFile()
    new_text = convert(text)
    writeToFile(new_text)
    
if __name__ == "__main__": # we want main() to run if called from command-line
    main()
