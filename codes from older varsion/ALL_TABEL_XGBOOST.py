import pandas as pd

# Read the ALL_TABLE.csv file
file_path = "A:/FinalProjectMagshimim/ALL_TABLE.csv"
df_all_table = pd.read_csv(file_path)

# Keep only the first 3 characters of ICD10
df_all_table['icd10cm'] = df_all_table['icd10cm'].astype(str).str[:3]

# Define ICD10 categories
icd_categories = {
    "Intraoperative and Postoperative Complications": {"H59", "I97", "J95", "K91", "N99", "G97", "M96", "D78", "H95", "L76", "E36"},
    "Cardiovascular Diseases": {"I10", "I25", "I50", "T82", "I35", "I48", "I95"},
    #"Metabolic and Endocrine Diseases": {"E78", "E11", "E87"},
    #"Respiratory Diseases": {"J96"},
    "Diseases": {"E78", "E11", "E87", "J96"},
    #"Kidney and Urinary Diseases": {"N17"},
    "Neonatal and Pregnancy Conditions": {"P07", "P00", "Z38"},
    #"Medical History and Other Chronic Conditions": {"Z79", "Z85", "R65"},
    #"Special and Unclassified Categories": {"NoD"}

}

# List of relevant ITEMIDs (example - should be updated based on available data)
relevant_itemids =  {
    51221, 51301, 51265, 51222, 51249,
    51250, 51279, 51248, 51277, 50902,
    50983, 50971, 50882, 50868, 51006,
    50912, 50931, 50960, 50893, 50970
}


# Create a new column for category
def categorize_icd(icd_code):
    for category, codes in icd_categories.items():
        if icd_code in codes:
            return category
    return None

# Apply categorization
df_all_table['Category'] = df_all_table['icd10cm'].apply(categorize_icd)

# Remove rows with ICD codes that do not belong to any category
df_categorized = df_all_table.dropna(subset=['Category'])

# Keep only relevant columns
df_categorized = df_categorized[['SUBJECT_ID', 'Category'] + [str(item) for item in relevant_itemids]]

# Save the categorized table
df_categorized.to_csv("A:/FinalProjectMagshimim/CATEGORIZED_ICD_TABLE_BY_ELINOR.csv", index=False)

# Function to print statistics
def print_statistics(df):
    print("\nCategory Counts:")
    print(df['Category'].value_counts())

    # Compute the top 20 ITEMIDs with the highest number of non-null values
    top_items = df.iloc[:, 2:].count().nlargest(20)
    print("\nTop 20 tests (ITEMID) with the highest number of non-null values:")
    print(top_items)

# Print statistics
print_statistics(df_categorized)
