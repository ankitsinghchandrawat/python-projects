import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

# Function to perform Google search using Selenium and get HTML content
def get_google_search_results(query):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    html = driver.page_source
    driver.quit()
    return html

# Function to parse the HTML content and extract search results
def parse_search_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('div', class_='g')
    search_results = []
    for result in results:
        title = result.find('h3').text if result.find('h3') else 'No title'
        link = result.find('a')['href']
        description = result.find('span', class_='aCOpRe').text if result.find('span', class_='aCOpRe') else 'No description'
        search_results.append({'title': title, 'link': link, 'description': description})
    return search_results

# Main function to execute the search and print results
def main():
    query = input("Enter your search query: ")
    html = get_google_search_results(query)
    search_results = parse_search_results(html)
    
    # Print results
    for result in search_results:
        print(f"Title: {result['title']}\nLink: {result['link']}\nDescription: {result['description']}\n")
    
    # Save results to CSV
    with open('search_results.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Link', 'Description'])
        for result in search_results:
            writer.writerow([result['title'], result['link'], result['description']])

if __name__ == "__main__":
    main()
