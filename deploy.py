import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.title("📊 Employee Data Analysis Dashboard")

# Show merged data
st.subheader("📋 Merged Data")
st.dataframe(df)

# Show average salary
st.subheader("💰 Average Salary by Department")
st.dataframe(avg_salary)

# Visual 1: Boxplot - Salary by Department
st.subheader("📦 Salary Distribution by Department")
fig1, ax1 = plt.subplots()
sns.boxplot(x='department', y='salary', data=df, ax=ax1)
st.pyplot(fig1)

# Visual 2: Scatterplot - Performance vs Salary
st.subheader("📈 Performance vs Salary")
fig2, ax2 = plt.subplots()
sns.scatterplot(x='performance_rating', y='salary', hue='department', data=df, ax=ax2)
st.pyplot(fig2)

# Visual 3: Correlation Heatmap
st.subheader("📊 Correlation Heatmap")
fig3, ax3 = plt.subplots()
sns.heatmap(correlation, annot=True, cmap="coolwarm", ax=ax3)
st.pyplot(fig3)
