# Two Way ANOVA using Python without replication


import pandas as pd
import scipy.stats as stats 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Generate sample data
two_percent_discount = [16,14,11,10,9]
one_percent_discount = [23,21,16,15,10]
no_discount = [21,16,18,14,11]
df = pd.DataFrame({'2% Discount': two_percent_discount, '1% Discount': one_percent_discount, 'No Discount': no_discount}, index=['50 USD', '100 USD', '150 USD', '200 USD', '250 USD'])
df_oryginal = df.copy()
df['Mean'] = df.mean(axis=1)
print(df)
# calculation of two way ANOVA
anova_results = stats.f_oneway(df['2% Discount'], df['1% Discount'], df['No Discount'])
print("F-statistic:", anova_results.statistic)
print("P-value:", anova_results.pvalue)
# Visualization using boxplot
#sns.boxplot(data=df)
#plt.title('Invoice Payment Times by Discount Plan')
#plt.ylabel('Payment Time (days)')   
#plt.show()
# Interpretation
alpha = 0.05
if anova_results.pvalue < alpha:
    print("Reject the null hypothesis: There is a significant difference in average payment times among the groups.")
else:
    print("Fail to reject the null hypothesis: No significant difference in average payment times among the groups.")
# manual calculation of two way ANOVA
mean_2_percent = np.mean(two_percent_discount)
mean_1_percent = np.mean(one_percent_discount)
mean_no_discount = np.mean(no_discount)
overall_mean = np.mean(two_percent_discount + one_percent_discount + no_discount)
print(f"Mean of 2% Discount Group: {mean_2_percent}")
print(f"Mean of 1% Discount Group: {mean_1_percent}")
print(f"Mean of No Discount Group: {mean_no_discount}")
print(f"Overall Mean: {overall_mean}")
# Degrees of freedom
df_between = 3 - 1  # number of groups - 1
df_within = 15 - 3  # total number of observations - number of groups
print(f"Degrees of Freedom Between Groups: {df_between}")
print(f"Degrees of Freedom Within Groups: {df_within}")
# F value and p-value calculation
# two way ANOVA using scipy.stats
f_value, p_value = stats.f_oneway(two_percent_discount, one_percent_discount, no_discount)
print(f"F-value: {f_value}")
print(f"P-value: {p_value}")
# Critical value
critical_value = stats.f.ppf(0.95, df_between, df_within)
print(f"Critical Value at alpha=0.05: {critical_value}")
if f_value > critical_value:
    print("Reject the null hypothesis: There is a significant difference in average payment times among the groups.")
else:
    print("Fail to reject the null hypothesis: No significant difference in average payment times among the groups.")

# add column for average payment time
df['Mean'] = df.mean(axis=1)
# overall mean for each column and add it to the dataframe
mean_2_percent = np.mean(two_percent_discount)
mean_1_percent = np.mean(one_percent_discount)
mean_no_discount = np.mean(no_discount)
# multiply sum of squares by number of observations
no_of_blocks = 3
no_of_observations = 5 # in each column
df.loc['Overall Mean'] = [mean_2_percent, mean_1_percent, mean_no_discount, np.mean([mean_2_percent, mean_1_percent, mean_no_discount])]
print(df)
# calculate sum of squares in each row for mean in columns
df['Sum of Squares'] = df[['2% Discount', '1% Discount', 'No Discount']].apply(lambda row: np.sum((row.mean() - overall_mean)**2), axis=1)
print(df)
# calculate sum of sum of squares
total_sum_of_squares = df['Sum of Squares'].sum()
print(f"Total Sum of Squares: {total_sum_of_squares}")
# sum of square groups
ssg = ((mean_2_percent - overall_mean)**2 + (mean_1_percent - overall_mean)**2 + (mean_no_discount - overall_mean)**2)* no_of_observations
print(f"Sum of Squares Between Groups (SSG): {ssg}")
# sum of squares blocks
ssb = ((df.loc['50 USD','Mean'] - overall_mean)**2 + (df.loc['100 USD','Mean'] - overall_mean)**2 + (df.loc['150 USD','Mean'] - overall_mean)**2 + (df.loc['200 USD','Mean'] - overall_mean)**2 + (df.loc['250 USD','Mean'] - overall_mean)**2)* no_of_blocks
print(f"Sum of Squares Between Blocks (SSB): {ssb}")
# sum of squares total
sst = np.sum((df_oryginal.values - overall_mean)**2)
print(f"Sum of Squares Total (SST): {sst}")
# sum of squares within groups
sse = sst - ssg - ssb
print(f"Sum of Squares Within Groups (SSE): {sse}")
# degrees of freedom
df_between_groups = 3 - 1  # number of groups - 1
df_between_blocks = 5 - 1  # number of blocks - 1
df_within = (3 - 1) * (5 - 1)  #
print(f"Degrees of Freedom Between Groups: {df_between_groups}")
print(f"Degrees of Freedom Between Blocks: {df_between_blocks}")
# calculate mean squares
msg = ssg / df_between_groups
msb = ssb / df_between_blocks
mse = sse / df_within   
print(f"Mean Square Between Groups (MSG): {msg}")
print(f"Mean Square Between Blocks (MSB): {msb}")
# F ratios
f_ratio_groups = msg / mse
print(f"F-ratio for Groups: {f_ratio_groups}")
f_ratio_blocks = msb / mse
print(f"F-ratio for Blocks: {f_ratio_blocks}")  
# Critical values
critical_value_groups = stats.f.ppf(0.95, df_between_groups, df_within)
print(f"Critical Value for Groups at alpha=0.05: {critical_value_groups}")
critical_value_blocks = stats.f.ppf(0.95, df_between_blocks, df_within)
print(f"Critical Value for Blocks at alpha=0.05: {critical_value_blocks}")








