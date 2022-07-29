from re import sub

from .search_anime import search_anime


def select_anime(name='', flag=0):

    if flag == 1:
        select_anime.anime_name = search_anime(name=name, flag=2)
    else:
        select_anime.anime_name = search_anime()

    while True:
        if flag == 1:
            select_anime.anime_select = str(1)
            break
        else:
            select_anime.anime_select = input("> ")

        try:
            if select_anime.anime_select == 'q':
                exit()
            elif int(select_anime.anime_select) > len(select_anime.anime_name):
                print('sorry select in range....')
            else:
                break
        except ValueError:
            print('Try "q" to quit')

    return remove_special_char()


def remove_special_char():
    anime_select = select_anime.anime_name[select_anime.anime_select].split()
    episode_no = anime_select.pop()
    anime_select = ' '.join(anime_select).lower()
    remove_special_char = sub(
        '[^a-zA-Z0-9 \n\.]', '', anime_select).replace(' ', '-')

    return remove_special_char, episode_no
