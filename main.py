import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
import sqlcon
import mysql.connector

# Initialize connection.
# conn = st.experimental_connection('mysql', 'sql')

# Perform query.
# df = conn.query("select * from stat_user_total_study_history where entry_date > '2023-06-10';", ttl=600)
engine = create_engine(sqlcon.url)


# 쿼리 작성
query_a = "select * from stat_user_total_study_history where entry_date > '2023-06-08' "
df = pd.read_sql_query(query_a, con=engine)


st.write(df)

