# Question
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.

import math


def compute_distance(commands):

    current_coords = [0, 0]

    command_list = commands.split("\n")
    command_list = [tuple(command.split(" ")) for command in command_list]
    command_list = [(command, int(distance))
                    for command, distance in command_list]

    for direction, distance in command_list:
        if direction == "UP":
            current_coords[1] += distance
        elif direction == "DOWN":
            current_coords[1] -= distance
        elif direction == "RIGHT":
            current_coords[0] += distance
        elif direction == "LEFT":
            current_coords[0] -= distance
        else:
            return "Error in Directions"

    distance = math.sqrt(current_coords[0]**2 + current_coords[1]**2)
    return round(distance, 2)


directions = "UP 100\nDOWN 3\nLEFT 3\nRIGHT 20"
print(
    f"Bleep Bleep BLOOOOP! Your robot is {compute_distance(directions)} away.")
