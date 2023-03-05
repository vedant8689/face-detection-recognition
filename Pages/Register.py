import streamlit as st
import papermill
st.set_page_config(
    page_title="JK Lakshmi Cement",
    page_icon="👋",
)
st.title('Register new Employee!!')

st.text(
''' 
How to Register?? - Employee Need to Focus on Camera with normal and
Natural smile on the Face
'''
)
st.text(
''' 
Within 2 or 3 seconds System Manager need to 
Press Y key for Yes (Yes for Proper Frame Capturing of the Employee)
'''
)


def execute_notebook():
    papermill.execute_notebook(
        'Pages/Register.ipynb',
        'output.ipynb'
    )


if st.button("Register Here"):
    execute_notebook()
