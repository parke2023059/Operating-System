import os
import shutil



class System():
    
    
    #rename, move folder
    #make, remove, rename, move, file
    
    
    
    
    
    #make folder
    def makeFolder(path):
        os.mkdir(path)
        print(path + " Was Created ")
    
    def removeFolder(path):
        shutil.rmtree(path)
        print(path + " Was Removed ")

    def renameFolder():
        print("Currently Not Functional")    
        
    def moveFolder():
        print("Currently Not Functional")    
    
    
    
    
    
    #change directory
    def changeDirectory(path):
        os.chdir(path)
        print(os.listdir())
    
    #list directory'
    def listDirectory():
        print(os.listdir())
    
    #clear
    def clear():
        os.system('cls')
     
     
    #exit
   
