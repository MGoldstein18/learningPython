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
