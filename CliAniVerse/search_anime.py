from bs4 import BeautifulSoup

from requests import get
from os import system, uname


def search_anime(name='', flag=0):

    system('cls' if uname == 'nt' else 'clear')

    if flag == 0:
        search = input("Enter the anime name: ").replace(' ', '%20')
    elif flag == 2:
        search = name.replace(' ', '%20')
    else:
        search = input(
            "No result found try other anime name: ").replace(' ', '%20')

    url = f'https://gogoplay5.com/search.html?keyword={search}'
    req = get(url).content
    doc = BeautifulSoup(req, 'html.parser')

    search_anime.anime_name = {}

    for index, ani_name in enumerate(doc.find_all(class_='name')):
        tag = ani_name.get_text().strip()
        search_anime.anime_name[str(index+1)] = tag
        print(f'[{index+1}] {tag}')
    print(f'[q] quit')

    check_list()

    return search_anime.anime_name


def check_list():
    while True:
        if len(search_anime.anime_name) == 0:
            search_anime(flag=1)
        else:
            break
