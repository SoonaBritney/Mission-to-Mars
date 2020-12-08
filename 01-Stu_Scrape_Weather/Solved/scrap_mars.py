from flask import Flask, render_template
import pymongo
from splinter import Browser
from bs4 import BeautifulSoup
import os
import platform
import pdb
import requests
import time
import pandas as pd

def init_browser():
    return Browser('chrome')


def scrape():
    content = {}
    browser = init_browser()

    # Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. 
    # Assign the text to variables that you can reference later.
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    content["news_title"] = soup.find("div", class_="content_title").text
    content["news_body"] = soup.find("div", class_="article_teaser_body").text


    # JPL Mars Space Images - Featured Image
    # Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    base_url = "https://www.jpl.nasa.gov"
    search_url = soup.find("a", class_="button")["data-link"]
    link = base_url + search_url
    browser.visit(link)
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image_url = soup.find('figure', class_="lede").a["href"]
    content["featured_image_url"] = base_url + image_url


    # * Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called `mars_weather`.
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    content["mars_weather"] = soup.find('p', class_="tweet-text").text


    # Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # Use Pandas to convert the data to a HTML table string.
    url = "http://space-facts.com/mars/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_facts = pd.read_html(url)[0]
    mars_facts.columns = ["Description", "Value","Earth"]
    mars_facts.set_index("Description", inplace = True)
    mars_facts.drop(columns=['Earth'])
    mars_facts_html = mars_facts.to_html(classes="table table-striped")
    content["mars_facts_html"]= mars_facts_html


    # Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of \
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    xpath = "//div[@class='description']//a[@class='itemLink product-item']/h3"
    results = browser.find_by_xpath(xpath)
    hemisphere_image_urls = []
    for i in range(4):
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        # find the new Splinter elements
        results = browser.find_by_xpath(xpath)
        # Save the name of the hemisphere
        header = results[i].html
        # Click on the header to go to the hemisphere details page 
        details_link = results[i]
        details_link.click()
        time.sleep(2)
        # Load hemisphere details page into Beautiful Soup
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        # Save the image url
        hemisphere_image_urls.append({"title": header, "image_url": soup.find("div", class_="downloads").a["href"]})
        # Go back to the original page
        browser.back()
        time.sleep(2)

    content["hemisphere_image_urls"] = hemisphere_image_urls
    browser.quit()
    return content

