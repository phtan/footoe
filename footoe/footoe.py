import sys
import argparse

import helpers as h

# "Magic" constants
OUTPUT_NAME = "footoe_output.txt"
FILE_WRITING_MODE = "x"

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
    
    pre = h.getAllPreFootnotes(your_text)
    post = h.getAllPostFootnotes(your_text)
    
    h.ensureAllUnique(pre) # make sure no duplicates occur
    h.ensureAllUnique(post)
    # TODO: update Readme to reflect the above expectation of no duplicates
    
    h.ensureAllPreHasCounterpartAmongPostFootnotes(pre, post) # defensive coding
    
    a_map = h.mapFootnotesToNumbers(pre) # I suppose either Pre Footnotes or Post Footnotes would work as an argument, given the checks above
    
    converted_text = h.replaceFootnotesWithNumbers(your_text, a_map)
    
    return converted_text

def writeToFile(converted_text):
    
    some_file = open(OUTPUT_NAME, FILE_WRITING_MODE) # TODO out of curiosity, change FILE_WRITING_MODE to "a"; and also find out what "w" does
    some_file.write(converted_text)
    some_file.close()
    
def main():
    text = getTextFromFile()
    new_text = convert(text)
    writeToFile(new_text)
    
if __name__ == "__main__": # we want main() to run if called from command-line
    main()
