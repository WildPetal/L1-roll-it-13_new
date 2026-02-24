error = "please enter an integer more than / equal to 13"

while True:
    try:
        game_goal = int(input("please enter your goal : "))

        print(f"game goal: {game_goal}")

        if game_goal < 13:
            print(error)
        else:
            print(f"game goal: {game_goal}")

    except ValueError:
        print(error)
