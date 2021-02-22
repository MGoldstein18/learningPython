# Project 1

# Import libraries
import pandas as pd
import numpy as np
import scipy.stats as scipy

# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')

#inspect data
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