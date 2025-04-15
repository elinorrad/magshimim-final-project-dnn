import pandas as pd

# קריאת הקובץ ALL_TABLE.csv
file_path = "A:/FinalProjectMagshimim/ALL_TABLE.csv"
df_all_table = pd.read_csv(file_path)

# שמירה רק על 3 התווים הראשונים של ICD10
df_all_table['icd10cm'] = df_all_table['icd10cm'].astype(str).str[:3]

# עדכון קבוצות ה-ICD10 הרלוונטיות
anemia_codes = {"D63", "D50"}
diabetes_codes = {"E10", "E11"}

# עדכון רשימות ה-ITEMID לכל מחלה
anemia_itemids = {51221, 51222, 51248, 51249, 51250, 51277, 51279, 51301,
                  50868, 50882, 50902, 50912, 50931, 50971, 50983, 51006, 51265}

diabetes_itemids = {51265, 51221, 51301, 51222, 51249, 51248, 51250, 51279,
                    50912, 51006, 51277, 50882, 50902, 50971, 50983, 50868,
                    50931, 50960, 50970, 50893}

# סינון טבלת האנמיה לפי ICD10
df_anemia = df_all_table[df_all_table['icd10cm'].isin(anemia_codes)]
# שמירה רק על העמודות הרלוונטיות
columns_to_keep_anemia = ['SUBJECT_ID', 'icd10cm'] + [str(item) for item in anemia_itemids]
df_anemia = df_anemia[columns_to_keep_anemia]
df_anemia.to_csv("A:/FinalProjectMagshimim/ANEMIA_ALL_BY_ELINOR.csv", index=False)

# סינון טבלת הסוכרת לפי ICD10
df_diabetes = df_all_table[df_all_table['icd10cm'].isin(diabetes_codes)]
# שמירה רק על העמודות הרלוונטיות
columns_to_keep_diabetes = ['SUBJECT_ID', 'icd10cm'] + [str(item) for item in diabetes_itemids]
df_diabetes = df_diabetes[columns_to_keep_diabetes]
df_diabetes.to_csv("A:/FinalProjectMagshimim/DIABETES_ALL_BY_ELINOR.csv", index=False)

# פונקציה להדפסת סטטיסטיקות
def print_statistics(df, name):
    print(f"\n{name}:")

    # ספירת מופעים של כל ICD10
    icd_counts = df['icd10cm'].value_counts()
    print("כמות מופעים של כל ICD10:")
    print(icd_counts)

    # חישוב 20 ה-ITEMID עם מספר הערכים שאינם NULL הגבוה ביותר
    top_items = df.iloc[:, 2:].count().nlargest(20)
    print("\n20 הבדיקות (ITEMID) עם מספר הבדיקות הגבוה ביותר (שאינן NULL):")
    print(top_items)

# הדפסת סטטיסטיקות
print_statistics(df_anemia, "ANEMIA_ALL_BY_ELINOR")
