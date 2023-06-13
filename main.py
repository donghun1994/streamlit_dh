import streamlit as st
import pandas as pd
import matplotlib.pyplot

# streamlit_app.py

import streamlit as st



# Initialize connection.
conn = st.experimental_connection('mysql', 'sql')

# Perform query.
df = conn.query("select * from stat_user_total_study_history where entry_date > '2023-06-10';", ttl=600)


st.write(df)