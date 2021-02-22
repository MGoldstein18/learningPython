# Project 1

# Import libraries
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import codecademylib3
import pandas as pd
import numpy as np
import scipy.stats as scipy

# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')

# inspect data
print(lifespans.head())

vein_pack_lifespans = lifespans.lifespan[lifespans.pack == 'vein']
vein_lifespan_mean = np.mean(vein_pack_lifespans)
print(vein_lifespan_mean)

# 1 sided test
tstat, pval = scipy.ttest_1samp(vein_pack_lifespans, 73)
print(pval)

artery_pack_lifespans = lifespans.lifespan[lifespans.pack == 'artery']

artery_lifespan_mean = np.mean(artery_pack_lifespans)
print(artery_lifespan_mean)

# 2 sided test
tstat, pval = scipy.ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print(pval)

print(iron.head())

Xtab = pd.crosstab(iron.pack, iron.iron)
print(Xtab)

# chi2 test
chi2, pval, dof, exp = scipy.chi2_contingency(Xtab)
print(pval)


# Project 2
# Import libraries

# Import data
dogs = pd.read_csv('dog_data.csv')
print(dogs.head())

# Subset to just whippets, terriers, and pitbulls
dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]

# Subset to just poodles and shihtzus
dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]

whippet_rescue = dogs.is_rescue[dogs.breed == 'whippet']
num_whippet_rescues = np.sum(whippet_rescue)
print(num_whippet_rescues)

num_whippets = len(whippet_rescue)
print(num_whippets)

pval = scipy.binom_test(num_whippet_rescues, num_whippets, 0.08)
print(pval)

wt_whippets = dogs.weight[dogs.breed == 'whippet']
wt_terriers = dogs.weight[dogs.breed == 'terrier']
wt_pitbulls = dogs.weight[dogs.breed == 'pitbull']

Fstat, pval = scipy.f_oneway(wt_whippets, wt_terriers, wt_pitbulls)
print(pval)

output = pairwise_tukeyhsd(dogs_wtp.weight, dogs_wtp.breed)
print(output)

Xtab = pd.crosstab(dogs_ps.color, dogs_ps.breed)
print(Xtab)

chi2, pval, dof, exp = scipy.chi2_contingency(Xtab)
print(pval)


# Project 3

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('clicks.csv')
print(abdata.head())

Xtab = pd.crosstab(abdata.group, abdata.is_purchase)
print(Xtab)

chi2, pval, dof, exp = scipy.chi2_contingency(Xtab)
print(pval)

num_visits = len(abdata)

num_sales_needed_099 = 1000 / 0.99

p_sales_needed_099 = num_sales_needed_099 / num_visits

num_sales_needed_199 = 1000 / 1.99

p_sales_needed_199 = num_sales_needed_199 / num_visits

num_sales_needed_499 = 1000 / 4.99

p_sales_needed_499 = num_sales_needed_499 / num_visits

print(p_sales_needed_099, p_sales_needed_199, p_sales_needed_499)

samp_size_099 = np.sum(abdata.group == 'A')
sales_099 = np.sum((abdata.group == 'A') & (abdata.is_purchase == 'Yes'))

samp_size_199 = np.sum(abdata.group == 'B')
sales_199 = np.sum((abdata.group == 'B') & (abdata.is_purchase == 'Yes'))

samp_size_499 = np.sum(abdata.group == 'C')
sales_499 = np.sum((abdata.group == 'C') & (abdata.is_purchase == 'Yes'))


pvalueA = scipy.binom_test(sales_099, samp_size_099,
                           p_sales_needed_099, alternative='greater')

pvalueB = scipy.binom_test(sales_199, samp_size_199,
                           p_sales_needed_199, alternative='greater')

pvalueC = scipy.binom_test(sales_499, samp_size_499,
                           p_sales_needed_499, alternative='greater')

print(pvalueA, pvalueB, pvalueC)
