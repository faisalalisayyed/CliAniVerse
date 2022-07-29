import argparse
from os import remove


def parse_arg():

    parser = argparse.ArgumentParser(
        description='CliAniVerse - To Watch and download anime'
    )

    parser.add_argument(
        '-hist',
        '--history',
        action='store_true',
        help='Use to get history of anime you have watch'
    )

    parser.add_argument(
        '-del',
        '--delete',
        action='store_true',
        help='To delete current save history'
    )

    return parser.parse_args()


def parse_action():

    args = parse_arg()

    if args.history:
        try:
            from .history import retrieve_history
            from .player_option import call_fun
            name = retrieve_history()
            call_fun(name=name[0], epi=name[1], flag=1)

        except FileNotFoundError:
            print('No history found...')
        exit()
    elif args.delete:
        try:
            remove('history.txt')
            print('Successfully remove history...')
            exit()
        except FileNotFoundError:
            print('File not found')
            exit()
