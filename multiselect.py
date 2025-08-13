import streamlit as st


spells = ['quas','hex','wex','invoke']



selected_spell = st.multiselect(label='select spell',
                                options=spells,)

st.write(selected_spell)