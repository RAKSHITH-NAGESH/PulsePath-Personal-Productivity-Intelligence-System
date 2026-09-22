import pandas as pd

df = pd.read_csv("data.csv")

print("Original Data:")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing numeric values with median
numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Fill missing text values
text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = df[column].fillna("Unknown")

print("\nCleaned Data:")
print(df)

df.to_csv("cleaned_data.csv", index=False)
