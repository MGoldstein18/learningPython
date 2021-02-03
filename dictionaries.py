# working with given dictionary to create, modify and display a new dictionary

# create an empty dictionary
medical_costs = {}

# populate the dictionary
medical_costs.update({"Marian": 6607.0, "Vinay": 3225.0,
                      "Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})

# update a value in the dictionary
medical_costs["Vinay"] = 3325.0

# get the average of all insurance costs in the dictionary
total_cost = 0

for each in medical_costs.values():
    total_cost += each

average_cost = total_cost / len(medical_costs)
print("Average Insurance Cost: " + str(average_cost))

# create a new dictionary from 2 lists
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

zipped_ages = zip(names, ages)

names_to_ages = {key: value for key, value in zipped_ages}

# create a new dictionary and populate it
medical_records = {}

medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1,
                             "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}

medical_records.update({
    "Vinay": {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0, },
    "Connie": {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0},
    "Isaac": {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0},
    "Valentina": {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}
})

# remove a key value pair from the dictionary
medical_records.pop("Vinay")

# print all the data in the dictionary with an appropriate sentence
for key, value in medical_records.items():
    print("{Name} is a {Age} year old {Sex} {Smoker} with a BMI of {BMI} and insurance cost of a {Insurance_cost}".format(
        Name=key, Age=value["Age"], Sex=value["Sex"], Smoker=value["Smoker"], BMI=value["BMI"], Insurance_cost=value["Insurance_cost"]))
