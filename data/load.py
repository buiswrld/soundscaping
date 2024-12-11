import pandas as pd

# Reference: (7), (8), (16), (19), (20)
class DataLoader:

    # Reference: (19), (7), (8)
    def __init__(self):
        self.df_aoty = pd.read_csv("data/raw/aoty.csv")
        self.df_top100s = pd.read_csv("data/raw/top100s.csv")
        
        self.df_aoty.rename(columns={'id': 'rank'}, inplace=True)
        self.df_top100s.insert(0, 'rank', range(1, 1 + len(self.df_top100s)))

    def load_aoty(self) -> pd.DataFrame:
        """
        Load the AOTY dataset.
        Returns: 
        pd.DataFrame: The AOTY dataset.
        """
        return self.df_aoty
    
    def load_top100s(self) -> pd.DataFrame:
        """
        Load the Spotify Top 100 songs dataset.
        
        Returns:
        pd.DataFrame: The Spotify Top 100 dataset.
        """
        return self.df_top100s
    
    def length(self, df: pd.DataFrame) -> int:
        """
        Get the number of rows (length) in the DataFrame.
        
        Parameters:
        df (pd.DataFrame): The DataFrame to measure.
        
        Returns:
        int: The number of rows in the DataFrame.
        """
        return len(df)

    def get_rows(self, df: pd.DataFrame, i: int, j: int = None) -> pd.DataFrame:
        """
        Get a specific subsection of rows from the DataFrame
        
        Parameters:
        df (pd.DataFrame): The DataFrame to slice.
        i (int): The starting index.
        j (int, optional): The ending index. If None, we treat j as i+1.
        
        Returns:
        pd.DataFrame: The sliced DataFrame from i to j.
        """
        if j is None:
            return df.iloc[i]
        return df.iloc[i:j]

    def get_col(self, df: pd.DataFrame, col: str) -> pd.DataFrame:
        """
        Get a column from the DataFrame.
        
        Parameters:
        df (pd.DataFrame): The DataFrame to extract the column from.
        col (str): The name of the column to extract.
        
        Returns:
        pd.Series: The extracted column.
        """
        return df[col]
    
    # Reference: (16), (19)
    def filter(self, df: pd.DataFrame, column: str, value, contains=False) -> pd.DataFrame:
        """
        Filter the DataFrame based on the contents of a column and a desired value.
        
        Parameters:
        df (pd.DataFrame): The DataFrame to filter.
        column (str): The name of the column to filter through.
        value: The value to filter by. Case insensitive if a string.
        contains (bool): If True, will utilize the "contains()" function to omit the need for exact matches. Otherwise, perform an exact match.
        
        Returns:
        pd.DataFrame: The filtered DataFrame.
        """
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
        """
        Count the occurrences of a value in a column. Designed to be more efficient than filter in certain cases.
        
        Parameters:
        df (pd.DataFrame): The DataFrame with the column
        column (str): The name of the column to count in.
        value: The value to count for. Uses exact matching.
        
        Returns:
        int: The number of occurrences of the value in the column.
        """
        return df[df[column] == value].shape[0]
    
    # Reference: (19), (20)
    def count(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
        """
        Count the occurrences of each unique value in a column. Intended for multiple counts; a broader case of count_occurrences.
        
        Parameters:
        df (pd.DataFrame): The DataFrame to count in.
        column (str): The name of the column to count in.
        
        Returns:
        pd.DataFrame: A DataFrame with the counts of each unique value.
        """
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
        """
        Calculate the proportion of values above and below a split point in a column.
        
        Parameters:
        df (pd.DataFrame): The DataFrame to analyze.
        col (str): The name of the column to analyze.
        split (int): The split point.
        
        Returns:
        dict: A dictionary with the counts of values above and below/equal to the split point.
            - 'above_split': The frequency of values above the split point.
            - 'below_split': The frequency of values below or equal to the split point.
        """
        above_split = len(df[df[col] > split])
        below_split = len(df[df[col] <= split])
        return {
            'above_split': above_split,
            'below_split': below_split
        }
