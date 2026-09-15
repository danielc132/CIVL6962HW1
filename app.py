import streamlit as st
from datetime import datetime

st.title("Daniel Collins CIVL 6962 HW 1")
st.write("Dashboard pipeline is successfully life")

# This clock proves the script reruns properly on the server
st.info(f"Last script rerun execution completed at: {datetime.now():%H:%M:%S}")