# Functions included in this file:
# # list_to_col


def list_to_col(df, list_col: str):
    """Takes a dataframe like the following:
    idx | list_col
    ----+----------
    1   | [1, 2]
    2   | [3, 4, 5]

    and returns the following:
    idx | list_col
    ----+----------
    1   | 1
    1   | 2
    2   | 3
    2   | 4
    2   | 5

    """
    return df.explode(list_col).reset_index(drop=True)
