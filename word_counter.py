def count_words(text):
    """ returns the number of words in a string #(use.split())."""
    return len(text.split())



def count_characters(text, include_spaces=True):
    """returns the character count, with a keyword argument controlling
    whether spaces are counted.
    """
    if include_spaces == True:
        return len(text)
    else:
        return len(text.replace(" ", ""))
    
        

def text_report(text):
    """ A function that calls both of the above and returns a formatted
    multi-line string summarizing the results (this function is allowed 
    to combine results, but should not do the counting itself).
    """
    characters = count_characters # Using the characters VARIABLE to calls the "characters" FUNCTION of the previous stage"
    words = count_words # Using the words " VARIABLE to call the "count_words" FUNCTION of the previous stage
  
    return (f"Sentences: {sentence}\n"
            f"Number of characters: {words(sentence)}\n"
            f"Numbers of words : {characters(sentence)}")

# MAIN SECTION
sentence = " am not a fool because I chosed God"
print(text_report(sentence))


# sentence ="I am a student of Evolve school of computation"
# print(f"Words in Sentence = {text_report(sentence)} words")


    # print count_words():
    #MAIN SECTION
    # In a main section, test all three functions 
    # with at least two different strings, and print the report.

