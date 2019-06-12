"""A collection of function for doing my project."""

import string

END_CHAT = ['nevermind','goodbye','bye']

# comment which ones ive taken
# Removes punctuation
def remove_punctuation(input_string):
    """Takes all punctuation out of a string."""
    out_string=""
    for character in input_string:
        if character not in string.punctuation:
            out_string += character
    return out_string.lower()

# Process inputs
def prepare_text(input_string):
    """Makes string lowercase and removes punctuation."""
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    return temp_string

# Ends chat with bot
def end_chat(my_input):
    """Checks if user inputted words to end program"""
    if (my_input in END_CHAT):
        return True
    else:
        return False

    