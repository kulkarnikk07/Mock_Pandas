# Mock_Pandas

# 1 Problem 1 : Not Boring Movies (Mock Problem) (https://leetcode.com/problems/not-boring-movies/)  05/19/24

import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    df = cinema[(cinema['id']%2 == 1) & (cinema['description']!='boring')]
    return df.sort_values(by =['rating'], ascending = False)

# 2 Problem 2 : Biggest Single Number (Mock Problem) ( https://leetcode.com/problems/biggest-single-number/ ) 05/19/24

import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df = my_numbers.drop_duplicates(keep= False)
    df = pd.DataFrame(df.max(), columns = ['num'])
    return df

# 3 Problem 3 :Sales Analysis III (Mock Problem) (https://leetcode.com/problems/sales-analysis-iii/)



# 4 Problem 4 : Market Analysis I (Mock Problem) ( https://leetcode.com/problems/market-analysis-i/) 

