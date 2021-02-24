from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS",
         "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers = [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

plt.bar(range(len(games)), viewers, color='green')
plt.title('Views per Game')
plt.xlabel('Games')
plt.ylabel('Views')
ax = plt.subplot()
ax.set_xticks(range(len(games)))
ax.set_xticklabels(games, rotation=30)
plt.legend(['Twitch'])
plt.show()

plt.clf()


labels = ["US", "DE", "CA", "N/A", "GB", "TR",
          "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue',
          'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']

explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

plt.pie(countries, explode=explode, colors=colors, shadow=True,
        startangle=345, autopct='%1.0f%%', pctdistance=1.15)

plt.title('League of Legends Viewers\' Whereabouts')
plt.legend(labels)
plt.show()
plt.clf()


hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5,
                48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

y_upper = [i * 1.15 for i in viewers_hour]
y_lower = [i * 0.85 for i in viewers_hour]

plt.fill_between(hour, y_lower, y_upper, alpha=0.2)

plt.plot(hour, viewers_hour, marker='o')
plt.title('Views per Hour')
plt.xlabel('Hour')
plt.ylabel('Views')
ax = plt.subplot()
ax.set_xticks(hour)
ax.set_xticklabels(hour)
plt.legend(['2015-01-01'])
plt.show()
