python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'Traffic Accident-v3.0 (values) Abu Dhabi 2023.xlsx'
data = pd.read_excel(file_path)

# Display first few rows of the dataset
data.head()

# Data Preprocessing
# Convert date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Analyze accident frequency by month
data['Month'] = data['Date'].dt.month
monthly_accidents = data.groupby('Month').size()

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x=monthly_accidents.index, y=monthly_accidents.values)
plt.title('Monthly Traffic Accidents in Abu Dhabi 2023')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.show()
