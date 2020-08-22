#!/bin/python
#Autor: @ErickWhiteHat
# COLORES
Black="\033[0;30m"        
Red="\033[0;31m"          
Green="\033[0;32m"        
Yellow="\033[0;33m"      
Blue="\033[0;34m"         
Purple="\033[0;35m"       
Cyan="\033[0;36m"         
White="\033[0;37m" 
end = "\033[0m" 

# MODULOS
import subprocess
import os
import random
from optparse import OptionParser


# CLASES
class Mac:
    
    def __init__(self):
        os.system('clear')
        print(Yellow + """
             __   __  _______  _______   
            |  |_|  ||   _   ||       |  
            |       ||  |_|  ||       |  
            |       ||       ||       |  
            |       ||       ||      _|  
            | ||_|| ||   _   ||     |_   
            |_|   |_||__| |__||_______| 
        """+ end)
        
        
        
    def Parametros(self):
        self.parse = OptionParser()
        self.parse.add_option('-i',dest="interfaz",help="Interfaz de red")
        (self.opcion,self.arg) = self.parse.parse_args()

        if not self.opcion.interfaz:
            self.arg.error("Verifique la ayuda, con el comando --help")
        return self.opcion
        
    
    def GenerandoMAC(self):
        self.random = [ 0x00, 
                random.randint(0x00,0x1f), 
                random.randint(0x00,0x1f),
                random.randint(0x00, 0x7f),
	            random.randint(0x00, 0xff),
                random.randint(0x00, 0xff) ]
        self.mac = ':'.join(map(lambda x: "%02x" % x, self.random))

    
    def Cambio(self):
        self.interfaz = self.opcion.interfaz

        subprocess.run(['ifconfig',self.interfaz,'down'])
        subprocess.run(['ifconfig',self.interfaz,'hw','ether',self.mac])
        subprocess.run(['ifconfig',self.interfaz,'up'])

    
    def NuevaMAC(self):
        print(Yellow + "[i]"+ end,"Nueva MAC: ",self.mac)
        print("\n")


cambio = Mac() 
cambio.Parametros()
cambio.GenerandoMAC()
cambio.Cambio()
cambio.NuevaMAC()