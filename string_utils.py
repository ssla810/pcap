import math


def halve_string(input_string):
    middle = math.ceil(len(input_string) / 2)
    return (input_string[:middle], input_string[middle:])