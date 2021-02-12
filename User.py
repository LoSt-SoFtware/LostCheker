
import random, string
import os
import time
os.system('pkg install figlet && pkg install python')
os.system('clear')


print ('\033[92mCheking Updates')

os.system ('\033[97mrm -rif LostCheker')
os.system ('git clone https://github.com/LoSt-SoFtware/LostCheker')
time.sleep (2)

os.system ('figlet STOP')
time.sleep(9)
os.system ('clear')
print ('\033[91mTawaw Bu')
time.sleep(1)
os.system('clear')

os.system('figlet LOST')
time.sleep(4)


print("======================")
text = string.ascii_letters + string.digits

ani = int(input('Chand Pet Be : '))
print("========================")
hama = int(input('Chand User Drust kat : '))

with open('User.txt', 'a') as file:

    for x in range(hama):

        word = ''.join(random.choice(text) for x in

range(ani))

        if x == range(hama)[-1]:
            file.write(word)
        else:
            file.write(word + '\n')

    print("===========================")
    os.system('clear')
    input('=====Tawaw Bu! Enter Ka Bo Darchun!========\n')
    print("===================DoNe====================")
    os.system("clear")