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
