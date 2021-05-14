import pandas as pd
pd.options.display.max_columns = None
pd.options.display.float_format = '{:,.1f}'.format
import sqlite3

# -----------------------------------------------------------------------------
# DATABASE CONFIG
# -----------------------------------------------------------------------------
db_path = 'chemographs.sqlite'
db = sqlite3.connect(db_path, check_same_thread=False)
table_name = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", db)

try:    
    if table_name['name'].str.contains('RawDATA').any():
        RawDATA = pd.read_sql_query(sql="SELECT * FROM RawDATA", con=db)
    else:
        print("ERROR: RawDATA TABLE NOT EXIST")

    if table_name['name'].str.contains('GeoinformationDATA').any():
        GeoinformationDATA = pd.read_sql_query(sql="SELECT * FROM GeoinformationDATA", con=db)
    else:
        print("ERROR: GeoinformationDATA TABLE NOT EXIST")
except:
    print("ERROR: DATABASE NOT EXIST")