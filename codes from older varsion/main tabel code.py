import pandas as pd

# יצירת קבוצת כל ה-ITEMID ללא כפילויות
anemia_itemids = {51221, 51222, 51248, 51249, 51250, 51277, 51279, 51301,
                  50868, 50882, 50902, 50912, 50931, 50971, 50983, 51006, 51265}

diabetes_itemids = {51265, 51221, 51301, 51222, 51249, 51248, 51250, 51279,
                    50912, 51006, 51277, 50882, 50902, 50971, 50983, 50868,
                    50931, 50960, 50970, 50893}

respiratory_itemids = {51221, 51222, 51248, 51249, 51250, 51277,
                       51279, 51265, 51301, 50912, 51006, 50902,
                       50971, 50983, 50868, 50882, 50931, 50960,
                       50893, 50970}

infectious_itemids = {51221, 51222, 51248, 51249, 51250, 51277,
                      51279, 51301, 50868, 50882, 50902, 50971,
                      50983, 51006, 50912, 50893, 50931, 50970,
                      51265, 50960}

all_itemid = anemia_itemids | diabetes_itemids | respiratory_itemids | infectious_itemids

# יצירת מיפוי של קודים לערכים אחידים
code_mapping = {
    "D63": "A", "D50": "A",  # anemia_codes -> A
    "E10": "B", "E11": "B",  # diabetes_codes -> B
    "J44": "C", "J45": "C",  # respiratory_codes -> C
    "A40": "D", "M02": "D", "B96": "D", "B05": "D", "A01": "D"  # infectious_codes -> D
}

# קריאת הקובץ ALL_TABLE.csv
file_path = "A:/FinalProjectMagshimim/ALL_TABLE.csv"
df_all_table = pd.read_csv(file_path)

# שמירה רק על 3 התווים הראשונים של ICD10
df_all_table['icd10cm'] = df_all_table['icd10cm'].astype(str).str[:3]

# הוספת עמודת קטגוריה לפי ה-ICD10
df_all_table['Diagnosis_Category'] = df_all_table['icd10cm'].map(code_mapping)

# הסרת שורות עם ערך NaN ב-Diagnosis_Category (כלומר קודים שלא במיפוי)
df_all_table = df_all_table.dropna(subset=['Diagnosis_Category'])

# שמירה רק על העמודות הרלוונטיות
columns_to_keep = ['SUBJECT_ID', 'Diagnosis_Category'] + [str(item) for item in all_itemid]
df_main = df_all_table[columns_to_keep]

# שמירת הטבלה כקובץ CSV
df_main.to_csv("A:/FinalProjectMagshimim/MAIN_TABEL_ALL_BY_ELINOR.csv", index=False)

# פונקציה להדפסת סטטיסטיקות
def print_statistics(df, name):
    print(f"\n{name}:")
    icd_counts = df['Diagnosis_Category'].value_counts()
    print("כמות מופעים של כל קטגוריית אבחנה:")
    print(icd_counts)
    top_items = df.iloc[:, 2:].count().nlargest(20)
    print("\n20 הבדיקות (ITEMID) עם מספר הבדיקות הגבוה ביותר (שאינן NULL):")
    print(top_items)

# הדפסת סטטיסטיקות
print_statistics(df_main, "MAIN_TABEL_ALL_BY_ELINOR")
