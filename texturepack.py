#Installs texturepacks from downloads folder after checking for windows or linux operating systems
#Created by Graham Helton 04/22/2020
import getpass
import os
import shutil
from sys import platform
from os import listdir



def linux():
    user = getpass.getuser()
    deliveryPath = r'/home/%s/.minecraft/resourcepacks' %user
    linuxPath = r'/home/%s/Downloads/' %user
    #Enumerates ZIP files within downloads folder 
    print("Type Yes to install texturepack")
    for file in os.listdir(linuxPath):
        if file.endswith(".zip"):
            userSelection = input("Is this your texturepack?: " +str(file) + " ")
            #Asks the user if this is the correct file
            if userSelection.__contains__ ("yes"):
                linuxPath = r'/home/{0}/Downloads/{1}'.format(user,str(file))
                shutil.move(linuxPath,deliveryPath)
                break

def windows():
    user = getpass.getuser()
    windowsDeliveryPath = r'C:\users\{0}\appdata\roaming\.minecraft\resourcepacks'.format(user)
    windowsPath = r'C:\users\{0}\Downloads'.format(user)
    #Enumerates ZIP files within downloads folder 
    print("Type Yes to install texturepack")
    for file in os.listdir(windowsPath):
        if file.endswith(".zip"):
            userSelection = input("Is this your texturepack?: " +str(file) + " ")
            #Asks the user if this is the correct file
            if userSelection.__contains__ ("yes"):
                windowsPath = r'C:\users\{0}\Downloads\{1}'.format(user,str(file))
                shutil.move(windowsPath,windowsDeliveryPath)
                break


#Checks to see which operating system is currently running
if platform.__contains__("linux"):
    linux()
elif platform.__contains__("win"):
    windows()


