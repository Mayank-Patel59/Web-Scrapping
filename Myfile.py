import urllib
import  csv
from bs4 import BeautifulSoup
from urllib.request import urlopen

print('Enter Movie Name that you want to Search: ');
input1 = input()

quote_page = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

page = urllib.request.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

rating_box = soup.findAll('td', attrs={'class': 'ratingColumn imdbRating'})
name_box = soup.findAll('td', attrs={'class': 'titleColumn'})

for val in range (0, 249):
    name = name_box[val].text.strip()
    #print(name);

    rating = rating_box[val].text.strip()
    #print(rating);

    if(input1 in name):
        print('Rating For '+ name + ' is: ' +rating)

    with open('index.csv', 'a') as csv_file:
        writer  = csv.writer(csv_file)
        writer.writerow([name, rating])
