# 💼 IT Salary Survey Analysis (2018–2020) Proposal 📊

## 🧾 Project Overview
This project explores salary trends among IT professionals across Europe using three years of anonymous salary survey data (2018–2020). The goal is to uncover insights related to compensation patterns based on job roles, experience levels, locations, company types, and technologies used in the industry.

The dataset includes rich demographic and professional details from multiple years, allowing for both cross-sectional and longitudinal analysis.

---

## 📁 Dataset Sources
All datasets are sourced from Kaggle:

🔗 [2020 IT Salary Survey for EU Region](https://www.kaggle.com/datasets/parulpandey/2020-it-salary-survey-for-eu-region)

Includes:
- `IT Salary Survey EU 2018.csv`
- `T Salary Survey EU 2019.csv`
- `IT Salary Survey EU 2020.csv`

Each file contains anonymized responses covering:
- Age
- Gender
- Location (City, Country)
- Job Title
- Seniority Level
- Years of Experience
- Salary Figures
- Tech Stack / Domain
- Company Size
- Employment Type
- Industry Focus

---

## 🎯 Objectives
- Perform **Exploratory Data Analysis (EDA)** to identify key trends in IT salaries.
- Compare salary changes over time (2018–2020).
- Analyze how **experience**, **location**, **job type**, and **technology stack** affect income.
- Visualize and report findings clearly for HR teams, job seekers, and policymakers.

---

## 🔍 Key Questions to Explore
- How have average IT salaries changed between 2018 and 2020? 📈
- Which job roles offer the highest pay in Europe? 💰
- What are the top-paying cities and countries for IT professionals? 🌍
- How does salary vary by gender, experience level, and industry? 🚻
- What tech stacks or domains correlate with higher compensation? 🧠

---

## 🛠️ Tools & Technologies
| Task                        | Tool/Library               |
|----------------------------|-----------------------------|
| Data Manipulation          | Pandas, NumPy              |
| Visualization              | Matplotlib, Seaborn        |
| Report Generation          | Jupyter Notebook / Markdown|
| Hosting / Documentation    | GitHub                     |

---

## 🧩 Methodology

### 1. **Data Integration**
- Load all three datasets (`2018`, `2019`, `2020`) using Pandas.
- Identify overlapping and unique columns.
- Rename and normalize column names for consistency.
- Merge datasets into a unified DataFrame with a new `Year` column for temporal analysis.

### 2. **Data Cleaning**
- Handle missing values: impute where appropriate or drop rows/columns if negligible.
- Convert inconsistent data types (e.g., salary strings to numeric).
- Normalize categorical variables:
  - Map equivalent job titles (e.g., "Fullstack" vs "Full-stack")
  - Standardize location names (e.g., "Munich" vs "München")
  - Harmonize seniority levels (e.g., "Senior", "Lead", "Principal")
- Detect and handle outliers in salary fields using IQR or Z-score methods.

### 3. **Feature Engineering**
- Derive new features such as:
  - Salary per year of experience (`Salary / Years_of_Experience`)
  - Salary change per year (for longitudinal analysis)
  - Binary flag for remote work availability (from 2020 data)
- Encode categorical variables using:
  - One-Hot Encoding for nominal categories (e.g., city, country)
  - Ordinal Encoding for ordered categories (e.g., seniority levels)

### 4. **Exploratory Data Analysis (EDA)**
- Summary statistics: mean, median, min/max salaries.
- Distribution plots: histogram, boxplots, violin plots.
- Grouped analysis:
  - Salary by job title and experience level
  - Salary by location (city/country heatmaps)
  - Salary by tech stack/domain
- Correlation matrices and pair plots to explore relationships.
- Time-based analysis: salary growth, role popularity, location shifts.

### 5. **Visualization Strategy**
- Use **Seaborn** and **Matplotlib** for:
  - Line charts showing salary trends over time
  - Bar charts comparing job roles
  - Heatmaps of salary distribution by country
  - Scatter plots for salary vs. experience
  - Cluster maps to visualize tech stack clusters
- Optional: use **Plotly/Dash** for interactive dashboards.

### 6. **Insights & Reporting**
- Top-paying roles and technologies.
- Comparison of salary growth between years.
- Country-wise salary rankings.
- Recommendations for professionals and employers.
- Export cleaned datasets for further machine learning modeling.

---

## 📦 Deliverables
- Cleaned and integrated dataset (`CSV`)
- Jupyter Notebook with EDA and visualizations
- Final report summarizing findings and visual dashboards

---

## ✅ Technical Workflow Summary

```
Raw Datasets
│
├── Load and Normalize Columns
├── Handle Missing Values
├── Convert Data Types
├── Encode Categorical Features
├── Feature Engineering
├── Exploratory Data Analysis
├── Visualization Dashboards
└── Export Insights & Cleaned Data
```
