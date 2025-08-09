# College Major Salary Analysis with Pandas 🎓💰

![Pandas Logo](https://pandas.pydata.org/static/img/pandas_white.svg)

An analysis of post-university salaries by college major using Python's Pandas library. This project explores which degrees lead to the highest earnings and which represent the best value.

* [Google Colab Notebook](https://colab.research.google.com/drive/1KCnM0R0l7yv_NGJ3MED2SNbQKJqemtQB)

## 🔍 Project Overview

Using PayScale's survey data of 1.2 million Americans with bachelor's degrees, this analysis answers key questions about the ROI of different college majors:

- Which degrees have the highest starting salaries?
- Which majors have the lowest earnings after college?
- What degrees have the highest earning potential?
- Which are the lowest-risk majors from an earnings standpoint?
- Do STEM, Business or HASS degrees earn more on average?

## 📊 Key Findings

### Highest Earning Majors
* | Rank | Major | Mid-Career 90th Percentile Salary |
* |------|-------|-----------------------------------|
* | 1 | **Economics** | $210,000 |
* | 2 | **Chemical Engineering** | $194,000 |
* | 3 | **Finance** | $195,000 |

### Lowest Risk Majors (Smallest Salary Spread)
1. **Nursing**  
2. **Physician Assistant**  
3. **Nutrition**  

### By Degree Category (Average Mid-Career Salary):
1. **STEM**: $92,763  
2. **Business**: $84,247  
3. **HASS**: $63,316  

## 🛠️ Technical Implementation

## Data Exploration Techniques

### Basic dataframe inspection
* clean_df.head()
* clean_df.shape
* clean_df.columns

###  Handling missing data
* clean_df = df.dropna()

### Accessing specific data points
* clean_df['Starting Median Salary'].max()
* clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmax()]

# Advanced Analysis
### Sorting by salary potential
* highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)

### Calculating risk (salary spread)
* clean_df.insert(1, 'Spread', clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary'])

### Grouping by category
* clean_df.groupby('Group').mean()

---

# 📚 Skills Demonstrated
* Pandas DataFrame manipulation

* Data cleaning with .dropna()

* Column operations and sorting

* GroupBy aggregations

* Salary spread calculations

* Data visualization basics

---

# 📈 Insights for Students
* STEM degrees dominate high earnings

* Business degrees offer good balance of risk/reward

* HASS degrees have wider salary variability

* Physician Assistant has both high median and low spread
---

# 🤝 Contributing
* Pull requests welcome! For major changes, please open an issue first.
---

# 📜 License
* [MIT License](https://choosealicense.com/licenses/mit/)
---
