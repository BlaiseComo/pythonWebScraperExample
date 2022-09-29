from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

##### !!!!! This code no longer works with the website or for some other reason so take caution when referencing it !!!!!! ######

# You can also import request and use those methods to pull data from the internet

my_url = 'https://www.newegg.com/p/pl?d=graphics+cards'

# This handy piece of code downloads the web page from my_url 
uClient = uReq(my_url)

# Saves the html file as page_html
page_html = uClient.read()

uClient.close()

# This parses page_html
page_soup = BeautifulSoup(page_html, "html.parser")

# Grabs all data in each container, this is sort of like a list, you can call len on it to see how many item-containers it found
# This would be a good spot to use regex and a for loop to try and catch common classes
containers = page_soup.findAll("div", {"class":"item-container"})

