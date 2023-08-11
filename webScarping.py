# Project: Automated Web Scraping and Data Visualization
"""
Description: This project automates the process of scraping data from a website, processing it, and creating visualizations to gain insights. It uses web scraping libraries to extract data from web pages and visualization libraries to create charts and graphs.

Steps:

Install necessary libraries such as requests, beautifulsoup4, and matplotlib.
Write a Python script that uses web scraping to extract data from a specific webpage.
Process and analyze the extracted data to generate insights.
Use data visualization libraries to create visual representations of the insights.
Requirements:

Python (installed on your system)
Knowledge of web scraping techniques, data manipulation, and data visualization.
Example Code (Scraping Top Movies from IMDb and Creating a Bar Chart):
"""
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def scrape_top_movies(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = []
    for movie in soup.select('.lister-item-content'):
        title = movie.h3.a.text
        rating = float(movie.select_one('.ratings-imdb-rating strong').text)
        movies.append({'title': title, 'rating': rating})

    return movies

def create_bar_chart(movies):
    titles = [movie['title'] for movie in movies]
    ratings = [movie['rating'] for movie in movies]

    plt.figure(figsize=(10, 6))
    plt.barh(titles, ratings, color='skyblue')
    plt.xlabel('IMDb Rating')
    plt.title('Top Rated Movies on IMDb')
    plt.gca().invert_yaxis()
    plt.show()

if __name__ == "__main__":
    imdb_url = "https://www.imdb.com/chart/top"
    
    top_movies = scrape_top_movies(imdb_url)
    create_bar_chart(top_movies)