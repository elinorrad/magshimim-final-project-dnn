import pandas as pd

# Read the ALL_TABLE.csv file
file_path = "A:/FinalProjectMagshimim/ALL_TABLE.csv"
df_all_table = pd.read_csv(file_path)

# Keep only the first 3 characters of ICD10
df_all_table['icd10cm'] = df_all_table['icd10cm'].astype(str).str[:3]

# Update relevant ICD10 groups
complication_codes = {"H59", "I97", "J95", "K91", "N99", "G97", "M96", "D78", "H95", "L76", "E36"}

# List of relevant ITEMIDs (example - should be updated based on available data)
complication_itemids = {
    51265,
    51222,
    51221,
    51279,
    51250,
    51249,
    51248,
    51301,
    51277,
    50882,
    51006,
    50902,
    50912,
    50868,
    50971,
    50983,
    50931,
    50960,
    50893,
    50970
}

# Filter the table by ICD10
df_complications = df_all_table[df_all_table['icd10cm'].isin(complication_codes)]

# Keep only relevant columns
columns_to_keep_complications = ['SUBJECT_ID', 'icd10cm'] + [str(item) for item in complication_itemids]
df_complications = df_complications[columns_to_keep_complications]
df_complications.to_csv("A:/FinalProjectMagshimim/COMPLICATIONS_ALL_BY_ELINOR.csv", index=False)

# Function to print statistics
def print_statistics(df, name):
    print(f"\n{name}:")

    # Count occurrences of each ICD10
    icd_counts = df['icd10cm'].value_counts()
    print("Occurrences of each ICD10:")
    print(icd_counts)

    # Compute the top 20 ITEMIDs with the highest number of non-null values
    top_items = df.iloc[:, 2:].count().nlargest(20)
    print("\nTop 20 tests (ITEMID) with the highest number of non-null values:")
    print(top_items)

# Print statistics
print_statistics(df_complications, "COMPLICATIONS_ALL_BY_ELINOR")
