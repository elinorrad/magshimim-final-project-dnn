import pandas as pd

# קריאת הקובץ ALL_TABLE.csv
file_path = "A:/FinalProjectMagshimim/ALL_TABLE.csv"
df_all_table = pd.read_csv(file_path)

# שמירה רק על 3 התווים הראשונים של ICD10
df_all_table['icd10cm'] = df_all_table['icd10cm'].astype(str).str[:3]

# הגדרת קבוצות ה-ICD10 הרלוונטיות
infectious_codes = {"A40", "M02", "B96", "B05", "A01"}

# סינון טבלת הסוכרת
df_infectious = df_all_table[df_all_table['icd10cm'].isin(infectious_codes)]
df_infectious.to_csv("A:/FinalProjectMagshimim/INFECTIOUS_ALL_BY_ELINOR.csv", index=False)

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
print_statistics(df_infectious, "INFECTIOUS_ALL_BY_ELINOR")
