# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 10:15:09 2019

@author: gorbulus
"""

# Import modules
import urllib
import urllib.request
from bs4 import BeautifulSoup

'''
Input: url to a site with html.
1. Opens the url request for use.
2. Passes the url to the BS constructor, add the html.parser parser.
3. Returns the 'soup' or the raw html of the url.
'''

# Restaurant Inspections - Duval County
    # Attempting with one county at first - plan to implement a zip code search 
    url =  "https://data.tallahassee.com/restaurant-inspections/duval/list/"
    
# make_soup
def make_soup(url):
	the_page = urllib.request.urlopen(url)
	soup_data = BeautifulSoup(the_page, "html.parser")
	return soup_data

# Make the soup!
soup = make_soup(url)

# Some variable for display examples
restaurant = ""

# TODO - turn in to a function once the site is known
# (Too many examples here to nail to one function just now)
for record in soup.findAll("tr"):
	# Print every table row
	print(record.text)


# Commented out for Hoshi and True - Works with the Health Dept Page
for data in record.findAll("td"):
	# Print all cell data
	restaurant = restaurant +","+ data.text
	print(restaurant)
