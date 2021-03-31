# Calculate average points per game for an NBA played if a game is 48 minutes and the
# function is provided with point scored in a game (ppg) and the number of minutes played in that game (mpg)
def nba_extrap(ppg, mpg):
    ppg = round((48 / mpg) * ppg, 1)
    return ppg

