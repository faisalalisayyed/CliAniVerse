def history(name, episode):
    name, episode = name, episode

    with open('history.txt', 'a') as f:
        f.write(f'{name}-{episode}\n')


def retrieve_history():

    with open('history.txt', 'r') as f:
        history = f.read().split()
        history = list(dict.fromkeys(history))

    for index, hist in enumerate(history):
        print(f'[{index+1}] {hist}')
    print(f'[q] Quit')

    while True:
        history_episode = input('> ')

        try:
            if history_episode == 'q':
                exit()
            elif int(history_episode) == 1:
                name = history[0]
                break
            elif int(history_episode) > 1:
                try:
                    name = history[int(history_episode)-1]
                    break
                except IndexError:
                    print('Out of range...')
        except ValueError:
            print('Try "q" to quit')

    anime_name = name.replace('episode', '').replace('-', ' ').split()
    anime_epi = anime_name.pop()
    anime_name = ' '.join(anime_name)
    return anime_name, anime_epi
