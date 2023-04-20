# Update test
import sqlconn.conn  # sqlconn is a private package use pyodbc - it is implemented in other repository

# do not forget to give the permission to access for user to the database which will be connected
# database = 'AdventureWorksDW2019'
database = 'Test'

table = 'DimProductCategory'

conn = sqlconn.conn.create_conn(database)

"""df = conn.create_dataframe(f'{table}')

print(df)

df.info()  # 4 rows * 5 columns

col_list = conn.get_columns(table)"""

"""
['ProductCategoryKey', 'ProductCategoryAlternateKey', 
'EnglishProductCategoryName', 'SpanishProductCategoryName', 
'FrenchProductCategoryName']

"""

cursor = conn.cursor()

# Update table with query= statement

query = f"INSERT INTO {table}\
           ([ProductCategoryAlternateKey]\
           ,[EnglishProductCategoryName]\
           ,[SpanishProductCategoryName]\
           ,[FrenchProductCategoryName])\
        VALUES\
           (6\
           ,'English Coat'\
           ,'Spanish Coat'\
           ,'French Coat')"

try:
    cursor.execute(query)
    print('Insert Successfully Completed')
except ValueError:
    print('Error occurred!')


# if you do not use commit() sql table will not be updated,
# but check the identity key is increased, it is used but not updated before commit
conn.commit()


# cursor.close() - do not forget to close connection as conn.close()
conn.close() # do not ever forget to close conn - it is vital otherwise sql will not be used properly
