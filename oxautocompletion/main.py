####################################################################
#           ______________________________________
#  ________|           0xAutoCompletion           |_______
#  \       |                                      |      /
#   \      |              @0x68616469             |     /
#   /      |______________________________________|     \
#  /__________)                                (_________\
#
# A Handy Package to add Auto-Completion
#
# Github repo : https://github.com/0x68616469/oxautocompletion
#
####################################################################

import sys
from oxansi import Short as a

def complete(wordlist=[], case_sensitive=True):
    current_input = ""

    def getch():
        try:
            import termios, sys
        except:
            print(f"{a.cll}{a.bl}[{a.r}!{a.bl}] {a.r}Error: {a.rst}\"sys\" & \"termios\" needed.")

        fd = sys.stdin.fileno()
        orig = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~termios.ICANON
        new[6][termios.VMIN] = 1
        new[6][termios.VTIME] = 0
        try:
            termios.tcsetattr(fd, termios.TCSAFLUSH, new)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, orig)
            
    print(a.sc, end="")
    while True:
        print(a.rc, end="")
        print(a.cll, end="")
        
        guess = ""
        for word in wordlist:
            if case_sensitive == False:
                if word.lower().startswith(current_input.lower()):
                    guess = word
                    break
            else:
                if word.startswith(current_input):
                    guess = word
                    break
                
        print(f"{a.w}{current_input}",end="")
        print(f"{a.bl}{a.udr}{guess[len(current_input):]}{a.rst}", end="")
        
        sys.stdout.flush()
        
        try:
            keyboard_input = getch()
        except KeyboardInterrupt:
            print(f"{a.cll}{a.bl}[{a.r}!{a.bl}] {a.r}Error: {a.rst}Keyboard Interrupt.")
            sys.exit(0)

        if keyboard_input == "\n":
            print(a.rc, end="")
            print(a.cll, end="")
            if guess == "":
                return current_input
            else:
                return guess
        
        elif keyboard_input == "\177":
            current_input = current_input[:-1]

        else:
            current_input += keyboard_input