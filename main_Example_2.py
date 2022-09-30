from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#### !!!! Important Documentation can be found in this link https://www.crummy.com/software/BeautifulSoup/bs4/doc/  !!!!! 

# Creates a request object that contains a plethora of data about the website in the parentheses
websiteObject = requests.get('https://www.crummy.com/software/BeautifulSoup/bs4/doc/')

# Prints the status of the website object, 200 means a success, 404 is an error
# Any status code between 200 and 400 mean some workable response was obtained
#print(websiteObject.status_code)
print()

# This will print all of the html content of the websiteObject
# print(websiteObject.content)

# This will give you vital info on the website 
#print(websiteObject.headers)

# This is an object that lets us perfrom many different functions on websiteObject
# html.parser essentially clarifies that the document is html code
soup = BeautifulSoup(websiteObject.content, "html.parser")

# This prints the document in a much more readable way
#print(soup.prettify())

chocolateRatings = soup.find_all('div')

ratings = []

for i in range(1, len(chocolateRatings)):
  ratingString = chocolateRatings[i].get_text()
  #print(ratingString)
  #print("\n\n\n")

#plt.hist(ratings)
plt.show()

chocolateCompanies = soup.find_all(attrs={"class": "Company"})

companies = []

for i in range(1, len(chocolateCompanies)):
  companies.append(chocolateCompanies[i].get_text())

dictionaryColumns = {"Company": companies, "Ratings": ratings}
newDataFrame = pd.DataFrame.from_dict(dictionaryColumns)

companyGroupBy = newDataFrame.groupby("Company").Ratings.mean()
ten_best = companyGroupBy.nlargest(10)



