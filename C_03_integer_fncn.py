
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

#main routine starts here
game_goal = int_check()
print(game_goal)