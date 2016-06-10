from core.server.main import Listener
from sys import argv

def main ():
    l = Listener('', int (argv [1]), argv [2])

    from core.design.banners import show_main_banner, show_date
    show_main_banner()
    show_date ('Start')

    l.start_listen ()

if __name__ == '__main__':
    main ()