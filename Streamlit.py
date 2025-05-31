streamlit_code = """
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# === Page Setup ===
st.set_page_config(page_title="💼 IT Salary Dashboard", layout="wide")
sns.set(style="whitegrid", palette="Set2")  # Harmonized color theme
plt.rcParams.update({'figure.figsize': (8, 4)})

# === Load Data ===
df = pd.read_csv("IT Salary Combined.csv")
df.columns = df.columns.str.strip()

# === Sidebar Filters (LEFT SIDE) ===
with st.sidebar:
    st.header("🔎 Filter Options")

    gender_options = df["Gender"].dropna().unique().tolist()
    selected_genders = st.multiselect("Select Gender", gender_options, default=gender_options)

    seniority_options = df["Seniority level"].dropna().unique().tolist()
    selected_seniority = st.multiselect("Select Seniority Level", seniority_options, default=seniority_options)

    city_options = df["City"].dropna().unique().tolist()
    selected_cities = st.multiselect("Select City", city_options, default=city_options)

    company_type_options = df["Company type"].dropna().unique().tolist()
    selected_company_types = st.multiselect("Select Company Type", company_type_options, default=company_type_options)

# === Apply Filters ===
filtered_df = df[
    (df["Gender"].isin(selected_genders)) &
    (df["City"].isin(selected_cities)) &
    (df["Seniority level"].isin(selected_seniority)) &
    (df["Company type"].isin(selected_company_types))
]

# === MAIN PAGE CONTENT ===
st.markdown("<h1 style='text-align: center;'>💼 IT Salary Dashboard</h1>", unsafe_allow_html=True)
st.markdown("")

# === KPIs ===
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("👥 Total Employees", len(filtered_df))
kpi2.metric("💰 Avg Salary", f"${filtered_df['Yearly salary'].mean():,.0f}")
kpi3.metric("📈 Avg Experience", f"{filtered_df['Total years of experience'].mean():.1f} years")

st.markdown("---")

# === Helper Function ===
def display_two_columns(figures):
    for i in range(0, len(figures), 2):
        col1, col2 = st.columns(2)
        col1.pyplot(figures[i])
        if i + 1 < len(figures):
            col2.pyplot(figures[i + 1])

# === Charts Section ===
charts = []

# 1. Gender Distribution
fig, ax = plt.subplots()
sns.countplot(data=filtered_df, x="Gender", ax=ax)
ax.set_title("Gender Distribution")
charts.append(fig)

# 2. Top Cities
fig, ax = plt.subplots()
top_cities = filtered_df["City"].value_counts().nlargest(5).index
sns.countplot(data=filtered_df[filtered_df["City"].isin(top_cities)], y="City", ax=ax, order=top_cities)
ax.set_title("Top 5 Cities by Employees")
charts.append(fig)

# 3. Main Tech
fig, ax = plt.subplots()
top_tech = filtered_df["main technology"].value_counts().nlargest(10).index
sns.countplot(data=filtered_df[filtered_df["main technology"].isin(top_tech)], y="main technology", ax=ax, order=top_tech)
ax.set_title("Top 10 Main Technologies")
charts.append(fig)

# 4. Business Sectors
fig, ax = plt.subplots()
top_sectors = filtered_df["Company business sector"].value_counts().nlargest(10).index
sns.countplot(data=filtered_df[filtered_df["Company business sector"].isin(top_sectors)], y="Company business sector", ax=ax, order=top_sectors)
ax.set_title("Top 10 Business Sectors")
charts.append(fig)

# 5. Avg Salary by Position
fig, ax = plt.subplots()
top_positions = filtered_df["Position"].value_counts().nlargest(10).index
avg_salary_by_position = filtered_df[filtered_df["Position"].isin(top_positions)].groupby("Position")["Yearly salary"].mean().sort_values(ascending=True)
sns.barplot(x=avg_salary_by_position.values, y=avg_salary_by_position.index, ax=ax)
ax.set_title("Avg Salary by Top 10 Positions")
charts.append(fig)

# 6. Seniority & Company
fig, ax = plt.subplots()
senior_df = filtered_df[filtered_df["Seniority level"].str.contains("Senior", case=False, na=False)]
senior_counts_top = senior_df["Company type"].value_counts().nlargest(5)
sns.barplot(x=senior_counts_top.index, y=senior_counts_top.values, ax=ax)
ax.set_title("Top Company Types (Senior Roles)")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
charts.append(fig)

# 7. Bonus by Gender
fig, ax = plt.subplots()
avg_bonus_gender = filtered_df.groupby("Gender")["Yearly bonus"].mean()
sns.barplot(x=avg_bonus_gender.index, y=avg_bonus_gender.values, ax=ax)
ax.set_title("Average Bonus by Gender")
charts.append(fig)

# 8. Top Languages by Gender
fig, ax = plt.subplots()
sns.countplot(data=filtered_df, y="Main language at work", hue="Gender", ax=ax,
              order=filtered_df["Main language at work"].value_counts().index[:4])
ax.set_title("Top Languages at Work by Gender")
charts.append(fig)

# 9. Bonus by Seniority
fig, ax = plt.subplots()
avg_bonus_seniority = filtered_df.groupby("Seniority level")["Yearly bonus"].mean().sort_values(ascending=False).head(5)
sns.barplot(x=avg_bonus_seniority.values, y=avg_bonus_seniority.index, ax=ax)
ax.set_title("Top 5 Seniority Levels by Bonus")
charts.append(fig)

# 10. Tech by Gender
fig, ax = plt.subplots()
tech_gender = filtered_df.groupby(["main technology", "Gender"]).size().unstack().fillna(0)
top_tech = tech_gender.sum(axis=1).sort_values(ascending=False).head(5)
tech_gender.loc[top_tech.index].plot(kind="bar", ax=ax, colormap="Set2", stacked=False)
ax.set_title("Top 5 Technologies by Gender")
charts.append(fig)

# === Show Charts in Two Columns ===
display_two_columns(charts)

# === Footer ===
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Designed by Marwan Waled | Streamlit Dashboard © 2025</p>", unsafe_allow_html=True)

"""

# Save to app.py
with open("app.py", "w", encoding="utf-8") as f:
    f.write(streamlit_code)

print("Streamlit app saved as app.py")

requirements = """
streamlit
pandas
seaborn
matplotlib
"""

with open("requirements.txt", "w") as f:
    f.write(requirements.strip())

print("requirements.txt file created")