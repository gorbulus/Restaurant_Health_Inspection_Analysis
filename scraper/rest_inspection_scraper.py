# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 10:15:09 2019

@author: gorbulus
"""

### Scraping Example =======================================================
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://boston.craigslist.org/search/npo"

# Create a dictionary
dict = { "key" : "value"}
print(dict)

# Update the dictionary
dict["new key"] = "new value"
print(dict)

npo_jobs = {}
job_no = 0
while True:
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    jobs = soup.find_all("p",{"class":"result-info"})
    for job in jobs:
        title = job.find("a", {"class":"result-title"}).text
        location_tag = job.find("span", {"class":"result-hood"})
        location = location_tag.text[1:-1] if location_tag else "N/A"
        date = job.find("time", {"class":"result-date"}).text
        link = job.find("a", {"class":"result-title"}).get("href")
        
        job_response = requests.get(link)
        job_data = job_response.text
        job_soup = BeautifulSoup(job_data, "html.parser")
        job_description = job_soup.find("section", {"id":"postingbody"}).text
        job_attributes_tag = job_soup.find("p", {"class":"attrgroup"})
        job_attributes = job_attributes_tag.text if job_attributes_tag else "n/A"
        
        job_no += 1
        npo_jobs[job_no] = [title, location, date, link, job_attributes, job_description]


        
        print("Job Title: ", title, "\nLocation:", location, "\nDate:", date, "\nLink", link, "\nJob Attributes:", job_attributes, "\nJob Description:", job_description)
        
        url_tag = soup.find("a", {"title":"next page"})
        if url_tag.get("href"):
            url= "https://boston.craigslist.org" + url_tag.get("href")
            print(url)
        else:
            break

        print("Total Jobs:", job_no)
        
        # Use Pandas to convert the dictionary to a datafram
        npo_jobs_df = pd.DataFrame.from_dict(npo_jobs, orient = "index", columns = ["Job Title", "Location", "Date", "Link", "Job Attributes", "Job Description"])
        
        # Save the DataFrame to a csv file
        npo_jobs_df.to_csv("npo_jobs.csv")
        
### RIHA Project =====================================================
# Import modules
import csv
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

# Turn in to function

# Some variable for display examples
rest_report = ""
restaurant = ""

with open('project_rhia.csv', 'w', newline='') as csvfile:
    rest_writer = csv.writer(csvfile, delimiter=",")
    rest_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    rest_riter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

# Find all tr rows
for record in soup.findAll("tr"):
	# Print every table row
    rest_report = rest_report + "," + record.text
    

# Find all data for each tr record
for data in record.findAll("td"):
	# Print all cell data
	restaurant = restaurant + "," + data.text
	print(restaurant)

