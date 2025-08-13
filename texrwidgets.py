import pandas as pd
import streamlit as st

st.markdown(' # markdown display')
st.markdown(' ## markdown display')
st.markdown(' ### markdown display')

st.header(' this is header')
st.subheader('this is subheader')
st.text('this is text')
st.caption('this is caption')

code_snippet = """

def greet(name):
    returns f"Hello, {name}"

"""

st.code(code_snippet, language='python')

mylist = ['a', 'b', 'c']

mydict = {'a':1, 'b':2, 'c':3}

st.write(mylist)
st.write(mydict)