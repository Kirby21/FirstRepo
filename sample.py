import streamlit as st

# Sidebar layout
st.sidebar.title("Navigation")
st.sidebar.selectbox("Choose a page", ["Home", "About", "Settings"])

# Main layout
st.title("Dashboard")
st.subheader("Welcome to Your App")

# Columns
col1, col2 = st.columns(2)
col1.metric("Users", "1,234")
col2.metric("Revenue", "$5,678")

# Tabs
tab1, tab2 = st.tabs(["Overview", "Details"])
with tab1:
    st.write("This is the overview tab.")
with tab2:
    st.write("This is the details tab.")

# Expander
with st.expander("Show Advanced Options"):
    st.checkbox("Enable feature X")
    st.text_input("Set threshold")

# Footer-style note
st.caption("Built with Streamlit")