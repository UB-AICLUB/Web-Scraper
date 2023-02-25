# Author: Shail Rajesh Shah
# created for : UB AI Club
# Description: Web scraper basic example script using beautiful soup 4 


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup # install via -> pip install bs4


class SearchNewEgg():
    def __init__(self):
        self.searchbox = input("Enter product name: ") # take input 

    def load_data(self):

        print('searching...')
        print('')

        # cleaning inputfor url
        searchbox_input = self.searchbox.replace(' ', '+').strip()
        # making url for request
        my_url = "https://www.newegg.com/global/in-en/p/pl?d=" + searchbox_input

        # connecting to server and grab the html
        uClient = uReq(my_url)
        page = uClient.read()
        uClient.close()

        # using bs4 to parse html and get required values
        # parsing is reading and extracting information from some form of structured / semi-structured data
        page_soup = soup(page, "html.parser")

        # analyze the html to find patterns of specific html elements 
        cards = page_soup.findAll("div", {"class", "item-cell"})

        # loop over elements to get the data you need
        for card in cards:
            # try and except to catch any errors
            try:
                # storing info from specific paths 
                prod_link = card.a.get("href")
                prod_im = card.a.img.get("src")
                prod_details = card.findAll('a', {"class", "item-title"})[0].text
                # display info scrapped
                print("link: "+prod_link)
                print("img_src: "+prod_im)
                print("details: "+prod_details)
                print("")

            except Exception as e:
                print(e)
                print('')

        print('')
        print("END")

# driver code
if __name__ == '__main__':
    s = SearchNewEgg()
    s.load_data()


