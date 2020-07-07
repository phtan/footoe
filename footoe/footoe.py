import sys
import argparse
import re

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
        None

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
    ensureAllUnique(pre) # make sure no duplicates occur
    ensureAllPreHasCounterpartAmongPostFootnotes(pre) # defensive coding
    numbered = convertToNumbers(pre)
    replacePreFootnotesWithNumbers(your_text, numbered)
    map = getMapOfReplacements(pre, numbered)
    
    post = getAllPostFootnotes(your_text)
    for element in map:
        replaceAmongPostFootnotes(post, element.old, element.new)

def writeToFile(converted_text):
     # TODO
    print("hello, here's a TODO")
    
def main():
    text = getTextFromFile()
    new_text = convert(text)
    writeToFile(new_text)
    
if __name__ == "__main__": # we want main() to run if called from command-line
    main()
