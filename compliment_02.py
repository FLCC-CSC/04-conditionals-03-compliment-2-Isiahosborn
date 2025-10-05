# FILE NAME - compliment_02.py

# NAME: isiah osborn
# DATE: 2025-10-05
# BRIEF DESCRIPTION:
#   Read a single line of input. If it's exactly "yes" (lowercase),
#   print a compliment. Otherwise print "No compliment for you!"
#   Always print "Thank you for playing." afterward.

########## AUTOGRADER VERSION ##########

def main():
    reply = input().strip().lower()  
    if reply == "yes":
        print("You have wonderful eyes.")
    else:
        print("No compliment for you!")
    print("Thank you for playing.")

if __name__ == "__main__":
    main()

########### END YER CODE ABOVE THIS LINE ###########


########################################
#          SAMPLE OUTPUT
########################################

'''
Would you like a compliment? yes
You have wonderful eyes.
Thank you for playing.
'''

'''
Would you like a compliment? Yes
No compliment for you!
Thank you for playing.
'''

'''
Would you like a compliment? y
No compliment for you!
Thank you for playing.
'''

'''
Would you like a compliment? no
No compliment for you!
Thank you for playing.
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Did you struggle with this lab (YES/NO)?
YES


'''
