
# serching test to build the dataset

import pandas as pd

file_path = "A:/FinalProjectMagshimim/ALL_TABLE.csv"
df_all_table = pd.read_csv(file_path)

df_all_table['icd10cm'] = df_all_table['icd10cm'].astype(str).str[:3]

all_codes = {

}

df_all = df_all_table[df_all_table['icd10cm'].isin(all_codes)]
df_all.to_csv("A:/FinalProjectMagshimim/TABEL_FOR_DNN_RUN.csv", index=False)

 """
    Prints basic statistics for a given DataFrame.

    Parameters:
    - df (DataFrame): The data, expected to include an 'icd10cm' column and test columns from the 3rd column onward.
    - name (str): A label for the dataset (used in the printed header).

    Prints:
    - Frequency of each ICD-10 code in the 'icd10cm' column.
    - Top 20 test columns (ITEMIDs) with the most non null values.
    """
def print_statistics(df, name):
    print(f"\n{name}:")

    icd_counts = df['icd10cm'].value_counts()
    print("amount ICD10:")
    print(icd_counts)

    top_items = df.iloc[:, 2:].count().nlargest(20)
    print("\n20 tests (ITEMID) with most test (no NULL):")
    print(top_items)


print_statistics(df_all, "TABEL_FOR_DNN_RUN")
