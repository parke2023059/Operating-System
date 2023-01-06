import os
import shutil
from cmd import Cmd


class Terminal(Cmd):
    
    
    def do_mkdir(self, path):
        os.mkdir(path)
        
    def do_rmdir(self, path):
        shutil.rmtree(path)
    
    
    
    def do_nf(self, path):
        os.system("echo > " + path)



    
    
    



Terminal().cmdloop()