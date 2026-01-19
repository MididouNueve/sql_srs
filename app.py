import io
import streamlit as st
import pandas as pd
import duckdb as duckdb

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# solution_df = duckdb.sql(ANSWER_STR).df()

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ("cross_joins", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="Select a theme...",
    )

    st.write("You selected:", theme)

exercise = con.execute(
    f"SELECT * FROM memory_state WHERE theme = '{theme}'"
).df()

st.write(exercise)


with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ("Groupbys", "cross_joins", "Windows functions"),
        index=None,
        placeholder="Select a theme...",
    )
    st.write("You selected:", option)


st.header("enter your code:")
query = st.text_area(label="votre code SQL ici", key="user_input")

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)


tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)

    st.write("table: food_items")
    st.dataframe(food_items)

    st.write("expected:")
    st.dataframe(solution)

with tab3:
    st.write(answer)
