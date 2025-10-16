# Two-Sample T-Test
from scipy.stats import ttest_ind

# Data from two groups
group1 = [12, 14, 15, 16, 17, 18, 19]
group2 = [11, 13, 14, 15, 16, 17, 18]

# Perform t-test
t_stat, p_value = ttest_ind(group1, group2)
print("T-Statistic: ", t_stat)
print("P-Value: ", p_value)

# Interpretation 
alpha = 0.05
if p_value <= alpha:
    print("Reject the null hypothesis: significant difference")
else:
    print("Fail to Reject the null hypothesis: no significant difference")


# Additional Practice:
# A. Perform a z-test for a large sample sizes.
from scipy.stats import norm
import numpy as np

# Simulate large samples
np.random.seed(42)
group1 = np.random.normal(50, 10, 100)
group2 = np.random.normal(52, 10, 100)

# Z-test calculation
mean1, mean2 = group1.mean(), group2.mean()
std1, std2 = group1.std(ddof=1), group2.std(ddof=1)
n1, n2 = len(group1), len(group2)

# Pooled standard error
se = np.sqrt(std1**2/n1 + std2**2/n2)
z = (mean1 - mean2) / se

# Two-sided p-value
p_value = 2 * (1 - norm.cdf(abs(z)))

print("Z-Statistic:", z)
print("P-Value:", p_value)


# B. Use the Iris dataset to test if the mean sepal length differs between two species.
import pandas as pd
from scipy.stats import ttest_ind

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

setosa = df[df.species == "setosa"]["sepal_length"]
versicolor = df[df.species == "versicolor"]["sepal_length"]

t_stat, p_value = ttest_ind(setosa, versicolor, equal_var=False)  # Welch's t-test

print("T-Statistic:", t_stat)
print("P-Value:", p_value)
if p_value <= 0.05:
    print("Reject the null hypothesis: mean sepal length differs between species.")
else:
    print("Fail to reject the null hypothesis: no significant difference.")


# C. Perform hypothesis testing on proportions using the binomial distribution.
from statsmodels.stats.proportion import proportions_ztest

# Example: 50 successes in 100 trials vs. 60 in 120 trials
successes = np.array([50, 60])
samples = np.array([100, 120])

stat, pval = proportions_ztest(count=successes, nobs=samples, alternative='two-sided')

print("Z-Statistic:", stat)
print("P-Value:", pval)
if pval <= 0.05:
    print("Reject the null hypothesis: significant difference in proportions.")
else:
    print("Fail to reject the null hypothesis: no significant difference.")


