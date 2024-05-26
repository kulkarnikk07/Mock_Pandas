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

# 3 Problem 3 :Sales Analysis III (Mock Problem) (https://leetcode.com/problems/sales-analysis-iii/) 5/26/2024

import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    start_date = pd.to_datetime('2019-01-01')
    end_date = pd.to_datetime('2019-03-31')

    df = sales.groupby(['product_id']).filter(lambda x: min(x['sale_date']) >= start_date and max(x['sale_date'])<=end_date)
    df = df.drop_duplicates(subset = 'product_id')
    result = df.merge(product, on = 'product_id', how = 'left')
    return result[['product_id','product_name']]

# 4 Problem 4 : Market Analysis I (Mock Problem) ( https://leetcode.com/problems/market-analysis-i/)  5/26/2024

import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    df = orders[(orders['order_date'] >= '2019-01-01') & (orders['order_date'] <= '2019-12-31')]
    df = df.groupby('buyer_id')['order_id'].size().reset_index(name ='orders_in_2019')
    result = users.merge(df, left_on ='user_id', right_on ='buyer_id', how ='left').fillna(0)
    return result[['user_id','join_date','orders_in_2019']].rename(columns = {'user_id':'buyer_id'})