cd myproject
-st.title("🎈 My new app")
+st.title("🎈 My new Streamlit app")import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("my_data.csv")
st.line_chart(df)