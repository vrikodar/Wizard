import os
import sys
from termcolor import colored
import time
import subprocess

gun = '''
 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX /
 / XXXXXX /
(________(                
 `------'   '''

map = '''                     
|     .-.
|    /   \         .-.
|   /     \       /   \       .-.     .-.     _   _
+--/-------\-----/-----\-----/---\---/---\---/-\-/-\/\/---
| /         \   /       \   /     '-'     '-'
|/   
      '''


def scan():
    print("\nEntering Scan mode..\n")
    opt = '''
    ///////////////////////////////////////////////////////////////////
    0. Scan For alive hosts on network--> x1
    1. Scan open ports on all hosts on the Network--> x2
    2. Scan For Open Ports on single Host--> x3
    //////////////////////////////////////////////////////////////////
    '''
    while True:
        print(map)
        print("\n" + opt + "\n")
        ask = input(colored("pool@scan_mode:~ ", 'red', attrs=['bold']))
        if ask == 'x1':
            sub = input("Enter the--subnet: ")
            os.system(f"nmap -sn {sub}")
        if ask == 'x2':
            sub = input("Enter the--subnet: ")
            print("\nStarting with simple scan....\n")
            try:
                command = f"nmap -sS {sub}"
                CMD = subprocess.check_output(command, shell = True)
                with open('s1.html', 'w') as file:
                    html = f'''<!DOCTYPE html>
                            <html>
                            <head>
                                <title>SIMPLE PORT SCAN REPORT</title>
                            </head>
                            <body>
                                <hr>
                                <hr>
                            <br>
                            <br>
                            <p>
                            {CMD}
                            </p>
                             '''
                    file.write(html)
                    file.close()
                # with open('s1.html', 'wb') as file:
                #     file.writelines(data)
                print(colored("\nScan results written to s1.html..\n", 'green'))
                time.sleep(2)
                print("opening scan results!")
                os.system('firefox s1.html')
            except KeyboardInterrupt:
                print("CTRL + C detected")


def working():
    print("working!!")
    time.sleep(5)
    sys.exit(0)


def options():
    opt = '''\n
    ////////////////////////////////////////////////////////////////////////
    0. Attack--> shoot
    1. SCAN THE TARGET--> scan
    2. Launch DOS attack--> dos
    3. Look For exploits--> expl

    /////////////////////////////////////////////////////////////////////////
    \n'''
    print(colored(opt, 'green'))
    while True:
        ask = input(colored("pool@SxNade:~ ", 'red', attrs=['bold']))
        if ask == 'scan':
            scan()
        elif ask == '':
            print("Enter something!")
        elif ask == 'clear':
            os.system('clear')
        elif ask == 'help':
            print("\n" + gun + "\n")
            print(colored(opt, 'green'))
        elif ask == 'exit':
            print("Exit..")
            sys.exit(0)
        else:
            print("unexpected input!")
            sys.exit(0)

def initiate():
    print(gun)
    time.sleep(1)
    print(colored("\n(v5.1) starting...\n"))
    options()


initiate()


