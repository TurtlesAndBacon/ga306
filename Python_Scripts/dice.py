import random

def get_sides():
    """#user enters # of sides on die"""
    num_sides = int(input("Enter the number of sides"))
    return num_sides

def get_num_die():
    """#user enters # of die being cast"""
    num_die = int(input("Enter the number of dice being rolled"))
    return num_die

def get_roll(num_sides, num_die):
    """#program returns a 'roll' value"""
    roll_range = num_sides * num_die
    roll_result = random.randint(1, roll_range)
    return roll_result

def main():
    num_sides = get_sides()
    num_die = get_num_die()
    roll_result = get_roll(num_sides, num_die)
    print(roll_result)

main()
