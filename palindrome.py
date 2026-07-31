


def is_palindrome(text):
    ##.lower to force all values in the CLEAN_TXT variable to lowercases and ".replace"(" ", "") removes all spaces.
    clean_texts = text.lower().replace(" ", "") #
    # implemented a SLICE that returns a boolen
    return clean_texts == clean_texts[:: - 1] 

# test_cases = (
#         ("Was it a car or a cat I saw", True),  # Palindrome
#         ("racecar", True),                       # Palindrome
#         ("hello", False),                       # Not a palindrome
#         ("toot ", True),                      # Not a palindrome
#         ("A man a plan a canal Panama", True),  # Palindrome (famous example)
#         ("No lemon no melon", True),            # Palindrome
#         ("Never odd or even", True),            # Palindrome
#   )
    

test_cases = ["Was it a car or a cat I saw",
"No lemon no melon", "Noon day is noon", 
"my name is Famous not pupular",]
#TEST CASE OPTION 1. Here I used the if statement in the test case
for test_string in test_cases:
        result = is_palindrome(test_string)
        if result == True:
            print(f"✅ '{test_string}': {result} ")
        else:
            print(f"❌ '{test_string}': {result} ")

# Sir which is prefarable for the test case SIR?
#TEST CASE OPTION 2.....Loading 
