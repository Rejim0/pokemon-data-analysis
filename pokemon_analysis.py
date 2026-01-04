import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# 🔹 STAGE 1 — Data Understanding
df_pokemon = pd.read_csv("PokemonData.csv")
print("First five rows: \n",df_pokemon.head().to_string())
print("\nLast five rows: \n",df_pokemon.tail().to_string())
print("\nShape of DATASET: \n",df_pokemon.shape)
print("\nInfo of Dataset: ")
print(df_pokemon.info())
numerical_columns = df_pokemon.select_dtypes(include = "number")
print("\nNumerical columns: \n",list(numerical_columns))
categorical_columns = df_pokemon.select_dtypes(include = "object")
print("Object columns: \n",list(categorical_columns))
print("\nChecking missing values: \n",df_pokemon.isna().sum())
print("\nDuplicates Rows count: ",df_pokemon.duplicated().sum())
print("\nStats of Dataset: \n",df_pokemon.describe().to_string())
print("\nPokemon Counts: ",df_pokemon["Name"].nunique())
print("\nType 1 of pokemon: ",list(df_pokemon["Type1"].unique()))
print("\nPossible Legendary: ",list(df_pokemon["Legendary"].unique()))

# 🔹 STAGE 2 — Data Cleaning
df_pokemon = df_pokemon.fillna({"Type2":"No Type 2"})

object_cols = ["Name","Type1","Type2"]
for cols in object_cols:
    df_pokemon[cols] = df_pokemon[cols].str.lower().str.strip()
print(df_pokemon.head())

# 🔹 STAGE 3 — Analysis Questions

# How are Pokémon stats distributed?
stats = ["HP","Attack","Defense", "SpAtk", "SpDef","Speed","Generation"]
df_pokemon[stats].hist(bins = 10,figsize = (6,8))
plt.tight_layout()
plt.savefig("Pokemon_stats.png")
plt.show()
# Which stats vary the most?
print("\nStats Vary most: \n",df_pokemon[stats].std().sort_values(ascending= False))

# 2️⃣ Legendary vs Non-Legendary comparison
print(df_pokemon.groupby("Legendary")[stats].mean().to_string())
df_pokemon.boxplot(column = stats, by = "Legendary", figsize=(9,6))
plt.suptitle("")
plt.savefig("Legendary vs Non_Legendary.png")
plt.show()

# 3️⃣ Type-based analysis
# Which Pokémon types are fastest?
pokemon_type = df_pokemon.groupby("Type1")["Speed"].mean().idxmax()
print("\nFastest Pokemon type: ",pokemon_type)

# Which types have the highest attack or defense?
pokemon_type = df_pokemon.groupby("Type1")["Attack"].mean().idxmax()
print("Highest Attack Pokemon type: ",pokemon_type)
pokemon_type = df_pokemon.groupby("Type1")["Defense"].mean().idxmax()
print("Highest Defense Pokemon type: ",pokemon_type)

# 📊 Groupby + bar charts
pokemon_SpeedType = df_pokemon.groupby("Type1")["Speed"].mean()
plt.barh(pokemon_SpeedType.index,pokemon_SpeedType.values,color = "green",edgecolor="black")
plt.title("Pokemon Types with speed")
plt.xlabel("Speed")
plt.ylabel("Pokemon Names")
plt.tight_layout()
plt.savefig("Pokemon Types W speed.png")
plt.show()

# 4️⃣ Generation trends
# Do Pokémon get stronger across generations?
pokemon_generationGroup = df_pokemon.groupby("Generation")["Attack"].mean()
print("\nAverage Attack power across generation: \n",pokemon_generationGroup)
plt.plot(pokemon_generationGroup,marker="*",mfc="cyan",mec="blue",color="blue")
plt.title("Generation with Attack")
plt.xlabel("Generation")
plt.ylabel("Attack Stats")
plt.savefig("Generation W attack.png")
plt.show()

# How has average total stats changed over time?
stats_Generation = ["HP","Attack","Defense","SpAtk","SpDef","Speed"]
average_statsGeneration = df_pokemon.groupby("Generation")[stats_Generation].mean()
print("\nAverage total stats changed over time: \n",average_statsGeneration)
average_statsGeneration.plot(marker="o",figsize=(10,6))
plt.savefig("Average Stats over time.png")
plt.show()

# 5️⃣ Correlation analysis
# Which stats are strongly related?
# Is Speed related to Attack?
# Is Defense related to HP?
# 📊 Heatmaps (Seaborn)
correlation = df_pokemon[stats_Generation].corr()
print("\nCorrelation analysis: \n",correlation)
sb.heatmap(correlation, annot = True, cmap = "Blues", fmt =".2f",linewidths=0.5)
plt.savefig("Stats Correlation.png")
plt.show()

# 6️⃣ Custom metrics
df_pokemon["Offense Score"] = df_pokemon["Attack"] + df_pokemon["SpAtk"]
df_pokemon["Defense Score"] = df_pokemon["Defense"] + df_pokemon["SpDef"]
df_pokemon["Balanced Score"] = df_pokemon["Offense Score"] + df_pokemon["Defense Score"]

best_offensivepokemon = df_pokemon["Offense Score"].idxmax()
print("\nBest Offensive Pokemon: \n",df_pokemon.iloc[best_offensivepokemon])

best_defensivepokemon = df_pokemon["Defense Score"].idxmax()
print("\nBest Defensive Pokemon: \n",df_pokemon.iloc[best_defensivepokemon])

Balanced_pokemon = df_pokemon["Balanced Score"].idxmax()
print("\nBalanced Pokemon: \n",df_pokemon.iloc[Balanced_pokemon])


#Bar chart — Top offensive Pokemon
offensive = df_pokemon.sort_values("Offense Score", ascending = False).head(10)
plt.figure(figsize = (10,5))
plt.barh(offensive["Name"], offensive["Offense Score"])
plt.xlabel("Offense Score")
plt.ylabel("Pokémon")
plt.title("Top 10 Offensive Pokémon")
plt.tight_layout()
plt.gca().invert_yaxis()
plt.savefig("Top 10 offensive Pokemon.png")
plt.show()

#Bar chart — Top Defensive Pokemon
defensive = df_pokemon.sort_values("Defense Score", ascending = False).head(10)
plt.figure(figsize = (10,5))
plt.barh(defensive["Name"], defensive["Defense Score"])
plt.xlabel("Defense Score")
plt.ylabel("Pokémon")
plt.title("Top 10 defensive Pokémon")
plt.tight_layout()
plt.gca().invert_yaxis()
plt.savefig("Top 10 defensive Pokemon.png")
plt.show()

#Scatter plot — Offense vs Defense
plt.figure(figsize=(7,6))
plt.scatter(df_pokemon["Offense Score"], df_pokemon["Defense Score"], alpha=0.6)
plt.xlabel("Offense Score")
plt.ylabel("Defense Score")
plt.title("Offense vs Defense Distribution of Pokémon")
plt.savefig("Offense vs Defense.png")
plt.show()

