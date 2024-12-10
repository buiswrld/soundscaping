import pandas as pd

class DataLoader:
    def __init__(self):
        self.df_aoty = pd.read_csv("data/raw/aoty.csv")
        self.df_top100s = pd.read_csv("data/raw/top100s.csv")
        
        self.df_aoty.rename(columns={'id': 'rank'}, inplace=True)
        self.df_top100s.insert(0, 'rank', range(1, 1 + len(self.df_top100s)))

    def load_aoty(self) -> pd.DataFrame:
        return self.df_aoty
    
    def load_top100s(self) -> pd.DataFrame:
        return self.df_top100s
    
    def length(self, df: pd.DataFrame) -> int:
        return len(df)

    def get_rows(self, df: pd.DataFrame, i: int, j: int = None) -> pd.DataFrame:
        if j is None:
            return df.iloc[i]
        return df.iloc[i:j]

    def get_col(self, df: pd.DataFrame, col: str) -> pd.DataFrame:
        return df[col]


    def filter(self, df: pd.DataFrame, column: str, value, contains=False) -> pd.DataFrame:
        if isinstance(value, str):
            value = value.lower()
            if contains:
                return df[df[column].str.lower().str.contains(value, na=False)]
            return df[df[column].str.lower() == value]
        else:
            if contains:
                return df[df[column].str.contains(value, na=False)]
            return df[df[column] == value]

    def count_occurrences(self, df: pd.DataFrame, column: str, value) -> int:
        return df[df[column] == value].shape[0]

    def count(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
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


    def split_proportion(self, df: pd.DataFrame, col: str, split: int) -> dict:
        above_split = len(df[df[col] > split])
        below_split = len(df[df[col] <= split])
        return {
            'above_split': above_split,
            'below_split': below_split
        }
