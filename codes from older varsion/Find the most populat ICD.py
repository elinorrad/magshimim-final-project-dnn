import pandas as pd
from collections import Counter
import os

# בדיקה אם הקובץ קיים
input_csv = "A:/FinalProjectMagshimim/ALL_TABLE.csv"
if not os.path.exists(input_csv):
    raise FileNotFoundError(f"הקובץ {input_csv} לא נמצא, ודא שהנתיב נכון")

# קריאת הקובץ הראשי עם בדיקה על עמודות זמינות
try:
    df = pd.read_csv(input_csv, usecols=['icd10cm'], dtype=str)
except ValueError:
    df = pd.read_csv(input_csv, dtype=str)
    if 'icd10cm' not in df.columns:
        raise KeyError("עמודת 'icd10cm' לא נמצאה בקובץ, בדוק את שמות העמודות.")

# שמירת שלושת התווים הראשונים של עמודת icd10cm
df['icd10cm_prefix'] = df['icd10cm'].astype(str).str[:3]

# ספירת 30 הערכים הנפוצים ביותר
icd10_counts = Counter(df['icd10cm_prefix'].dropna())
top_30_icd10 = icd10_counts.most_common(30)

# קריאת קובץ המשמעויות
icd_categories_csv = "A:/FinalProjectMagshimim/haifa-1605-medical/categories_ICD10.csv"
if not os.path.exists(icd_categories_csv):
    raise FileNotFoundError(f"הקובץ {icd_categories_csv} לא נמצא, ודא שהנתיב נכון")

# קריאת הקובץ עם בדיקה לשמות עמודות
icd_categories_df = pd.read_csv(icd_categories_csv, dtype=str, encoding='utf-8')
icd_categories_df.columns = icd_categories_df.columns.str.strip()  # ניקוי רווחים מיותרים

# הדפסת שמות העמודות כדי לוודא התאמה
print("שמות עמודות בקובץ המשמעויות:", icd_categories_df.columns.tolist())

# שימוש בשמות העמודות המדויקים
col_code = icd_categories_df.columns[0]  # שם העמודה של הקודים
col_desc = icd_categories_df.columns[1]  # שם העמודה של המשמעויות

icd_categories_dict = dict(zip(icd_categories_df[col_code], icd_categories_df[col_desc]))

# יצירת רשימה עם המידע הרצוי
output_lines = []
for icd, count in top_30_icd10:
    meaning = icd_categories_dict.get(icd, "Unknown")
    output_lines.append(f"{icd}: {meaning} ({count} appearances)")

# כתיבת התוצאה לקובץ
output_txt = "A:/FinalProjectMagshimim/MOST_POPULAR_ICD.txt"
with open(output_txt, "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print(f"הקובץ נוצר בהצלחה: {output_txt}")
