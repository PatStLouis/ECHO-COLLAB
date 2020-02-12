import os, time, sys, random, socket, _thread, distutils

# Patrick St-Louis
#*****************************************************
def fn_clear():                                  
    """ Nettoyer le CLI """
    if self_os == 'linux':
        os.system('clear')
    if self_os == 'windows':
        os.system('cls')

def fn_printDelay(str):                                 
    """ Style de print() """
    for x in str:
        print(x, end="", flush=True)
        time.sleep(random.uniform(.01, .1))
    time.sleep(1)
#******************************************************

def fn_interface(): 
        print(r"                                                                        ")
        print(r"     ________________________________________________________________   ")
        print(r"    |                                                                |  ")
        print(r"    |         _                                                      |  ")                               
        print(r"    |       _| |_         Welcome to my machine.                     |  ")                      
        print(r"    |    )  (O_O)                We're all out of coffee.            |  ")      
        print(r"    |   (    _|_                                                     |  ")                                 
        print(r"    |  [_])_/ | \_            1. Scan                                |  ")
        print(r"    |         |               2. See results                         |  ")        
        print(r"    |        / \              3. Set payload                         |  ")      
        print(r"    |       /   \             4. Pwn                                 |  ") 
        print(r"    |                         5. Quit                                |  ")
        print(r"    |________________________________________________________________|  ") 
        choix = input('                 - ')

        return choix

#***************************************************************************

def fn_findHosts():                                     
    """ Trouver les hotes sur notre reseau """
    def fn_findSelfIP():                                
        """ Trouver sa propre adresse IP """
        s   = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        IP  = s.getsockname()[0]
        s.close()

        return IP
        
    def fn_scan():
        return os.popen(f"{nmap} -sn {ip}/24").read()

    def fn_transformScan(scan, file):                   
        """ Ecrire les resultats du scan dans un fichier .txt """
        file = open(file,"w")  
        file.write(scan)  
        file.close()

    def fn_targetDiscovery(file):               
        """ Filtrer le fichier .txt pour extraire les hotes dans un dictionnaire (IP:[Nom,MAC]) """                                                        
        lst_hosts       = []                            
        with open(file,'r') as f_open:
            for line in f_open:
                line = line.rstrip('\n')
                lst_hosts.append(line)
            f_open.close()

        lst_hostsV2     = []
        for x in range (0,len(lst_hosts)):
            if lst_hosts[x].count('MAC'):
               lst_hostsV2.append(lst_hosts[x][32:-1])
               lst_hostsV2.append(lst_hosts[x][13:30])
               lst_hostsV2.append(lst_hosts[x-2][21:])

        dct_hosts       = {}
        x = 0
        while x < len(lst_hostsV2):
            dct_hosts.update({lst_hostsV2[x+2]:[lst_hostsV2[x],lst_hostsV2[x+1]]})
            x+=3

        return dct_hosts

    

  
    ip      = fn_findSelfIP()   
    scan    = fn_scan()
    file    = r'Results\nmapResult.txt'
    
    fn_transformScan(scan, file) 

    return fn_targetDiscovery(file)

#*********************************************************


self_os = input('\n\n\n     Please enter your operating system (windows or linux)\n\n        - ')

if self_os == 'windows':
    nmap        = 'C:"\\Program Files (x86)"\\Nmap\\nmap.exe'
    putty       = 'C:"\\Program Files"\\PuTTY\\plink.exe'
    path        = '%CD%\\Payloads\\'


    
while True:
    fn_clear()
    operation = fn_interface()

    if operation   == '1':
        fn_clear()
        scanResults = fn_findHosts()

    elif operation == '2':
        fn_clear()
        cpt = 0
        for key in scanResults:
            cpt += 1
            print(f'{cpt}. >{key}    [{scanResults[key][0]}]    [{scanResults[key][1]}]')
        input('Select your target: ')
        

    elif operation == '3':
        fn_clear()
        IP          = input('Target IP  : ')
        username    = input('Username   : ')
        password    = input('Password   : ')
        payloadFile = input('Payload    : ')
        payload     = path + payloadFile + '.txt'


    elif operation == '4':  
        fn_clear()  
        if self_os == 'windows':
            os.system(f"{putty} -pw {password} {username}@{IP} < {payload}")

        elif self_os == 'linux':                            
            """ TODO """      
            #os.system(f"sshpass -p {password} ssh {username}@{dct_targets} {payload} StrictHostkey_IPChecking=no")
            pass

    elif operation == '5':
        fn_clear()
        break

    else:
        pass