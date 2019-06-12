"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

# Imports
from my_module.functions import remove_punctuation, prepare_text, end_chat

### 
###

# Types of teas in the menu
TEA_TYPES = ['assam black tea', 'jasmine green tea', 'oolong tea','peach green tea',
             'peach black tea','passion fruit green tea','passion fruit black tea',
             'strawberry green tea', 'strawberry black tea','lychee green tea',
             'lychee black tea','mango green tea', 'mango black tea', 'honey green tea', 
             'honey black tea','pineapple green tea','pineapple black tea',
             'kiwi green tea','kiwi black tea','winter melon tea',
             'winter melon green tea','kumquat tea','top fruit tea','signature milk tea',
             'jasmine green milk tea','oolong milk tea','coffee milk tea','taro milk tea',
             'matcha milk tea','chocolate milk tea','honey milk tea','strawberry milk tea',
             'lychee milk tea','winter melon milk tea','peach milk tea','mango milk tea',
             'passion fruit milk tea','brown sugar milk tea','hazelnut milk tea',
             'vanilla milk tea','hokkaido black milk tea','hokkaido oolong milk tea',
             'aloe vera kiwi juice','aloe vera honey juice','honey lemon juice',
             'passion fruit juice','green tea yakult','green tea yogurt','passion fruit yakult',
             'passion fruit yogurt','lychee yakult','lychee yogurt','mango yakult',
             'mango yogurt','strawberry yakult','strawberry yogurt','black tea latte',
             'jasmine green tea latte','hokkaido coffee','mocha coffee','hazelnut coffee',
             'vanilla coffee','ginger tea','longan tea','ginger longan tea','ginger milk tea',
             'longan milk tea']
# Possible topping options
TOPPINGS = ['golden boba','coconut jelly','grass jelly','coffee jelly',
            'rainbow jelly','egg pudding','aloe vera','sea cream','crystal boba']
# Possible size options
SIZES = ['medium','large']
# Possible options for sugar levels
LEVELS = ['normal','less','half','slight','none']
# Possible options for ice levels
ICE = ['normal','half','none']

import string

def main():
    """The main method that handles conversation flow, questions, and types of answers."""
    
    # Introduction question that asks for drink type
    print("Hello, welcome to Ding Tea! What kind of drink would you like?")
    
    chat = True # Variable that checks whether chat continues or not
    while chat:
        
        # Takes drink type from keyboard
        drink_type = input('You:\t')
        # Makes answer case and punctuation insensitive
        drink_type = prepare_text(drink_type)
        
        # Checks if answer is legitimate
        legit_answer = False
        while(legit_answer==False):
            
            # If user ends conversation
            if end_chat(drink_type):
                print("Bye! Thanks for coming")
                chat = False
        
            # If drink isn't avaliable on menu
            if (drink_type not in TEA_TYPES):
                # Prompts for another attempt
                print("Sorry, we don't have that. Is there any other drink you'd like?")
                drink_type = input('You:\t')
                drink_type = prepare_text(drink_type)
            
            # If drink avaliable on menu
            if(drink_type in TEA_TYPES):
                legit_answer = True # Exit loop
            
        # If answer is legitimate
        if (legit_answer):
            
            # Asks for toppings
            result="What toppings would you like in your " + drink_type + "?"
            print(result) 
            # Takes toppings from keyboard
            toppings = input('You:\t')
            toppings = prepare_text(toppings)
            
            # Checks if answer is legitimate
            legit_answer = False
            while(legit_answer==False):
                
                # If user ends conversation
                if end_chat(toppings):
                    print("Bye! Thanks for coming")
                    chat = False
                    break
                    
                # If user specifically answers "none"
                if(toppings == "none"):
                    # Adjust stored value for later
                    toppings = "no toppings"
                    legit_answer = True
                    break
                
                # If toppings isn't avaliable on menu
                if(toppings not in TOPPINGS):
                    # Prompts for another attempt
                    print("Sorry, we don't have that. Is there any other topping you'd like?")
                    toppings = input('You:\t')
                    toppings = prepare_text(toppings)
                    
                # If toppings avaliable on menu
                if(toppings in TOPPINGS):
                    legit_answer = True # Exit loop
            
            # If answer is legitimate
            if(legit_answer):
                
                # Asks for size
                result="Okay, what size would you like?"
                print(result)
                # Takes size from keyboard
                size = input('You:\t')
                size = prepare_text(size)
                
                # Checks if answer is legitimate
                legit_answer = False
                while(legit_answer == False):
                    
                    # If user ends conversation
                    if end_chat(size):
                        print("Bye! Thanks for coming")
                        chat = False
                        break
                    
                    # If size isn't an avaliable option
                    if(size not in SIZES):
                        result = "Sorry, our size options are medium and large. "
                        result += "Is there any other size you'd like?"
                        print(result)
                        # Prompts for another attempt
                        size = input('You:\t')
                        size = prepare_text(size)
                        
                    # If size is an avaliable option
                    if(size in SIZES):
                        legit_answer = True # Exit loop
                
                # If answer is legitimate
                if(legit_answer):
                    
                    # Asks for sugar levels
                    result="Great, what about sugar levels?"
                    print(result)
                    # Takes sugar level from keyboard
                    sugar = input('You:\t')
                    sugar = prepare_text(sugar)
                    
                    # Checks if answer is legitimate
                    legit_answer = False
                    while(legit_answer==False):
                        
                        # If user ends conversation
                        if end_chat(sugar):
                            print("Bye! Thanks for coming")
                            chat = False
                            break
                            
                        # If user answers with "none"
                        if(sugar == "none"):
                            # Adjust stored answer for later
                            sugar = "no"
                            legit_answer = True # Exit loop
                            break
                        
                        # If sugar isn't an avaliable option
                        if(sugar not in LEVELS):
                            result = "Sorry, our sugar options are normal, less, half, "
                            result += "slight, and none."
                            print(result)
                            # Prompts for another attempt
                            sugar = input('You:\t')
                            sugar = prepare_text(sugar)
                            
                        # If sugar is an avaliable option
                        if(sugar in LEVELS):
                            legit_answer = True # Exit loop
                            
                    # If answer is legitimate
                    if(legit_answer):
                        
                        # Asks for ice levels
                        result = "And ice?"
                        print(result)
                        # Takes ice level from keyboard
                        ice = input('You\t')
                        ice = prepare_text(ice)
                        
                        # Checks if answer is legitimate
                        legit_answer = False
                        while(legit_answer == False):
                            
                            # If user ends conversation
                            if end_chat(ice):
                                print("Bye! Thanks for coming")
                                chat = False
                                break
                                
                            # If user answers with "none"
                            if(ice == "none"):
                                # Adjust stored answer for later
                                ice = "no"
                                legit_answer = True # Exit loop
                                break
                            
                            # If ice isn't an avaliable option
                            if(ice not in ICE):
                                print("Sorry, our ice options are normal, half, and none.")
                                # Prompts for another attempt
                                ice = input('You:\t')
                                ice = prepare_text(ice)
                                
                            # If ice is an avaliable option
                            if(ice in ICE):
                                legit_answer = True # Exit loop
                                
                        # If answer is legitimate
                        if(legit_answer):
                            
                            # Returns entire order as confirmation
                            result="Thank you, order confirmed! You ordered a " + size + " "
                            result+=drink_type + " with " + toppings + ", " + sugar + " sugar"
                            result+=", and " + ice + " ice. Your order will be ready shortly."
                            print(result)
                            
                            chat = False # Exit loop
main()

pass
