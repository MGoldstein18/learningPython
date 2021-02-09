import pandas as pd

# Task 1

# read in csv and print first few lines
user_visits = pd.read_csv('page_visits.csv')
print(user_visits.head())

# get and display number of visits per source
click_source = user_visits.groupby('utm_source').id.count().reset_index()
print(click_source)

# get and display number of visits per source per month
click_source_by_month = user_visits.groupby(
    ['utm_source', 'month']).id.count().reset_index()
print(click_source_by_month)

# display that as a pivot table
click_source_by_month_pivot = click_source_by_month.pivot(
    columns='month',
    index='utm_source',
    values='id'
).reset_index()

print(click_source_by_month_pivot)


# Task 2

# read in csv and display first few lines
ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

# get number of views per source
views_by_source = ad_clicks.groupby(
    'utm_source').user_id.count().reset_index()

# add a column to track whether or not an add was clicked on
ad_clicks['is_click'] = ~ad_clicks\
    .ad_click_timestamp.isnull()

# get number of add clicked on per source
clicks_by_source = ad_clicks.groupby(
    ['utm_source', 'is_click']).user_id.count().reset_index()

# display it as a pivot table
clicks_pivot = clicks_by_source.pivot(
    columns='is_click',
    index='utm_source',
    values='user_id'
)

# add to pivot table a column for percentage of clicks and then display the pivot table
clicks_pivot['percent_clicked'] = \
    (clicks_pivot[True] /
     (clicks_pivot[True] +
        clicks_pivot[False]) * 100)

print(clicks_pivot)

# get the number of of people who viewed each ad
number_shown_each_ad = ad_clicks.groupby(
    'experimental_group').user_id.count().reset_index()

# get aggregate of number of clicks per ad group
more_clicks_per_ad_type = ad_clicks.groupby(
    ['experimental_group', 'is_click']).user_id.count().reset_index()

# convert into pivot table
pivoted_clicks_per_type_of_ad = more_clicks_per_ad_type.pivot(
    columns='is_click',
    index='experimental_group',
    values='user_id'
).reset_index()

# add column for percentage of clicks and display the pivot table
pivoted_clicks_per_type_of_ad['click_percentage'] = (pivoted_clicks_per_type_of_ad[True] / (
    pivoted_clicks_per_type_of_ad[True] + pivoted_clicks_per_type_of_ad[False]) * 100)

print(pivoted_clicks_per_type_of_ad)

# compare clicks ad A and ad B per day by making tables of clicks per add per day and then making them into pivot tables and adding percentage column
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']


percent_by_day_A = a_clicks.groupby(
    ['day', 'is_click']).user_id.count().reset_index()
percent_by_day_B = b_clicks.groupby(
    ['day', 'is_click']).user_id.count().reset_index()

pivot_percent_by_day_A = percent_by_day_A.pivot(
    columns='is_click',
    index='day',
    values='user_id'
)

pivot_percent_by_day_A['percentage'] = (pivot_percent_by_day_A[True] / (
    pivot_percent_by_day_A[True] + pivot_percent_by_day_A[False]) * 100)

print(pivot_percent_by_day_A)

pivot_percent_by_day_B = percent_by_day_B.pivot(
    columns='is_click',
    index='day',
    values='user_id'
)

pivot_percent_by_day_B['percentage'] = (pivot_percent_by_day_B[True] / (
    pivot_percent_by_day_B[True] + pivot_percent_by_day_B[False]) * 100)

print(pivot_percent_by_day_B)
