
#make a table containing all the data

import pandas as pd

file_path_1 = "A:/FinalProjectMagshimim/LABEVENTS.csv"
file_path_2 = "A:/FinalProjectMagshimim/DIAGNOSES_ICD.csv"
file_path_3 = "A:/FinalProjectMagshimim/icd9toicd10cmgem.csv"

df_labevents = pd.read_csv(file_path_1)
df_diagnoses_icd = pd.read_csv(file_path_2)
df_icd9_to_icd10 = pd.read_csv(file_path_3)

df_diagnoses_icd = df_diagnoses_icd.merge(df_icd9_to_icd10, left_on='ICD9_CODE', right_on='icd9cm', how='left')

df_diagnoses_icd = df_diagnoses_icd.dropna(subset=['icd10cm'])

pivot_labevents = df_labevents.pivot_table(index='SUBJECT_ID', columns='ITEMID', values='VALUENUM', aggfunc='first')

final_table = df_diagnoses_icd[['SUBJECT_ID', 'icd10cm']].drop_duplicates().merge(pivot_labevents, on='SUBJECT_ID', how='left')

final_table.to_csv("A:/FinalProjectMagshimim/ALL_TABLE.csv", index=False)

print("done making ALL_TABLE.csv")
