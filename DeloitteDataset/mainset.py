import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel('del_winners.xlsx')

# convert values in "GROWTH" column to numeric
df["GROWTH"] = pd.to_numeric(df["GROWTH"], errors='coerce')


print(df.head())


mean_growth = df["GROWTH"].mean()
print("Mean growth rate: {:.2f}%".format(mean_growth))

# find the company with the highest growth rate
max_growth = df["GROWTH"].max()
max_growth_company = df.loc[df["GROWTH"] == max_growth, "COMPANY NAME"].values[0]
print("Company with highest growth rate: {}".format(max_growth_company))

# count the number of companies in each industry
industry_counts = df["PRIMARY INDUSTRY"].value_counts()
print("Number of companies in each industry:\n{}".format(industry_counts))

# create a bar chart of the number of companies in each industry
plt.figure(figsize=(8,6))
sns.set_style("whitegrid")
sns.countplot(x="PRIMARY INDUSTRY", data=df, palette="rocket")
plt.title("Number of Companies in Each Industry")
plt.xlabel("Industry")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.savefig("barChartNumberofCompanies.png")
# create a histogram of the distribution of growth rates
plt.figure(figsize=(8,6))
sns.set_style("whitegrid")
sns.histplot(data=df, x="GROWTH", bins=20, kde=True, color="darkorange")
plt.title("Distribution of Growth Rates")
plt.xlabel("Growth Rate (%)")
plt.ylabel("Count")
plt.savefig("growthRates.png")

# create a box plot of growth by industry
plt.figure(figsize=(8,6))
sns.set_style("whitegrid")
sns.boxplot(x="PRIMARY INDUSTRY", y="GROWTH", data=df, palette="rocket")
plt.title("Growth by Industry")
plt.xlabel("Industry")
plt.ylabel("Growth Rate (%)")
plt.xticks(rotation=45)
plt.savefig("boxPlotGrowthIndustry.png")


# create a heatmap of the correlation matrix
corr = df.corr()
plt.figure(figsize=(8,6))
sns.set_style("whitegrid")
sns.heatmap(corr, annot=True, cmap="rocket")
plt.title("Correlation Matrix")
plt.savefig("correlationMatrix.png")