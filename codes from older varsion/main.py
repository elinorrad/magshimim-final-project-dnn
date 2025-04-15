import pandas as pd

# הזנת הנתיבים של הקבצים
file_path_1 = "A:/FinalProjectMagshimim/LABEVENTS.csv"
file_path_2 = "A:/FinalProjectMagshimim/DIAGNOSES_ICD.csv"
file_path_3 = "A:/FinalProjectMagshimim/icd9toicd10cmgem.csv"

# קריאת הנתונים
df_labevents = pd.read_csv(file_path_1)
df_diagnoses_icd = pd.read_csv(file_path_2)
df_icd9_to_icd10 = pd.read_csv(file_path_3)

# מיזוג טבלת האבחונים עם טבלת ההמרה של ICD9 ל-ICD10
df_diagnoses_icd = df_diagnoses_icd.merge(df_icd9_to_icd10, left_on='ICD9_CODE', right_on='icd9cm', how='left')

# שמירה רק על שורות עם קוד ICD10 תקף
df_diagnoses_icd = df_diagnoses_icd.dropna(subset=['icd10cm'])

# יצירת טבלת בדיקות פר מטופל
pivot_labevents = df_labevents.pivot_table(index='SUBJECT_ID', columns='ITEMID', values='VALUENUM', aggfunc='first')

# מיזוג טבלת הבדיקות עם טבלת האבחונים
final_table = df_diagnoses_icd[['SUBJECT_ID', 'icd10cm']].drop_duplicates().merge(pivot_labevents, on='SUBJECT_ID', how='left')

# שמירת התוצאה בקובץ CSV
final_table.to_csv("A:/FinalProjectMagshimim/ALL_TABLE.csv", index=False)

print("הטבלה נשמרה בהצלחה בשם ALL_TABLE.csv")
