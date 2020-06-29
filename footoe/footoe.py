import sys

def convert(your_text):
    """
    Print a line about converting text
    Args:
        your_text (str): a certain text
    Returns:
        None

    """
    print(f"Hello world, I plan to convert the following text: {your_text}")    
    
    
def main():
     list_of_some_text = sys.argv[1:] # naively get input, for now
     convert(list_of_some_text) # this argument is not the expected type, a str

if __name__ == "__main__":
    main()
