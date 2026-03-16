
# initialise list to hold game history
game_history = []

# get data (base component does this already, code below fore testing purposes)
user_score = 0
comp_score = 0
rounds_played = 0

while True:
    round_played = input("Round?")
    if rounds_played == "":
        break

    user_points = int(input("Points?"))
    comp_points = int(input("Computer Points?"))
    winner = input ("Who won ")
    user_score = int(input("User score: "))
    comp_score = int(input("Computer score: "))

    game_results = (f"round {rounds_played}: User points {user_points} | "
                    f"computer {comp_points}, {winner} wins"
                    f"({user_score} | {comp_score})"

    game_history.append(game_results)

    print("game history")



