from cmd import Cmd
from kernel import *


class Terminal(Cmd):
    #make folder
    def do_mkdir(self, arg):
        System.makeFolder(arg)
    
    def do_rmdir(self, arg):
        System.removeFolder(arg)

    
Terminal().cmdloop()