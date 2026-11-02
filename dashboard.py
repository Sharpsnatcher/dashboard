# Простой дашборд: загрузка CSV и вывод графика
# Запуск: python3 -m streamlit run dashboard.py
import pandas as pd
import streamlit as st

st.title("Личные расходы")

# 1. Загрузка CSV
df = pd.read_csv("expenses.csv")

# 2. Оставляем только расходы (как в analysis.py)
expenses = df[(df["Transaction Type"] == "debit") & (df["Category"] != "Credit Card Payment")]

# 3. Показатели
st.write("Количество расходов:", len(expenses))
st.write("Средний расход:", round(expenses["Amount"].mean(), 2))

# 4. График: сумма расходов по категориям
categories = expenses.groupby("Category")["Amount"].sum().sort_values(ascending=False)
st.bar_chart(categories, sort=False)
