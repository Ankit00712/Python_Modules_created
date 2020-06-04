#/usr/bin/env python3                 
                                          #REQUIREMENT : Python version 3.5+
                                          #Best suited while working with interpretor
                                  #all the functions have prefix 'b' just to make them unique
from os import system                    #https://docs.python.org/3/library/subprocess.html
import subprocess                         #https://queirozf.com/entries/python-3-subprocess-examples
import shlex                              #to determine the correct tokenization for args




def breset():                 #restarts the python interpretor with updated library
    system('python3')        #but old loaded modules are gone : try to fix it


def bclear():                 #clear interpretor screen
    system('clear')
    
#common bash commands
#pwd = subprocess.check_output("pwd", shell=False).decode('UTF-8') #old way for : Python version 2.7 -> 3.4

pwd = subprocess.run(['pwd'], check=True, stdout=subprocess.PIPE, universal_newlines=True).stdout
env = subprocess.run(['env'], check=True, stdout=subprocess.PIPE, universal_newlines=True).stdout
ls = subprocess.run(['ls'], check=True, stdout=subprocess.PIPE, universal_newlines=True).stdout


def brun(command, play=0):              #to execute commands  . play : int value to test if user want to modifiy the output .
    command = shlex.split(command)   #converted the string into list  
    bout = subprocess.run(command, check=True, stdout=subprocess.PIPE, universal_newlines=True).stdout
    if(play==1):
        return bout  #Still piping is missing
    else:
        print(bout)
        print("{ARG : (command_to_run, int_value_1_if_want_a_output_to_play_with ) }")
    
def bhelp(tocheck):
    if(tocheck=='getsource'):
        sc = open('bash.py').read()
        print(sc)                #to get its own source code
    elif(tocheck=='all'):
        print('\nCommands => pwd, env, ls\n')
        print('Functions : breset(), bclear(), brun(), bhelp()\n')
        print('breset() => restarts the python interpretor with updated library {NO ARG REQUIRED}')
        print('bclear() => {NO ARG REQUIRED}')
        print('brun() => To execute bash commands {ARG : (command_to_run, int_value_1_if_want_a_output_to_play_with ) }')
        print('bhelp() => To get help regarding Module {arg required}')    
    else:
        print('INVALID ARGS PROVIDED')
        print("VALID ARGS : 'getsource', 'all' ")
