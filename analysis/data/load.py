import pandas as pd

df_aoty = pd.read_csv("data/raw/aoty.csv")
df_top100s = pd.read_csv("data/raw/top100s.csv")

df_aoty.rename(columns={'id': 'rank'}, inplace=True)

def get_rows(df: pd.DataFrame, i: int, j: int = None) -> pd.DataFrame:
    if j is None:
        return df.iloc[i]
    return df.iloc[i:j]

def get_col(df: pd.DataFrame, col: str) -> pd.DataFrame:
    return df[col]

def filter(df: pd.DataFrame, column: str, value) -> pd.DataFrame:
    return df[df[column] == value]

def count_occurrences(df: pd.DataFrame, column: str, value) -> int:
    return df[df[column] == value].shape[0]

def count(df: pd.DataFrame, column: str) -> pd.DataFrame:
    counts = {}
    for items in df[column]:
        item_list = [item.strip() for item in items.split(',')]
        for item in item_list:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1
    count_df = pd.DataFrame(list(counts.items()), columns=[column.capitalize(), 'Count'])
    count_df = count_df.sort_values(by='Count', ascending=False)
    return count_df