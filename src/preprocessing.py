import os
import yaml
from pathlib import Path
import pandas as pd
from utils import preprocessing_table

def read_yaml_config(config_path):
    with open(config_path, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            config = None
    return config


def df_merge(df1,df2):
    if 'WATER' in df1.columns and 'WATER' in df2.columns:
        result = pd.merge(df1, df2, on=['food_group', 'food_code', 'reference_number', 'food_name', 'WATER'], how='outer')
    else:
        result = pd.merge(df1, df2, on=['food_group', 'food_code', 'reference_number', 'food_name'], how='outer')
    return result

config_path = 'config.yaml'
config = read_yaml_config(config_path)

nutrition_data_path = Path(config["Data_path"]["Input_data_path"])
output_path = Path(config["Data_path"]["Output_data_path"])

if not os.path.exists(output_path):
    os.makedirs(output_path)

# concat_key = ["food_group", "food_code", "reference_number", "food_name","WATER"]

input_path = nutrition_data_path/"20230428-mxt_kagsei-mext_00001_012.xlsx"
column_mapping = {
    "Unnamed: 0":"food_group",
    "Unnamed: 1":"food_code",
    "Unnamed: 2":"reference_number",
    "成分識別子":"food_name",
    "Unnamed: 61":"note_012"
}
all_data = pd.read_excel(input_path, sheet_name="表全体", header=[11]).rename(columns=column_mapping)
# -----------------------------------------------------------
input_path = nutrition_data_path/"20230428-mxt_kagsei-mext_00001_022.xlsx"
column_mapping = {
    "Unnamed: 0":"food_group",
    "Unnamed: 1":"food_code",
    "Unnamed: 2":"reference_number",
    "成分識別子":"food_name",
    "Unnamed: 31":"note_022"
}
data = pd.read_excel(input_path, sheet_name="表全体", header=[4], skiprows=[5]).rename(columns=column_mapping)
all_data = df_merge(all_data, data)
# -----------------------------------------------------------
input_path = nutrition_data_path/"20230428-mxt_kagsei-mext_00001_023.xlsx"
column_mapping = {
    "Unnamed: 0":"food_group",
    "Unnamed: 1":"food_code",
    "Unnamed: 2":"reference_number",
    "成分識別子":"food_name",
    "Unnamed: 29":"note_023"
}
data = pd.read_excel(input_path, sheet_name="表全体", header=[4], skiprows=[5]).rename(columns=column_mapping)
all_data = df_merge(all_data, data)
# --------------------------------------------------------------------------------------------
input_path = nutrition_data_path/"20230428-mxt_kagsei-mext_00001_024.xlsx"
column_mapping = {
    "Unnamed: 0":"food_group",
    "Unnamed: 1":"food_code",
    "Unnamed: 2":"reference_number",
    "成分識別子":"food_name",
    "Unnamed: 27":"note_024"
}
data = pd.read_excel(input_path, sheet_name="表全体", header=[4], skiprows=[5]).rename(columns=column_mapping)
all_data = df_merge(all_data, data)
# --------------------------------------------------------------------------------------------
input_path = nutrition_data_path/"20230428-mxt_kagsei-mext_00001_025.xlsx"
column_mapping = {
    "Unnamed: 0":"food_group",
    "Unnamed: 1":"food_code",
    "Unnamed: 2":"reference_number",
    "成分識別子":"food_name",
    "Unnamed: 27":"note_025"
}
data = pd.read_excel(input_path, sheet_name="表全体", header=[4], skiprows=[5]).rename(columns=column_mapping)
all_data = df_merge(all_data, data)
# --------------------------------------------------------------------------------------------
input_path = nutrition_data_path/"20230428-mxt_kagsei-mext_00001_032.xlsx"
column_mapping = {
    "Unnamed: 0":"food_group",
    "Unnamed: 1":"food_code",
    "Unnamed: 2":"reference_number",
    "成分識別子":"food_name",
    "Unnamed: 62":"note_032"
}
data = pd.read_excel(input_path, sheet_name="表全体", header=[4], skiprows=[5]).rename(columns=column_mapping)
all_data = df_merge(all_data, data)
# --------------------------------------------------------------------------------------------
input_path = nutrition_data_path/"20230428-mxt_kagsei-mext_00001_033.xlsx"
column_mapping = {
    "Unnamed: 0":"food_group",
    "Unnamed: 1":"food_code",
    "Unnamed: 2":"reference_number",
    "成分識別子":"food_name",
    "Unnamed: 58":"note_033"
}
data = pd.read_excel(input_path, sheet_name="表全体", header=[4], skiprows=[5]).rename(columns=column_mapping)
all_data = df_merge(all_data, data)
# --------------------------------------------------------------------------------------------
input_path = nutrition_data_path/"20230428-mxt_kagsei-mext_00001_034.xlsx"
column_mapping = {
    "Unnamed: 0":"food_group",
    "Unnamed: 1":"food_code",
    "Unnamed: 2":"reference_number",
    "成分識別子":"food_name",
    "Unnamed: 59":"note_034"
}
data = pd.read_excel(input_path, sheet_name="表全体", header=[4], skiprows=[5]).rename(columns=column_mapping)
all_data = df_merge(all_data, data)
# --------------------------------------------------------------------------------------------
input_path = nutrition_data_path/"20230428-mxt_kagsei-mext_00001_042.xlsx"
column_mapping = {
    "Unnamed: 0":"food_group",
    "Unnamed: 1":"food_code",
    "Unnamed: 2":"reference_number",
    "成分識別子":"food_name",
    "Unnamed: 17":"note_042"
}
data = pd.read_excel(input_path, sheet_name="表全体", header=[4], skiprows=[5]).rename(columns=column_mapping)
all_data = df_merge(all_data, data)
# --------------------------------------------------------------------------------------------
input_path = nutrition_data_path/"20230428-mxt_kagsei-mext_00001_043.xlsx"
column_mapping = {
    "Unnamed: 0":"food_group",
    "Unnamed: 1":"food_code",
    "Unnamed: 2":"reference_number",
    "成分識別子":"food_name",
    "Unnamed: 17":"note_043"
}
data = pd.read_excel(input_path, sheet_name="表全体", header=[7],skiprows=[8]).rename(columns=column_mapping)
all_data = df_merge(all_data, data)
# --------------------------------------------------------------------------------------------
input_path = nutrition_data_path/"20230428-mxt_kagsei-mext_00001_044.xlsx"
column_mapping = {
    "Unnamed: 0":"food_group",
    "Unnamed: 1":"food_code",
    "Unnamed: 2":"reference_number",
    "成分識別子":"food_name",
    "Unnamed: 28":"note_044"
}
data = pd.read_excel(input_path, sheet_name="表全体", header=[4],skiprows=[5]).rename(columns=column_mapping)
all_data = df_merge(all_data, data)

for col in all_data.columns:
    if col.startswith('note_'):
        all_data[col] = all_data[col].str.replace('\n', '')

all_data.to_csv(output_path/"food_nutrition_all.csv", index=False)

food_categories = preprocessing_table(all_data)
food_categories.to_csv(output_path/"food_categories_all.csv", index=False)

