import pandas as pd

# Task 1

inventory = pd.read_csv('inventory.csv')
staten_island = inventory.head(10)


product_request = staten_island['product_description']

seed_request = inventory[(inventory.location == 'Brooklyn') & (
    inventory.product_type == 'seeds')]

inventory['in_stock'] = inventory.apply(
    lambda row: True if row['quantity'] > 0 else False, axis=1)

inventory['total_value'] = inventory.apply(
    lambda row: row.price * row.quantity, axis=1)


combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)


inventory.full_description = inventory.apply(combine_lambda, axis=1)


# Task 2

orders = pd.read_csv('shoefly.csv')
print(orders.head())

emails = orders.email

frances_palmer = orders[(orders.first_name == 'Frances')
                        & (orders.last_name == 'Palmer')]

comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]


# Task 3
orders = pd.read_csv('shoefly.csv')

print(orders.head())


def source(
    row): return 'vegan' if row['shoe_material'] != 'leather' else 'animal'


orders['shoe_source'] = orders.apply(source, axis=1)


def greeting(row): return 'Dear Mr. ' + \
    row['last_name'] if row['gender'] == 'male' else 'Dear Ms. ' + row['last_name']


orders['salutation'] = orders.apply(greeting, axis=1)
