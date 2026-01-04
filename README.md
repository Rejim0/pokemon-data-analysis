# Exploratory Analysis of Pokémon Combat Statistics

## 📌 Overview
This project performs an exploratory data analysis (EDA) on Pokémon combat statistics to understand how different attributes such as attack, defense, speed, type, generation, and legendary status influence overall Pokémon strength. The analysis focuses on discovering patterns, relationships, and trends through statistics and visualizations rather than prediction or machine learning.

## 📂 Dataset
- **Source:** Pokémon dataset (CSV file)
- **Total Records:** 800 Pokémon
- **Features Include:**
  - HP
  - Attack
  - Defense
  - Special Attack (SpAtk)
  - Special Defense (SpDef)
  - Speed
  - Type1, Type2
  - Generation
  - Legendary status

## 🔍 Analysis Workflow

### 🔹 Stage 1 — Data Understanding
- Inspected dataset structure, shape, and data types
- Identified numerical and categorical variables
- Checked for missing values and duplicates
- Reviewed summary statistics

### 🔹 Stage 2 — Data Cleaning
- Handled missing values in the `Type2` column
- Standardized categorical text data
- Ensured consistency across the dataset

### 🔹 Stage 3 — Exploratory Data Analysis
The following key questions were explored:

- How are Pokémon stats distributed?
- Which stats vary the most?
- Are Legendary Pokémon statistically stronger?
- Which Pokémon types are fastest or strongest?
- Do Pokémon stats change across generations?
- How are different stats correlated?
- Which Pokémon are the most offensive, defensive, or balanced?

### 🔹 Custom Metrics
To better evaluate Pokémon performance:
- **Offense Score** = Attack + Special Attack  
- **Defense Score** = Defense + Special Defense  
- **Balanced Score** = Offense Score + Defense Score  

These metrics were used to rank Pokémon and identify top offensive, defensive, and balanced performers.

---

## 📊 Visualizations
The project includes:
- Histograms for stat distributions
- Boxplots comparing Legendary vs Non-Legendary Pokémon
- Bar charts for type-based comparisons
- Line plots for generation trends
- Correlation heatmaps
- Scatter plots for offense vs defense analysis

All visual outputs are saved in the `images/` directory.

## 🧠 Key Insights
- Pokémon stats show significant variability, especially in offensive attributes
- Legendary Pokémon consistently outperform non-Legendary Pokémon
- Different Pokémon types specialize in speed, attack, or defense
- No clear power inflation across generations
- Balanced Pokémon with high offense and defense are rare but extremely powerful

## 🛠 Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn


## 👤 Author
Rejim Oli

---

## 📎 Notes
This project focuses on data exploration and insight generation. No machine learning models were applied.
