
import streamlit as st


def app(df):

    st.title("𝐃𝐚𝐭𝐚 𝐈𝐧𝐟𝐨 𝐏𝐚𝐠𝐞")
    st.subheader("View Data")

    with st.expander("View data"):
        st.dataframe(df)

    st.subheader("Columns Description:")

    if st.checkbox("View Summary"):
        st.dataframe(df.describe())

    col_name, col_dtype, col_data = st.columns(3)

    with col_name:
        if st.checkbox("Column Names"):
            st.dataframe(df.columns)

    with col_dtype:
        if st.checkbox("Columns data types"):
            dtypes = df.dtypes.apply(lambda x: x.name)
            st.dataframe(dtypes)
    
    with col_data: 
        if st.checkbox("Columns Data"):
            col = st.selectbox("Column Name", list(df.columns))
            st.dataframe(df[col])

    