from colorama import Fore, init

init ()

def show_main_banner ():

    from core.server.config import get_version

    print '''
    {0}
        ______      _ _______
       / ____/   __(_) / ___/___  ______   _____  _____
      / __/ | | / / / /\__ \/ _ \/ ___/ | / / _ \/ ___/
     / /___ | |/ / / /___/ /  __/ /   | |/ /  __/ /
    /_____/ |___/_/_//____/\___/_/    |___/\___/_/

    {1}

    [{2}DEVELOPER{1}] {5}
    [{3}VERSION{1}] {6}
    [{4}CODE NAME{1}] {7}

    '''.format (Fore.RED, Fore.RESET, Fore.CYAN, Fore.GREEN, Fore.MAGENTA, get_version ()[0], get_version ()[1], get_version ()[2])

def show_date (what):

    from core.design.colors import INFO

    import datetime

    print INFO + what + ' Date: {0}, {1}'.format(str(datetime.datetime.now().date()).replace('-', '.'),
                                               str(datetime.datetime.now().time()).split('.')[0])