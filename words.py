def uppercase_prints(listItems):
    """Prints all items of list in uppercase"""
    for string in listItems:
        string = string.upper()
        print(string)
#uppercase_prints(["hello", "hey", "goodbye", "yo", "yes"])
        

def print_e_words(listItems):
    """Prints words that start with "E" of list in uppercase"""
    for string in listItems:
        string = string.upper()
        if string.startswith('E'):
            print(string)

#print_e_words(["eello", "hey", "eoodbye", "yo", "yes"])        

def print_words_starting_with(listItems, must_start_with ):
    """Prints words starting with letters specified in set"""
    for string in listItems:
        for letter in must_start_with:
            if letter == string[0].upper() or letter == string[0].lower():
                print(string.upper())
                break
            
#print_words_starting_with(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
