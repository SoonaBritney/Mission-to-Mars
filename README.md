# Mission-to-Mars


https://github.com/SoonaBritney/Mission-to-Mars



## 1. Objectives

By the end of this module, we will be able to:

Gain familiarity with and use HTML elements, as well as class and id attributes, to identify content for web scraping.
Use BeautifulSoup and Splinter to automate a web browser and perform a web scrape.
Create a MongoDB database to store data from the web scrape.
Create a web application with Flask to display the data from the web scrape.
Create an HTML/CSS portfolio to showcase projects.
Use Bootstrap components to polish and customize the portfolio.

- Data Source: NASA news website, Mars Hemispheres website, getbootstrap website
- Software: BeautifulSoup, Splinter, MongoDB, Flask, Python, Jupyter notebook

![scrapping tools & data flow](https://github.com/SoonaBritney/Mission-to-Mars/blob/main/scrapping_tools.png)

## 2. Summary
In this module, we automated a web browser to visit the NASA news website and the Mars Hemispheres website to extract data about the Mission to Mars in index.html. We stored it in a Mongo DB, NoSQL database in scraping.py, and then render the data in a web application created with Flask in app.py.

(1). Deliverable 1: Scrape Full-Resolution Mars Hemisphere Images and Titles
In this chellenge, using BeautifulSoup and Splinter, I scraped full-resolution images of Mars’s hemispheres and the titles of those images.

(2). Deliverable 2: Update the Web App with Mars Hemisphere Images and Titles
Using the Python and HTML skills, I added the code you created in Deliverable 1 to your scraping.py file, update your Mongo database, and modify your index.html file so the webpage contains all the information you collected in this module as well as the full-resolution image and title for each hemisphere image.

(3). Deliverable 3: Add Bootstrap 3 Components
For this part of the Challenge, I updated the web app to make it mobile-responsive, and add two additional Bootstrap 3 components to make it stand out.


## 3.Results:
To run the code, we need to install many components prior to the scrapping.
- Mango DB
- pip install html5lib
- pip install lxml
- pip install numpy 
- python -m pip install pymongo
- pip install flask
- pip install splinter

1). Deliverable 1: 
[Mission_to_Mars_Challenge.ipynb](https://github.com/SoonaBritney/Mission-to-Mars/blob/main/Mission_to_Mars_Challenge.ipynb)

- full resolution image and title for each each hemisphere image
![screenshot - title and images](https://github.com/SoonaBritney/Mission-to-Mars/blob/main/Capture_hemisphere_image_title_path.PNG) 

2). Deliverable 2: 
scraping.py
index.html
app.py
-Step 0: After the  connect to Mongo DB, 
-Step 1: On the visual studio, run the code
- ![commnad line](https://github.com/SoonaBritney/Mission-to-Mars/blob/main/Capture_commandline_VS.PNG) 

-Step2: The scrapping is successfuly done on the local host
- ![scrape sucessful](https://github.com/SoonaBritney/Mission-to-Mars/blob/main/Capture_scrapping_successful.PNG)

- Step3: Now the screen shows the scrapped web site
- ![screen1](https://github.com/SoonaBritney/Mission-to-Mars/blob/main/Capture_scrapped_result3.PNG)
- ![screen2](https://github.com/SoonaBritney/Mission-to-Mars/blob/main/Capture_scrapped_result4.PNG)

- Step3: If you see the mango DB, you can see the DB size is also increaed with the scrapped content data
- ![After scrap - Mango DB size is increased](https://github.com/SoonaBritney/Mission-to-Mars/blob/main/Capture_mongo_scrapped3.PNG)


3). Deliverable 3: 
index.html
- The page is using the bootstrap css style and it is responsive for mobile app.
- ![bootstrap view](https://github.com/SoonaBritney/Mission-to-Mars/blob/main/Capture_scrapped_result5.PNG) 
- ![mobile app responsive view](https://github.com/SoonaBritney/Mission-to-Mars/blob/main/Capture_scrapped_responsive.PNG) 

We added the bootstrap Bootstrap grid examples to be responsive for mobile ipad display.

## 4.Conclusion
Web scraping is very powerful method to scrap the content and recreate a web site & pages dynamically. BeautifulSoup and Splinter are very helpful tool  as well as Chrome dev tool. To do this, we use BeautifulSoup and Splinter to scrape full-resolution images of Mars’s hemispheres and the titles of those images, store the scraped data on a Mongo database, use a web application to display the data, and alter the design of the web app to accommodate these images.



