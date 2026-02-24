import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_html(url):
    """Fetches the raw HTML content of a page."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # Check if the request was successful
        return response.text
    except Exception as e:
        return f"Error: {e}"

def parse_content(html, tag="p"):
    """Extracts specific tags from HTML and returns a list of strings."""
    if "Error" in html:
        return []
    
    soup = BeautifulSoup(html, 'lxml')
    # If user wants headings, we check for h1, h2, and h3
    if tag == "headings":
        elements = soup.find_all(['h1', 'h2', 'h3'])
    else:
        elements = soup.find_all(tag)
        
    return [el.get_text().strip() for el in elements if el.get_text().strip()]