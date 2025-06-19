
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load data
employees = pd.read_csv("employees.csv", parse_dates=['join_date'])
salaries = pd.read_csv("salaries.csv", parse_dates=['effective_date'])
performance = pd.read_csv("performance.csv")

# Merge all into one DataFrame
df = employees.merge(salaries, on='employee_id').merge(performance, on='employee_id')

# Add experience in years
df['experience_years'] = (pd.Timestamp.today() - df['join_date']).dt.days // 365

# Analysis
avg_salary = df.groupby('department')['salary'].mean().reset_index()
correlation = df[['salary', 'experience_years', 'performance_rating']].corr()

# Streamlit app
st.title("📊 Employee Data Analysis Dashboard")

st.subheader("📋 Merged Data")
st.dataframe(df)

st.subheader("💰 Average Salary by Department")
st.dataframe(avg_salary)

st.subheader("📦 Salary Distribution by Department")
fig1, ax1 = plt.subplots()
sns.boxplot(x='department', y='salary', data=df, ax=ax1)
st.pyplot(fig1)

st.subheader("📈 Performance vs Salary")
fig2, ax2 = plt.subplots()
sns.scatterplot(x='performance_rating', y='salary', hue='department', data=df, ax=ax2)
st.pyplot(fig2)

st.subheader("📊 Correlation Heatmap")
fig3, ax3 = plt.subplots()
sns.heatmap(correlation, annot=True, cmap="coolwarm", ax=ax3)
st.pyplot(fig3)
