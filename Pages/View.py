import streamlit as st

import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="JK Lakshmi Cement",
    page_icon="👋",
) 
st.title('View Marked Attendance!!')

if st.button("View Attendance"):
    col_name = ['Employee ID', 'Date', 'Time']
    df = pd.read_csv('Pages/Attendance.csv', names = col_name)

    # Display the DataFrame in a table using Streamlit
    hide_table_row_index = """
            <style table>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    # Display a static table
    st.table(df)