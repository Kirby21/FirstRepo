import streamlit as st

st.header('Foms in streamlit')

form =  st.form(key='form',
                clear_on_submit=True,
                enter_to_submit=True,
                border=True
                )

spell = form.selectbox(label='Spells',
               options=['quas','wex','hex','invoke'])

submit = form.form_submit_button(label='Submit')
if submit:
    st.write('Selected Spell: {}'.format(spell))


second_form = st.sidebar.form(key='sidebar_form',
                              )

age = second_form.number_input(label='level',
                               min_value=0,
                               max_value=100,
                               step=1,
                               value=0)
submit_second = second_form.form_submit_button(label='Submit')

if submit_second:
    second_form.write('Level is: {}'.format(age))
