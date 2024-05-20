# Mock_Pandas

# 1 Problem 1 : Not Boring Movies (Mock Problem) (https://leetcode.com/problems/not-boring-movies/)

import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    df = cinema[(cinema['id']%2 == 1) & (cinema['description']!='boring')]
    return df.sort_values(by =['rating'], ascending = False)

# 2 Problem 2 : Biggest Single Number (Mock Problem) ( https://leetcode.com/problems/biggest-single-number/ )

import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df = my_numbers.drop_duplicates(keep= False)
    df = pd.DataFrame(df.max(), columns = ['num'])
    return df

