import pandas as pd
import numpy as np
import re

# Load dataset
df = pd.read_csv("Luxury_Housing_Bangalore.csv")

# Clean Unit_Size_Sqft
if "Unit_Size_Sqft" in df.columns:
    df["Unit_Size_Sqft"] = df["Unit_Size_Sqft"].fillna("").astype(str)

    df["Unit_Size_Sqft"] = df["Unit_Size_Sqft"].apply(
        lambda x: re.sub(r"[^0-9.]", "", str(x))
    )

    df["Unit_Size_Sqft"] = pd.to_numeric(
        df["Unit_Size_Sqft"],
        errors="coerce"
    )

    df["Unit_Size_Sqft"] = df["Unit_Size_Sqft"].fillna(
        df["Unit_Size_Sqft"].median()
    )

# Clean Ticket_Price_Cr
if "Ticket_Price_Cr" in df.columns:
    df["Ticket_Price_Cr"] = df["Ticket_Price_Cr"].fillna("").astype(str)

    df["Ticket_Price_Cr"] = df["Ticket_Price_Cr"].apply(
        lambda x: re.sub(r"[^0-9.]", "", str(x))
    )

    df["Ticket_Price_Cr"] = pd.to_numeric(
        df["Ticket_Price_Cr"],
        errors="coerce"
    )

    df["Ticket_Price_Cr"] = df["Ticket_Price_Cr"].fillna(
        df["Ticket_Price_Cr"].median()
    )

# Clean numeric columns
numeric_columns = [
    "Connectivity_Score",
    "Amenity_Score",
    "Locality_Infra_Score",
    "Avg_Traffic_Time_Min"
]

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned file
df.to_csv(
    "cleaned_Luxury_Housing_Bangalore.csv",
    index=False
)

print("Data Cleaning Completed Successfully!")
