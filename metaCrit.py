#! python3
# metaCrit.py - Goes to movies page on metacritic, and prints score from page one to screen.
# There's four keywords: Movies, Games, TV, or Music
# The user inputs which category they would like to get scores from and prints to screen.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Sets headless option for Firefox and launches webdriver instance
options = Options()
options.headless = True
url = webdriver.Firefox(options=options, executable_path=r'C:\Utilities\geckodriver.exe')

categorie = input('What category would you like scores for?\n'
                  'Movies, Games, TV, or Music\n')
if categorie == 'Movies':
    url.get("https://www.metacritic.com/browse/movies/release-date/theaters/metascore")
    # Finds score for positive movie
    element = url.find_elements(By.XPATH, "//div[@class='metascore_w large movie positive']")
    vidTitle = url.find_elements(By.XPATH, "//a[@class='title']")
    s = []
    t = []
    for score in element:
        s.append(score.text)

    for title in vidTitle:
        t.append(title.text)

    str_list = list(filter(None, s))

    for i in range(len(t)):
        print('%s: %s metascore.' % (t[i], str_list[i]))

if categorie == 'Games':
    url.get("https://www.metacritic.com/game")
    element = url.find_elements(By.XPATH, "//div[@class='metascore_w large game positive']")
    gameTitle = url.find_elements(By.XPATH, "//a[@class='title']")
    s = []
    t = []
    for score in element:
        s.append(score.text)

    for title in gameTitle:
        t.append(title.text)

    str_list = list(filter(None, s))

    for i in range(len(t)):
        print('%s: %s metascore.' % (t[i], str_list[i]))

if categorie == 'TV':
    url.get("https://www.metacritic.com/tv")
    element = url.find_elements(By.XPATH, "//div[@class='metascore_w large season positive']")
    tvTitle = url.find_elements(By.XPATH, "//a[@class='title']")
    s = []
    t = []
    for score in element:
        s.append(score.text)

    for title in tvTitle:
        t.append(title.text)

    str_list = list(filter(None, s))

    for i in range(len(t)):
        print('%s: %s metascore.' % (t[i], str_list[i]))

if categorie == 'Music':
    url.get("https://www.metacritic.com/music")
    element = url.find_elements(By.XPATH, "//div[@class='metascore_w large release positive' or "
                                          "@class='metascore_w large release positive perfect']")
    album = url.find_elements(By.XPATH, "//a[@class='title']")
    s = []
    t = []
    for score in element:
        s.append(score.text)

    for title in album:
        t.append(title.text)

    str_list = list(filter(None, s))

    for i in range(len(t)):
        print('%s: %s metascore.' % (t[i], str_list[i]))

url.close()
ex = input('When you are done type exit.\n')
if ex == 'exit':
    sys.exit()
