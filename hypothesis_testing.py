import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import f_oneway
from scipy.stats import ttest_ind
import seaborn as sns
from scipy.stats import binom_test
import libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

chol_hd = yes_hd.chol
mean_chol_hd = np.mean(chol_hd)

tstat, pval = ttest_1samp(chol_hd, 240)
print(pval/2)

chol_no_hd = no_hd.chol
mean_chol_no_hd = np.mean(chol_no_hd)

tstat1, pval1 = ttest_1samp(chol_no_hd, 240)
print(pval1/2)

num_patients = len(heart)
print(num_patients)

num_highfbs_patients = np.sum(heart.fbs == 1)
print(num_highfbs_patients)

print(0.08 * num_patients)

pval = binom_test(num_highfbs_patients, num_patients, .08,
                  alternative='greater')
print(pval)


# project 2

# load data
heart = pd.read_csv('heart_disease.csv')

sns.boxplot(x=heart.heart_disease, y=heart.thalach)
plt.show()

thalach_hd = heart.thalach[heart.heart_disease == 'presence']
thalach_no_hd = heart.thalach[heart.heart_disease == 'absence']

mean_diff = np.mean(thalach_no_hd) - np.mean(thalach_hd)
print(mean_diff)

median_diff = np.median(thalach_no_hd) - np.median(thalach_hd)
print(median_diff)

tstat, pval = ttest_ind(thalach_hd, thalach_no_hd)
print(pval)

plt.clf()

sns.boxplot(x=heart.heart_disease, y=heart.age)
plt.show()

age_hd = heart.age[heart.heart_disease == 'presence']
age_no_hd = heart.age[heart.heart_disease == 'absence']

age_mean = np.mean(age_hd) - np.mean(age_no_hd)
age_median = np.median(age_hd) - np.median(age_no_hd)

print(age_mean, age_median)

tstat, pval = ttest_ind(age_hd, age_no_hd)
print(pval)

plt.clf()

sns.boxplot(x=heart.cp, y=heart.thalach)
plt.show()

thalach_typical = heart.thalach[heart.cp == 'typical angina']

thalach_asymptom = heart.thalach[heart.cp == 'asymptomatic']

thalach_nonangin = heart.thalach[heart.cp == 'non-anginal pain']

thalach_atypical = heart.thalach[heart.cp == 'atypical angina']

Fstat, pval = f_oneway(thalach_typical, thalach_asymptom,
                       thalach_nonangin, thalach_atypical)
print(pval)

result = pairwise_tukeyhsd(heart.thalach, heart.cp)
print(result)

Xtab = pd.crosstab(heart.cp, heart.heart_disease)
print(Xtab)

chi2, pval, dof, exp = chi2_contingency(Xtab)
print(pval)
