

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("netflix.csv")

# Drop rows with missing important values
df = df.dropna(subset=['type', 'release_year', 'rating', 'country', 'duration'])

# ---------------- Bar Chart: TV Shows vs Movies ----------------
type_count = df['type'].value_counts()

plt.figure(figsize=(6, 4))
plt.bar(type_count.index, type_count.values, color=['skyblue', 'pink'])

plt.title('TV vs Movies Watchers on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('tv_vs_movies_watchers.png', dpi=1000)
plt.show()

# ---------------- Pie Chart: Content Ratings ----------------
rating_count = df['rating'].value_counts()

plt.figure(figsize=(10, 5))
plt.pie(rating_count, labels=rating_count.index, autopct='%1.1f%%', startangle=90)

plt.title('Percentage of Content Ratings')
plt.tight_layout()
plt.savefig('content_rating.png', dpi=1000)
plt.show()

# ---------------- Histogram: Movie Duration ----------------
movie_df = df[df['type'] == 'Movie'].copy()

# Convert 'duration' to numeric minutes
movie_df['duration_int'] = movie_df['duration'].str.replace(' min', '').astype(int)

plt.figure(figsize=(8, 5))
plt.hist(movie_df['duration_int'], bins=30, color='orange', edgecolor='black')

plt.title('Distribution of Movie Durations')
plt.xlabel('Duration (minutes)')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('movie_duration_histogram.png', dpi=1000)
plt.show()

#release yea vs no. of shows plot diagram
release_count = df['release_year'].value_counts()

plt.figure(figsize=(10, 6))
plt.scatter(release_count.index, release_count.values, color=['red'])

plt.title('Release year vs Number of shows')
plt.xlabel('Number of shows')
plt.ylabel('Release year')
plt.tight_layout()
plt.savefig('Release_year_scatter.png', dpi=1000)
plt.show()

#top 10 countries 
country_count= df['country'].value_counts().head(10)

plt.figure(figsize=(8, 6))
plt.barh(country_count.index, country_count.values, color=['blue'])

plt.title('Top 10 countries')
plt.xlabel('Number of shows')
plt.ylabel('country')
plt.tight_layout()
plt.savefig('Top10_countrys.png', dpi=1000)
plt.show()

# Grouping and preparing data
content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)

# Fix column names if needed (optional safeguard)
content_by_year.columns = [col.strip().title() for col in content_by_year.columns]

# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# First subplot: Movies
ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue')
ax[0].set_title('Movies Released per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('No. of Movies')

# Second subplot: TV Shows
ax[1].plot(content_by_year.index, content_by_year['Tv Show'], color='green')
ax[1].set_title('TV Shows Released per Year')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('No. of TV Shows')

# Add overall title
fig.suptitle("Comparison of TV Shows and Movies Released per Year")

# Layout and save
plt.tight_layout(rect=[0, 0, 1, 0.95])  # leave space for suptitle
plt.savefig("movies_vs_tvshows_comparison.png", dpi=300)
plt.show()
