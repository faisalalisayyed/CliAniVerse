from time import sleep
from os import system, uname

from .select_episode import select_episode, search_episode


def call_fun(name='', epi='', flag=0):
    if flag == 1:
        call_fun.select = select_episode(name=name, epi=epi, flag=1)
        call_fun.epi = search_episode()
        check_option()
    else:
        call_fun.select = select_episode()
        call_fun.epi = search_episode()
        check_option()


def player_option():
    sleep(2)
    system('cls' if uname == 'nt' else 'clear')

    print(f'Loading episode no. {call_fun.epi}')
    print(f'Currently playing {call_fun.select[0]} {call_fun.epi}/{call_fun.select[1]}\n')

    if int(call_fun.epi) == int(call_fun.select[1]):
        print(f'[p] previous\n[s] search another anime\n[q] quit')
    elif int(call_fun.epi) > 1:
        print(f'[n] next\n[p] previous\n[s] search another anime\n[q] quit')
    else:
        print(f'[n] next\n[s] search another anime\n[q] quit')
    option = input('> ')
    if option == 'p' and int(call_fun.epi) == 1:
        option = 'o'
    elif option == 'n' and int(call_fun.epi) == int(call_fun.select[1]):
        option = 'o'
    return option


def check_option():
    key = player_option()

    while True:
        if key == 'n':
            call_fun.epi = search_episode(epi_no=1)
            key = player_option()
        elif key == 'p':
            call_fun.epi = search_episode(epi_no=-1)
            key = player_option()
        elif key == 's':
            call_fun()
        elif key == 'q':
            exit()
        else:
            system('cls' if uname == 'nt' else 'clear')
            print(f'Choose a vaild option')
            key = player_option()
