import sys

def getTextFromFile():
    file_name = sys.argv[1] # naively
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
