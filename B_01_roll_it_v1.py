
#functions go there

def yes_no(question):

    """checks user response to a question is yes / no (y/n), returns 'yes' or 'no'"""

    while True:

        response = input(question).lower()

        #check the user says yes / no
        if  response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please say yes / no")


def instructions():
    """prints instructions"""

    print("""
*** Instructions ***  
      
roll the dice and try to win!     
    """)


def int_check():
    """Check users an integer more than / equal to 13"""

    error = "please enter an integer more than / equal to 13"

    while True:
        try:
            response = int(input("please enter your goal : "))

            print(f"game goal: {response}")

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine


want_instructions = yes_no("Do you want to see the instructions")
print(f"you chose {want_instructions}")

# display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
game_goal = int_check()
print(game_goal)



