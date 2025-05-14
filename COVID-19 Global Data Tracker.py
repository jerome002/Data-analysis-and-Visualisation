import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
#Data Loading & Exploration
# Load the dataset
df = pd.read_csv("owid-covid-data.csv")

# View columns
print(df.columns)

# Preview first 5 rows
df.head()

# Check missing values
df.isnull().sum()
#Data cleaning
# Filter relevant countries
countries = ['Kenya', 'Uganda', '   Tanzania' ]
df = df[df['location'].isin(countries)]

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'])

# Handle missing numeric values
df.fillna(0, inplace=True)

# Keep relevant columns
df = df[['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_vaccinations', 'people_vaccinated_per_hundred']]

#Exploratory Data Analysis (EDA)
#Total Cases Over Time

plt.figure(figsize=(12,6))
for country in countries:
    subset = df[df['location'] == country]
    plt.plot(subset['date'], subset['total_cases'], label=country)

plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
#Total Deaths Over Time
plt.figure(figsize=(12,6))
for country in countries:
    subset = df[df['location'] == country]
    plt.plot(subset['date'], subset['total_deaths'], label=country)

plt.title("Total Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
#Daily New Cases Comparison
plt.figure(figsize=(12,6))
for country in countries:
    subset = df[df['location'] == country]
    plt.plot(subset['date'], subset['new_cases'], label=country)

plt.title("Daily New COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
#Death Rate Calculation
df['death_rate'] = df['total_deaths'] / df['total_cases']
death_rate_latest = df[df['date'] == df['date'].max()][['location', 'death_rate']]
print(death_rate_latest)
#Visualizing Vaccination Progress
#Cumulative Vaccinations Over Time
plt.figure(figsize=(12,6))
for country in countries:
    subset = df[df['location'] == country]
    plt.plot(subset['date'], subset['total_vaccinations'], label=country)

plt.title("Total Vaccinations Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
#People Vaccinated per Hundred
latest = df[df['date'] == df['date'].max()]
sns.barplot(data=latest, x='location', y='people_vaccinated_per_hundred')
plt.title("People Vaccinated per 100 (Latest)")
plt.ylabel("Vaccinated per 100 People")
plt.xlabel("Country")
plt.grid(True)
plt.show()
#Choropleth Map (Plotly)


latest = pd.read_csv("owid-covid-data.csv")
latest = latest[latest['date'] == latest['date'].max()]
latest = latest[latest['iso_code'].str.len() == 3]  # Exclude continents/global

fig = px.choropleth(latest,
                    locations="iso_code",
                    color="total_cases",
                    hover_name="location",
                    color_continuous_scale="Reds",
                    title="Global COVID-19 Total Cases (Latest)")
fig.show()
