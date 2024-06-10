import os
import re
import pandas as pd
from tqdm import tqdm


def extract_categories(input_text):
    categories = ["", "", "", "", "", ""]

    ruibun_match = re.search(r'（([^）]+)）', input_text)
    if ruibun_match:
        categories[0] = ruibun_match.group(1)
        input_text = input_text.replace(ruibun_match.group(0), '')

    fukubun_match = re.search(r'＜([^＞]+)＞', input_text)
    if fukubun_match:
        categories[1] = fukubun_match.group(1)
        input_text = input_text.replace(fukubun_match.group(0), '')

    chuu_match = re.search(r'［([^］]+)］', input_text)
    if chuu_match:
        categories[3] = chuu_match.group(1)
        input_text = input_text.replace(chuu_match.group(0), '')

    parts = [part.strip() for part in input_text.split('\u3000') if part.strip()]

    if len(parts) > 0:
        categories[2] = parts[0]
    if len(parts) > 1:
        categories[4] = parts[1]
    if len(parts) > 2:
        saibun_parts = parts[2:]
        categories.extend(saibun_parts)  # Extend categories to include all saibun parts

    return categories

def preprocessing_table(nutrition_data: pd.DataFrame):
    all_results = []
    max_columns = 0
    for index,row in tqdm(nutrition_data.iterrows(),total=nutrition_data.shape[0]):
        result = [str(int(float(row.food_code)))]
        food_name = row["food_name"]
        
        res = extract_categories(food_name)
        result.extend(res)
        all_results.append(result)
        if len(res) > max_columns:
            max_columns = len(res)

    # Create column names based on max_columns
    column_names = ["食品番号","類区分", "副分類", "大分類", "中分類", "小分類"] + [f"細分{i+1}" for i in range(max_columns - 5)]

    # Create DataFrame with dynamic columns
    df_results = pd.DataFrame(all_results, columns=column_names)
    return df_results

