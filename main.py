# main.py
# William Ponton
# 6.2.19
# Main file for the Restaurant Inspection Analysis Project

# Constants

# Import modules
import scraper.rest_inspection_scraper as ris

# Function definitions

# Main function
def main():
    
    # Restaurant Inspections - Duval County
    # Attempting with one county at first - plan to implement a zip code search 
    url =  "https://data.tallahassee.com/restaurant-inspections/duval/list/"
    
    # Make the soup!
    soup = ris.make_soup(url)
    
    return 0

# Control Initiating event
if __name__ == "__main__":
    main()
    
    