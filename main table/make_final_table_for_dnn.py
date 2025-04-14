
#make the final table for the model

import pandas as pd

file_path = "A:/FinalProjectMagshimim/ALL_TABLE.csv"
df_all_table = pd.read_csv(file_path)

df_all_table['icd10cm'] = df_all_table['icd10cm'].astype(str).str[:3]

all_codes = {
    "H59", "I97", "E78", "E11", "I10", "I25", "I50", "J95", "E87", "J96", "T82", "K91", "N99", "G97", "M96", "D78",
    "H95", "L76", "I35", "I48", "N17", "P07", "Z38", "Z79", "E36", "I95", "NoD", "R65", "Z85", "P00"
}

dnn_tabel_itemids = {51221, 51301, 51265, 51222, 51249, 51248, 51250, 51279, 51277, 50902, 50983, 50971, 50882, 50868, 51006, 50912, 50931, 50960, 51237, 51274}


df_respiratory = df_all_table[df_all_table['icd10cm'].isin(all_codes)]
columns_to_keep_respiratory = ['SUBJECT_ID', 'icd10cm'] + [str(item) for item in dnn_tabel_itemids]
df_respiratory = df_respiratory[columns_to_keep_respiratory]
df_respiratory.to_csv("A:/FinalProjectMagshimim/TABEL_FOR_DNN_RUN.csv", index=False)

