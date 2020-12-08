#!/usr/bin/env python
# coding: utf-8

# In[29]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd


# Import Dependencies
import os
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser


# In[30]:


# Path to chromedriver
get_ipython().system('which chromedriver')


# In[31]:


# Set the executable path and initialize the chrome browser in splinter
#executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
executable_path = {'executable_path': 'C:/Users/2018b/.wdm/drivers/chromedriver/win32/87.0.4280.88/chromedriver'}
browser = Browser('chrome', **executable_path)


# ### Visit the NASA Mars News Site

# In[32]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[33]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[34]:


slide_elem.find("div", class_='content_title')


# In[35]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[36]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### JPL Space Images Featured Image

# In[37]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[38]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[39]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# In[40]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[41]:


# find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[42]:


# Use the base url to create an absolute url
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# ### Mars Facts

# In[43]:


df = pd.read_html('http://space-facts.com/mars/')[0]

df.head()


# In[44]:


df.columns=['Description', 'Mars']
df.set_index('Description', inplace=True)
df


# In[45]:


df.to_html()


# ### Mars Weather

# In[46]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[47]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[48]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[58]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[59]:


# 1. Use browser to visit the URL 

USGS_url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
short_url="https://astrogeology.usgs.gov"


# In[60]:


browser.visit(USGS_url)
html = browser.html
img_soup = soup(html, 'html.parser')
main_url = img_soup.find_all('div', class_='item')
titles=[]

# 2. Create a list to hold the images 
hemisphere_img_urls=[]


# In[61]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.
for x in main_url:
    title = x.find('h3').text
    url = x.find('a')['href']
    hem_img_url= short_url+url
    #hem_img_url= short_url
    
    #print(hem_img_url)
    browser.visit(hem_img_url)
    html = browser.html
    #soup = bs(html, 'html.parser')
    img_soup = soup(html, 'html.parser')
    hemisphere_img_original= img_soup.find('div',class_='downloads')
    hemisphere_img_url=hemisphere_img_original.find('a')['href']
    
    print(hemisphere_img_url)
    img_data=dict({'title':title, 'img_url':hemisphere_img_url})
    hemisphere_img_urls.append(img_data)


# In[62]:


# 4. Print the list that holds the dictionary of each image url and title.

hemisphere_img_urls


# In[ ]:


# 5. Quit the browser
browser.quit()


# In[ ]:




