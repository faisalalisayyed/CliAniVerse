from bs4 import BeautifulSoup
from webbrowser import open

from requests import get
from os import system
from platform import system as uname

from .select_anime import select_anime
from .history import history


def select_episode(name='', epi='', flag=0):

    if flag == 1:
        select_episode.select = select_anime(name=name, flag=1)
    else:
        select_episode.select = select_anime()

    print(
        f'Which Episode to Watch, \nEpisodes: (1-{select_episode.select[1]})')

    while True:
        if flag == 0:
            select_episode.episode_select = input("> ")
        else:
            select_episode.episode_select = epi

        try:
            if int(select_episode.episode_select) > int(select_episode.select[1]):
                print('sorry select in range....')
            else:
                break
        except ValueError:
            print('Sorry use a valid number with in the range')

    return select_episode.select[0], select_episode.select[1]


def search_episode(epi_no=0):
    select_episode.episode_select = int(select_episode.episode_select)+epi_no
    episode_url = f'https://gogoplay5.com/videos/{select_episode.select[0]}-{select_episode.episode_select}'
    req = get(episode_url).text
    doc = BeautifulSoup(req, 'html.parser')
    streaming_link = doc.iframe['src']
    history(select_episode.select[0], select_episode.episode_select)
    open_browser(streaming_link)
    return select_episode.episode_select


def open_browser(streaming_link):
    stream_link = streaming_link
    if uname() == 'Linux':
        system(f'xdg-open https:{stream_link}')
    else:
        open(f'https:{stream_link}')
