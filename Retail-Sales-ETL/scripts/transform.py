import pandas as pd

# Load dataset
sales = pd.read_csv("./data/Superstore.csv", encoding="latin1")


# Remove null values
sales.dropna(inplace=True)

# Remove duplicates
sales.drop_duplicates(inplace=True)

# Revenue column
sales["Revenue"] = sales["Sales"]

# Save cleaned data
sales.to_csv("output/cleaned_sales.csv", index=False)

print("Data transformed successfully!")

print(sales.head())