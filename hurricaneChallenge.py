# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille',
         'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September',
          'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977,
         1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160,
                       175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], [
    'Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M',
           'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11,
          2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def update_damages():
    updated_damages = []
    for amount in damages:
        if amount == "Damages not recorded":
            updated_damages.append(amount)
        else:
            updated_damages.append(
                float(amount[0:-1]) * conversion[amount[-1]])
    return updated_damages

damages = update_damages()


# Create a Table
def hurricane_dictionary():
    detail_dictionary = {}
    for i in range(34):
        details = {'Name': names[i], 'Month': months[i], "Year": years[i], 'Max Sustained Winds': max_sustained_winds[i],
                   'Areas Affected': areas_affected[i], 'Damage': damages[i], 'Deaths': deaths[i]}
        detail_dictionary.update({names[i]: details})
    return(detail_dictionary)

hurricanes = hurricane_dictionary()


# Organizing hurricanes by Year
def organized_by_year():
    years = {}
    for key, value in hurricanes.items():
        current_year = years.get(value["Year"])
        if not current_year:
            years.update({value['Year']: value})
        else:
            details = [years[value['Year']], value]
            years[value["Year"]] = details
    return years

years = organized_by_year()


# Counting Damaged Areas
def damaged_areas():
    areas = {}
    for key, value in hurricanes.items():
        area_array = value['Areas Affected']
        for area in area_array:
            current_area = areas.get(area)
            if not current_area:
                areas[area] = 1
            else:
                new_count = areas[area] + 1
                areas[area] = new_count
    return areas

affected_areas = damaged_areas()


# find most frequently affected area and the number of hurricanes involved in
def worst_hit():
    area_list = affected_areas.keys()
    num_times_list = affected_areas.values()
    zipped = list(zip(area_list, num_times_list))
    worst_place = zipped[0][0]
    worst_times = zipped[0][1]
    for key, value in zipped:
        if value > worst_times:
            worst_place = key
            worst_times = value
    return (worst_place + " has been hit the most times - " + str(worst_times))

worst_hit_location = worst_hit()

# Function to create list of hurricane names and number of deaths
def create_death_list():
    deaths_list = []
    for key, value in hurricanes.items():
        current_hurricane = []
        current_hurricane.append(key)
        current_hurricane.append(value['Deaths'])
        deaths_list.append(current_hurricane)
    return deaths_list

# Calculating the Deadliest Hurricane
def most_deaths():
    deaths_list = create_death_list()
    most_deaths_hurricane = deaths_list[0][0]
    most_deaths = deaths_list[0][1]
    for hurricane, number in deaths_list:
        if number > most_deaths:
            most_deaths = number
            most_deaths_hurricane = hurricane
    return ("Hurricane " + most_deaths_hurricane + " caused the most deaths - " + str(most_deaths))

highest_mortality = most_deaths()


# Rating Hurricanes by Mortality
def mortality_rating():
    zero = []
    one = []
    two = []
    three = []
    four = []
    five = []
    for value in hurricanes.values():
        if value['Deaths'] == 0:
            zero.append(value)
        elif value['Deaths'] <= 100:
            one.append(value)
        elif value['Deaths'] <= 500:
            two.append(value)
        elif value['Deaths'] <= 1000:
            three.append(value)
        elif value['Deaths'] <= 10000:
            four.append(value)
        else:
            five.append(value)
    ratings = {
        0: zero,
        1: one,
        2: two,
        3: three,
        4: four,
        5: five
    }
    return ratings

mortality_ratings = mortality_rating()


# Calculating Hurricane Maximum Damage
def create_damage_list():
    damage_list = []
    for key, value in hurricanes.items():
        if value['Damage'] == "Damages not recorded":
            continue
        current_hurricane = []
        current_hurricane.append(key)
        current_hurricane.append(value['Damage'])
        damage_list.append(current_hurricane)
    return damage_list

# Function to create list of hurricane names and amount of damage
def most_damage():
    damage_list = create_damage_list()
    most_damage_hurricane = damage_list[0][0]
    most_damage = damage_list[0][1]
    for hurricane, number in damage_list:
        if number > most_damage:
            most_damage = number
            most_damage_hurricane = hurricane
    return ("Hurricane " + most_damage_hurricane + " caused the most damage - " + str(most_damage))

greatest_damage = most_damage()


# Rating Hurricanes by Damage
def damage_rating():
    zero = []
    one = []
    two = []
    three = []
    four = []
    five = []
    for value in hurricanes.values():
        if value['Damage'] == 'Damages not recorded':
            continue
        elif value['Damage'] == 0:
            zero.append(value)
        elif float(value['Damage']) <= 100000000:
            one.append(value)
        elif value['Damage'] <= 1000000000:
            two.append(value)
        elif value['Damage'] <= 10000000000:
            three.append(value)
        elif value['Damage'] <= 50000000000:
            four.append(value)
        else:
            five.append(value)
    ratings = {
        0: zero,
        1: one,
        2: two,
        3: three,
        4: four,
        5: five
    }
    return ratings

damages_rating = damage_rating()
