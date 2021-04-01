# Calculate average points per game for an NBA played if a game is 48 minutes and the
# function is provided with point scored in a game (ppg) and the number of minutes played in that game (mpg)
def nba_extrap(ppg, mpg):
    ppg = round((48 / mpg) * ppg, 1)
    return ppg

# function to take the numerical position of a month and return the quarter of the year it falls into. For example: month 2 (February) returns 1


def quarter_of(month):
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    else:
        return 4

# function to take a word and return a new string which consists of ')' if the letter appears more than once in the string and '(' if it only appears once


def duplicate_encode(word):
    new_word = []
    for letter in word.lower():
        if word.lower().count(letter) > 1:
            new_word.append(')')
        else:
            new_word.append('(')
    return "".join(new_word)

# function to add the to smallest numbers of a given array


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

# function to return number of sheep (True values in an array)


def count_sheep(sheep):
    num_sheep = 0
    for each in sheep:
        if each == True:
            num_sheep += 1
        else:
            pass
    return num_sheep

# function to return summation of any number


def summation(num):
    total = 0
    while num > 0:
        total += num
        num -= 1
    return total

# function to check directions relating to complex backstory


def is_valid_walk(walk):
    if len(walk) == 10 and walk.count('s') == walk.count('n') and walk.count('e') == walk.count('w'):
        return True
    else:
        return False

# function to check if array2 containts the squares of array1


def comp(array1, array2):
    try:
        return sorted(i ** 2 for i in array1) == sorted(array2)
    except:
        return False
