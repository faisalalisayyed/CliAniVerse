from re import sub
from bs4 import BeautifulSoup
from requests import get
from webbrowser import open
from time import sleep
from os import system,name,uname

class anime():

    def search_anime(self):
        self.search = input("Enter the anime name: ").replace(' ', '%20')
        self.url = f'https://gogoplay5.com/search.html?keyword={self.search}'
        self.req = get(self.url).content
        self.doc = BeautifulSoup(self.req, 'html.parser')

    def list_anime(self):
        self.anime_name = {}
        for index, name in enumerate(self.doc.find_all(class_='name')):
            tag = name.get_text().strip()
            self.anime_name[str(index+1)] = tag
            print(f'[{index+1}]  {tag}')
        print(f'[q] quit')
        return self.anime_name

    def select_anime(self):
        self.anime_select = input("> ")
        if self.anime_select == 'q':
            exit()
        return self.anime_select

    def list_anime_episode_remove_special_char(self):
        self.anime_select = self.anime_name[self.anime_select].split()
        self.episode_no = self.anime_select.pop()
        self.anime_select = ' '.join(self.anime_select).lower()
        self.remove_special_char = sub('[^a-zA-Z0-9 \n\.]', '', self.anime_select).replace(' ', '-')

    def select_anime_episode(self):
        print(f'Which Episode to Watch, \nEpisodes: (1-{self.episode_no})')
        self.episode_select = input('> ')
        
        if int(self.episode_select) > int(self.episode_no):
            return True
        else:
            return False

    def search_episode(self,i = 0):
        self.episode_select = int(self.episode_select)+i
        self.episode_url = f'https://gogoplay5.com/videos/{self.remove_special_char}-{self.episode_select}'
        self.req = get(self.episode_url).text
        self.doc = BeautifulSoup(self.req, 'html.parser')
        self.streaming_link = self.doc.iframe['src']

    def open_browser(self):
        if uname()[4] == 'aarch64':
            system(f'xdg-open https:{self.streaming_link}')
        else:
            open(f'https:{self.streaming_link}')

    def anime_option(self):
        print(f'Loading episode no. {self.episode_select}\n')
        print(
            f'Currently playing {self.remove_special_char} {self.episode_select}/{self.episode_no}\n')

        if int(self.episode_select) == int(self.episode_no):
            print(f'[p] previous\n[s] search another anime\n[q] quit')
        elif int(self.episode_select) > 1:
            print(f'[n] next\n[p] previous\n[s] search another anime\n[q] quit')
        else:
            print(f'[n] next\n[s] search another anime\n[q] quit')
        option = input('> ')
        if option == 'p' and int(self.episode_select) == 1:
            option = 'o'
        elif option == 'n' and int(self.episode_select) == int(self.episode_no):
            option = 'o'
        return option


anime = anime()


system('cls' if name == 'nt' else 'clear')
anime.search_anime()
anime_list = anime.list_anime()
while True:
    if len(anime_list) == 0:
        system('cls' if name == 'nt' else 'clear')
        print(f'The anime name you input does not exist or try some other name or check the spelling !')
        anime.search_anime()
        anime_list = anime.list_anime()
    else:
        break

select_anime = anime.select_anime()
while True:
    try:
        if int(select_anime) > len(anime_list):
            system('cls' if name == 'nt' else 'clear')
            print(f'The number input does not exist. Try again !')
            anime.list_anime()
            select_anime = anime.select_anime()
        else:
            break
    except ValueError:
            system('cls' if name == 'nt' else 'clear')
            print(f'The character input does not exist. Try again !')
            anime.list_anime()
            select_anime = anime.select_anime()


anime.list_anime_episode_remove_special_char()
system('cls' if name == 'nt' else 'clear')
select_episode = anime.select_anime_episode()
while True:
    try:
        if select_episode:
            system('cls' if name == 'nt' else 'clear')
            print(f'Episode number out of range')
            select_episode = anime.select_anime_episode()
        else:
            break
    except:
        system('cls' if name == 'nt' else 'clear')
        print(f'Episode number out of range')
        select_episode = anime.select_anime_episode()
    

anime.search_episode()
anime.open_browser()
sleep(4)
system('cls' if name == 'nt' else 'clear')
key = anime.anime_option()

while True:
    if key == 'n':
        anime.search_episode(i=1)
        anime.open_browser()
        sleep(2)
        system('cls' if name == 'nt' else 'clear')
        key = anime.anime_option()
    elif key == 'p':
        anime.search_episode(i=-1)
        anime.open_browser()
        sleep(2)
        system('cls' if name == 'nt' else 'clear')
        key = anime.anime_option()
    elif key == 's':
        system('cls' if name == 'nt' else 'clear')
        anime.search_anime()
        anime.list_anime()
        anime.select_anime()
        anime.list_anime_episode_remove_special_char()
        anime.select_anime_episode()
        anime.search_episode()
        anime.open_browser()
        sleep(4)
        system('cls' if name == 'nt' else 'clear')
        key = anime.anime_option()
    elif key == 'q':
        break
    else:
        system('cls' if name == 'nt' else 'clear')
        print(f'Choose a vaild option')
        key = anime.anime_option()