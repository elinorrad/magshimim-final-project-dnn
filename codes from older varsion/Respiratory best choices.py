import pandas as pd

# קריאת הקובץ ALL_TABLE.csv
file_path = "A:/FinalProjectMagshimim/ALL_TABLE.csv"
df_all_table = pd.read_csv(file_path)

# שמירה רק על 3 התווים הראשונים של ICD10
df_all_table['icd10cm'] = df_all_table['icd10cm'].astype(str).str[:3]

# עדכון קבוצות ה-ICD10 הרלוונטיות
respiratory_codes = {"J44", "J45"}


respiratory_itemids = {51221, 51222, 51248, 51249, 51250, 51277,
                       51279, 51265, 51301, 50912, 51006, 50902,
                       50971, 50983, 50868, 50882, 50931, 50960,
                       50893, 50970}

# סינון טבלת הסוכרת לפי ICD10
df_respiratory = df_all_table[df_all_table['icd10cm'].isin(respiratory_codes)]
# שמירה רק על העמודות הרלוונטיות
columns_to_keep_respiratory = ['SUBJECT_ID', 'icd10cm'] + [str(item) for item in respiratory_itemids]
df_respiratory = df_respiratory[columns_to_keep_respiratory]
df_respiratory.to_csv("A:/FinalProjectMagshimim/RESPIRATORY_ALL_BY_ELINOR.csv", index=False)

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
print_statistics(df_respiratory, "RESPIRATORY_ALL_BY_ELINOR")
