from core.server.main import Listener
from core.db.payloads_db import PayloadDB
from sys import argv

from optparse import OptionParser

def main ():
    from core.design.banners import show_main_banner, show_date
    show_main_banner()

    op = OptionParser ('''
         __  __________    ____
        / / / / ____/ /   / __ \\
       / /_/ / __/ / /   / /_/ /
      / __  / /___/ /___/ ____/
     /_/ /_/_____/_____/_/

    -l or --list - show available payload-list
    ''')

    op.add_option ('-l', '--list', default=False, action='store_true', dest='is_list')
    (op, args) = op.parse_args ()

    if not op.is_list:

        l = Listener('', int (argv [1]), argv [2])
        show_date ('Start')

        l.start_listen ()
    else:
        from core.const import PAYLOAD_DB_PATH
        from core.design.colors import INFO
        from colorama import Fore, init

        init ()

        db = PayloadDB (PAYLOAD_DB_PATH)

        for i in db.get_payloads ():
            for j in i:
                if j == 'name':
                    print INFO + 'Name: ' + i [j]
                elif j == 'description':
                    print INFO + 'Description: ' + i[j]
                elif j == 'version':
                    print INFO + 'Version: ' + i[j]
                elif j == 'short':
                    print INFO + 'Use string: ' + Fore.RED + i[j] + Fore.RESET
                elif j == 'author':
                    print INFO + 'Developer: ' + i[j]

if __name__ == '__main__':
    main ()