# Analysis of Variance (ANOVA) using Python
import pandas as pd
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Generate sample data
GroupA = [37,60,52,43,40,52,55,39,39,23]
GroupB = [62,27,69,64,43,54,44,31,49,57]
GroupC = [50,63,58,54,49,52,53,43,65,43]
# calculate averages
mean_A = np.mean(GroupA)
mean_B = np.mean(GroupB)        
mean_C = np.mean(GroupC)
overall_mean = np.mean(GroupA + GroupB + GroupC)
print(f"Mean of Group A: {mean_A}")
print(f"Mean of Group B: {mean_B}")
print(f"Mean of Group C: {mean_C}")
print(f"Overall Mean: {overall_mean}")
# degres of freedom
df_between = 3 - 1  # number of groups - 1
df_within = 30 - 3  # total number of observations - number of groups 
print(f"Degrees of Freedom Between Groups: {df_between}")
print(f"Degrees of Freedom Within Groups: {df_within}")
# F value and p-value calculation
f_value, p_value = stats.f_oneway(GroupA, GroupB, GroupC)
print(f"F-value: {f_value}")
print(f"P-value: {p_value}")
# Visualization using boxplot
data = {'Group A': GroupA, 'Group B': GroupB, 'Group C': GroupC}
df = pd.DataFrame(data)
critical_value = stats.f.ppf(0.95, df_between, df_within)
print(f"Critical Value at alpha=0.05: {critical_value}")
