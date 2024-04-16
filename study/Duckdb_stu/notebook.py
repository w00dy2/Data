# %% 
import pandas as pd
import glob
import time
import duckdb
# %%
conn = duckdb.connect("mydb.db",read_only=True)
