# Regression model in Python based on Regression Analysis/ Data Analytics in Regression - course used SPSS
import pandas as pd
import scipy.stats as stats 
import numpy as np
# Sample data: Replace this with your actual data from execel
file_path = r'c:\Users\Dani\Desktop\Udemy\Correlation-RegressionAnalysis.xlsx'
data = pd.read_excel(file_path, sheet_name='Sheet1')
# Check column names
print("Column names:", data.columns.tolist())
# Perform regression analysis
slope, intercept, r_value, p_value, std_err = stats.linregress(data['Hours_media'], data['College_GPA'])
# Print the regression results
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")    
print(f"R-squared: {r_value**2}")
print(f"P-value: {p_value}")
print(f"Standard Error: {std_err}")
# Predict College GPA based on Hours of Media Consumption
def predict_gpa(hours):
    return intercept + slope * hours    
predicted_gpa = predict_gpa(20)  # Example: Predict GPA for 20 hours of media consumption
print(f"Predicted College GPA for 20 hours of media consumption: {predicted_gpa}")
# Visualization (optional)
import matplotlib.pyplot as plt
plt.scatter(data['Hours_media'], data['College_GPA'], color='blue', label='Data points')
plt.plot(data['Hours_media'], intercept + slope * data['Hours_media'], color='red', label='Regression line')
plt.xlabel('Hours of Media Consumption per Week')   
plt.ylabel('College GPA')
plt.title('Regression Analysis: Media Consumption vs College GPA')
plt.legend()
plt.show()
