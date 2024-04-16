# %% 
import pandas as pd
import glob
import time
import duckdb
# %%
#conn = duckdb.connect("mydb.db",read_only=True)
#conn = duckdb.connect("mydb.db")
conn = duckdb.connect()
# %%
# 판다스 코드
cur_time = time.tine()
df = pd.concat([pd.read_csv(f) for f in glob.glob('dataset/*.csv')])
print(f"time : {(time.tiem() - cur_time)}")
print(df.head(10))
# %%
cur_time = time.time()
df = conn.execute("""
             SELECT *
             FROM 'dataset/*.csv'
             LIMIT 10
""").df()

print(f"time: {(time.time() - cur_time)}")
print(df)
# 자동으로 컬럼의 헤드를 지정하는 것
# %%
#자동으로 헤더 설정
cur_time = time.time()
df = conn.execute("""
             SELECT *
             FROM read_csv_auto('dataset/*.csv',header =True) 
             LIMIT 10
""").df()
print(df)



# %%
# 데이터 타입 지정
cur_time = time.time()
df = conn.execute("""
             SELECT *
             FROM read_csv_auto('dataset/*.csv',header =True, columns = {'Order ID' : 'INTEGER'})
             LIMIT 10
""").df()
print(df)
# %% 
conn.register("df_view", df)
conn.execute("DESCRIBE df_view").df()
# %%
df.isnull().sum()
# %% 
conn.execute("""SELECT * FROM df WHERE "Order ID" = '176558'""").df()
# %% 
conn.execute("""
CREATE OR REPLACE TABLE sales AS
            SELECT
             "Order ID* ::INTEGER AS order_id,
             Product AS product,
             "Quantity Ordered"::INTEGER AS quantity,
             "Price Each"::DECIMAL AS price_each,
             strptime("Order Date", '%m/%d/%Y %H:%M')::DATE as order_date,
             "Purchase Address" AS purchase_address
            
            FROM df
            WHERE 
             TRY_CAST("Order ID" AS INTEGER) NOTNULL
""")

# %% 
conn.execute("FROM aggregated_slaes").df()  