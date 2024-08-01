# use a stack to get rid of the duplicate chapters you can push when they come up and pop when they come up the
# second time

import httpx
from bs4 import BeautifulSoup

parent_Site = "https://asuracomic.net/series/"

"""Returns a list of links containing the pages for the updated manhua"""
def get_page():  # gets all individual pages and partial names for update page on Manhuas
    titles = []
    # names_and_links = {}
    site = httpx.get("https://asuracomic.net/")
    site_text = BeautifulSoup(site.text, 'html.parser')

    text = site_text.find_all('span', class_="text-[15px] font-medium hover:text-themecolor hover:cursor-pointer")
    links = []

    for i in range(len(text)):
        links.append("https://asuracomic.net" + str(text[i].find('a')['href']))
        titles.append(text[i].find('a').text)

    # Returns a list of the names and links of the updated page
    return links
"""Takes a list of links and returns a dictionary with the links Manhua name as the key and the all chapter links a"""
def get_chapter(links):  # get individual chapters and returns them into a dictionary
    # print(links)
    final = {}
    for k in range(len(links)):
        mh_Request = httpx.get(links[k])
        print(links[k])
        mh_text = BeautifulSoup(mh_Request.text, 'html.parser')
        name = mh_text.find_all('span', class_="text-xl font-bold  ")# maybe no space at end
        print(name)
        text = mh_text.find_all('h3', class_="text-sm text-white font-medium group-hover:text-themecolor")
        chapters = []
        for chaps in text:
            chapters.append(parent_Site + chaps.find('a')['href'])
        final[name] = chapters
    # print(final)
    return final


class AsuraAPI:
    names_and_links = {}
    titles = []

    chapter_Links = []
    final = {}
