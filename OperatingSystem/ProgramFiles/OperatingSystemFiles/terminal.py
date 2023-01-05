from cmd import Cmd
from kernel import *


class Terminal(Cmd):
    #make folder
    def do_mkdir(self, arg):
        System.makeFolder(arg)
    
    #remove folder
    def do_rmdir(self, arg):
        System.removeFolder(arg)

    #rename folder
    def do_rndir(self, blank):
        System.renameFolder()
    
    def do_mvdir(self, blank):
        System.moveFolder()
    
    
    
    
    def do_cd(self, arg):
        System.changeDirectory(arg)
    
    def do_list(self, blank):
        System.listDirectory()
    
    def do_clear(self, blank):
        System.clear()
    
    def do_exit(self, blank):
        exit()
    
Terminal().cmdloop()