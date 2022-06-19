from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

websiteObject = requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')

soup = BeautifulSoup(websiteObject.content, "html.parser")

chocolateRatings = soup.find_all(attrs={"class": "Rating"})

ratings = []

for i in range(1, len(chocolateRatings)):
  ratingString = chocolateRatings[i].get_text()
  ratings.append(float(ratingString))

plt.hist(ratings)
plt.show()

chocolateCompanies = soup.find_all(attrs={"class": "Company"})

companies = []

for i in range(1, len(chocolateCompanies)):
  companies.append(chocolateCompanies[i].get_text())

dictionaryColumns = {"Company": companies, "Ratings": ratings}
newDataFrame = pd.DataFrame.from_dict(dictionaryColumns)

companyGroupBy = newDataFrame.groupby("Company").Ratings.mean()
ten_best = companyGroupBy.nlargest(10)



