
# Project: Website Health validator

# Description: This project automates the process of checking the health status of a list of websites. It sends HTTP requests to each website and determines if they are up and running by checking their status codes. The script then generates a report with the website names and their respective health statuses.

# Steps:

# Create a list of websites to be checked.
# Write a Python script that sends HTTP requests to each website and checks their status codes (e.g., 200 for success).
# Based on the status codes, determine if the website is up and running or experiencing issues.
# Generate a report displaying the health status of each website.
# Requirements:

# Python (installed on your system)
# Basic knowledge of making HTTP requests and handling responses in Python.
# Example Code:

# python
# Copy code
import requests

def check_website_health(websites):
    health_report = {}

    for website in websites:
        try:
            response = requests.get(website)
            if response.status_code == 200:
                health_report[website] = "Healthy"
            else:
                health_report[website] = "Unhealthy"
        except requests.exceptions.RequestException:
            health_report[website] = "Error - Unable to connect"

    return health_report

if __name__ == "__main__":
    websites_to_check = [
        "https://www.example.com",
        "https://www.google.com",
        "https://www.invalidwebsite1234.com"
    ]

    report = check_website_health(websites_to_check)

    print("Website Health Report:")
    for website, status in report.items():
        print(f"{website}: {status}")