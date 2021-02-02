# two function working with string in python to generate a username and password from the user's first and last names
def username_generator(first_name, last_name):
    first = ""
    last = ""
    if len(first_name) <= 3:
        first = first_name
    if len(last_name) <= 4:
        last = last_name
    else:
        first = first_name[:3]
        last = last_name[:4]
    return first + last


def password_generator(username):
    password = ""
    for i in range(len(username)):
        password += username[i - 1]
    return password


# a function which does a series of steps calling various string methods to manipulate the string "list" of poems provided
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# first split the poems on commas to that each poem's info is one item in a list
highlighted_poems_list = highlighted_poems.split(',')

# then strip away any excess whitespace
highlighted_poems_stripped = []

for each in highlighted_poems_list:
    highlighted_poems_stripped.append(each.strip())

# then create sublists of each poems details in the bigger list by splitting them on colons
highlighted_poems_details = []

for each in highlighted_poems_stripped:
    highlighted_poems_details.append(each.split(':'))

# create lists for titles, poets and dates and then populate them using a for loop through the list of stripped and split data
titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
    titles.append(poem[0])
    poets.append(poem[1])
    dates.append(poem[2])

# print details for each poem in appropriate sentence
for i in range(len(titles)):
    print("The poem {title} was published by {poet} in {date}.".format(
        title=titles[i], poet=poets[i], date=dates[i]))
