from colorama import Fore, init

init ()

ERR = '{0}[!] {1}'.format (Fore.RED, Fore.RESET)
YES = '{0}[+] {1}'.format (Fore.GREEN, Fore.RESET)
NO = '{0}[-] {1}'.format (Fore.RED, Fore.RESET)
INFO = '{0}[*] {1}'.format (Fore.CYAN, Fore.RESET)