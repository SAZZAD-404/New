#-------------MAIN>MENU-------------#
import marshal,os,sys,time
os.system("clear")
#--------------------[LOGO]------------------------#
logo = (f"""\r\r\x1b[38;5;50mooo        ooooo ooooooooo.      ooooooo  ooooo 
\x1b[38;5;49m`88.       .888' `888   `Y88.     `8888    d8'  
\x1b[38;5;49m 888b     d'888   888   .d88'       Y888..8P    
\x1b[38;5;48m 8 Y88. .P  888   888ooo88P'  \x1b[1;97m\x1b[1;41mᏚᎪ𝐍Ꭼ\x1b[0m   \x1b[38;5;48m`8888'     
\x1b[38;5;47m 8  `888'   888   888`88b.          .8PY888.    
\x1b[38;5;47m 8    Y     888   888  `88b.       d8'  `888b   
\x1b[38;5;46mo8o        o888o o888o  o888o    o888o  o88888o  
\x1b[38;0;34m[\x1b[38;5;196m=\x1b[38;0;34m]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[\x1b[38;5;196m=\x1b[38;0;34m]
\x1b[38;0;34m[\x1b[38;5;196m~\x1b[38;0;34m] \x1b[38;5;46mADMIN          \x1b[38;0;34m= \x1b[38;5;46mSAZZAD ISLAM SANE
\x1b[38;0;34m[\x1b[38;5;196m~\x1b[38;0;34m] \x1b[38;5;46mFACEBOOK       \x1b[38;0;34m= \x1b[38;5;46mS A Z Z A D ツ
\x1b[38;0;34m[\x1b[38;5;196m~\x1b[38;0;34m] \x1b[38;5;46mSTATUS         \x1b[38;0;34m= \x1b[38;5;46mFILE ENCRYPTION
\x1b[38;0;34m[\x1b[38;5;196m=\x1b[38;0;34m]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[\x1b[38;5;196m=\x1b[38;0;34m]""")
def main():
        try:
                os.system("clear") 
                print (logo)
                print ('\x1b[38;0;34m[\x1b[38;5;196m~\x1b[38;0;34m] \x1b[38;5;46mEXAMPLE \x1b[38;5;196m:\x1b[38;5;46m /sdcard/mrx.py')
                print('\x1b[38;0;34m[\x1b[38;5;196m=\x1b[38;0;34m]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[\x1b[38;5;196m=\x1b[38;0;34m]')
                file = input ('\x1b[38;0;34m[\x1b[38;5;196m~\x1b[38;0;34m] \x1b[38;5;46mFILE NAME \x1b[38;5;196m:\x1b[38;5;46m')
                fileopen = open(file).read()
                a = compile(fileopen, 'dg', 'exec')
                m = marshal.dumps(a)
                s = repr(m)
                b = ('##-----------------------[ADMIN]---------------------------##\n# TOOL CREATED BY : SAZZAD ISLAM SANE\n# ENCRYPTION BY : SAZZAD MRX\n# GITHUB : https://github.com/SAZZAD-404\nimport marshal\nexec(marshal.loads(' + s +'))\n')
                c = file.replace('.py', '.py')
                d = open(c, 'w')
                d.write(b)
                d.close()
                time.sleep(8)
                os.system("clear")
                print(logo)
                print ('\x1b[38;0;34m[\x1b[38;5;196m~\x1b[38;0;34m] \x1b[38;5;46mYOUR ENCRYPTION SUCCESSFUL ')
                print ('\x1b[38;0;34m[\x1b[38;5;196m~\x1b[38;0;34m] \x1b[38;5;46mFILE SAVE IN >>',c)
                print('\x1b[38;0;34m[\x1b[38;5;196m=\x1b[38;0;34m]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[\x1b[38;5;196m=\x1b[38;0;34m]')
                time.sleep(1)
        except IOError:
                print ('\x1b[38;0;34m[\x1b[38;5;196m~\x1b[38;0;34m] \x1b[38;5;196mFILE NOT FOUND......! ')
                time.sleep(3)
                main()
main()
