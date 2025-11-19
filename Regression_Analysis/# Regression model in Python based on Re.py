# Regression model in Python based on Regression Analysis/ Data Analytics in Regression - more than one independent variable
import pandas as pd
import scipy.stats as stats
import numpy as np
import statsmodels.api as sm
# Sample data: Replace this with your actual data from excel
file_path = r'c:\Users\Dani\Desktop\Udemy\Correlation-RegressionAnalysis - More ThanOneVariable.xlsx'
data= pd.read_excel(file_path, sheet_name='Sheet1')
# Perform regression analysis
X = data[['SAT_score', 'Social Support']]  # Independent variables
y = data['College_GPA']  # Dependent variable
X = sm.add_constant(X)  # Adds a constant term to the predictors
model = sm.OLS(y, X).fit()  # Fit the regression model
# Print the regression results
print(model.summary())

