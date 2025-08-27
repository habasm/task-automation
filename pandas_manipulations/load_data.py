import pandas as pd
import matplotlib.pyplot as plt

# 📂 Step 1 — Load Data
df = pd.read_csv("../books.csv")

# 📂 Step 2 — Explore Data
print("*"*100)
print("The shape is: ",  df.shape)      # rows & columns
print("The column is:", df.columns)    # column names
print("Data types Info: ", df.info())     # data types
print("Quick statistics: ", df.describe()) # quick statistics
print("*"*100)

# 📂  Step 3 — Cleaning Data
df["Price"] = df["Price"].str.replace("Â£", "").astype(float)

# 📂 Step 4 — Selecting Data

# Prints the df types=> column types
print("*"*100)
print(df.dtypes)

# Show a first 5 rows
print(df.head())

# Select the first 5 titles
print(df["Title"].head())

# Select rows 0–2
print(df.iloc[0:3])


# Filter books cheaper than £20
cheap_books = df[df["Price"] < 20]
print(cheap_books)
print("*"*100)

# 📂 Step 5 — Aggregations
print("*"*100)
print("Average Price:", df["Price"].mean())
print("Max Price:", df["Price"].max())
print("Min Price:", df["Price"].min())
print("*"*100)

# 📂 Step 6 — Sorting & Grouping
# Top 5 most expensive books
print(df.sort_values(by="Price", ascending=False).head())

# Count books in price ranges
df["PriceRange"] = pd.cut(df["Price"], bins=[0,20,40,60], labels=["Low","Medium","High"])
print(df["PriceRange"].value_counts())

# 📂 Step 7 — Save Results
df.to_csv("books_cleaned.csv", index=False)
print("✅ Saved cleaned data to books_cleaned.csv")

# 📊  Step 8 — Visualize
df["Price"].plot(kind="hist", bins=10, title="Book Price Distribution")
plt.xlabel("Price (£)")
plt.show()