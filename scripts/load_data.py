import pandas as pd
from ucimlrepo import fetch_ucirepo

# Fetch dataset
print("Fetching the German Credit Dataset...")
statlog_german_credit_data = fetch_ucirepo(id=144)

# Extract features and targets
X = statlog_german_credit_data.data.features
y = statlog_german_credit_data.data.targets

# Combine features and targets into one dataframe
df = pd.concat([X, y], axis=1)

# Save the dataset to the 'data' folder
df.to_csv(r'..\data\german_credit_data.csv', index=False)

print("Data saved to 'data\german_credit_data.csv'")
