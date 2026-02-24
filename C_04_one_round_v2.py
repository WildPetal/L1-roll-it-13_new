import random

def initial_points(which_player):
    """Roll dice twice and return total / if double points apply"""


    double = "no"

    # Roll the dice for the user and more and note if they got a double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(f"{which_player} - roll 1: {roll_one} | roll 2: {roll_two} | Points: {total}")

    return total, double

# Intialise rounds points
user_points = 0
comp_points = 0


# roll the dice for the computer
comp_one = random.randint(1, 6)
comp_two = random.randint(1, 6)


# Update the dice for the computer points
user_points = user_one + user_two
comp_points = comp_two + user_one

# Output the user / computer points
# Let the user  know   if they qualify for double points
print("\ninitial points")
print(f"User        - Roll 1: {user_one} \t| Roll 2: {user_two} \t| Points: {user_points}")
print(f"computer    - Roll 1: {comp_one} \t| Roll 2: {comp_two} \t| Points: {comp_points}")

# Let the user know if they qualify for double points
if double_user == "yes":
    print("Great news - if you win, you will earn double points!")