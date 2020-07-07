import sys
import argparse

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
    # TODO
  
def convert(your_text):
    """
    Print a line about converting text
    Args:
        your_text (str): a certain text
    Returns:
        None

    """
    print(f"Hello world, I plan to convert the following text: {your_text}")    

def writeToFile(converted_text):
     # TODO
    print("hello, here's a TODO")
    
def main():
    text = getTextFromFile()
    new_text = convert(text)
    writeToFile(new_text)
    
if __name__ == "__main__": # we want main() to run if called from command-line
    main()
