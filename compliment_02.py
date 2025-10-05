# FILE NAME - compliment_02.py

# NAME: isiah osborn
# DATE: 2025-10-05
# BRIEF DESCRIPTION:
#   Prompt the user for a compliment. If the input is exactly "yes"
#   (lowercase), print a compliment. Otherwise print "No compliment for you!"
#   Always print "Thank you for playing." afterward.

# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    reply = input("Would you like a compliment? ")  # Prompt for user
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
