import requests
import selectorlib
import os
import time
from datetime import datetime
import sqlite3


connection = sqlite3.connect("data.db")

URL = "http://programmer100.pythonanywhere.com/"


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    """Extract the selector"""
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperature"]
    return value


def store(extracted):
    """Stores the event in a SQLite database"""
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperatures VALUES(?,?)", (now, extracted))
    connection.commit()

if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)

    store(extracted)