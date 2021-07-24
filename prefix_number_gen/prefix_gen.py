import time,os,sys,random
from sys import platform
from random import randint
msg0=('''+-------------------------------------------------------+
| Name:        PhoneNumber Generator (Prefix Version) V1
| Author:      juni0r
+-------------------------------------------------------+''')
for i in msg0:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)
if platform.startswith("win"):
    os.system("cls")
numbers = input("how many numbers do you want to generate: ")
prefix = input("Enter First 5 Digits: ")
number = int(numbers)
gentype = "0123456789"
for x in range(number):
    #generatestarted1 = random.choice(gentype)
    #generatestarted2 = random.choice(gentype)
    #generatestarted3 = random.choice(gentype)
    #generatestarted4 = random.choice(gentype)
    #generatestarted5 = random.choice(gentype)
    generatestarted6 = random.choice(gentype)
    generatestarted7 = random.choice(gentype)
    generatestarted8 = random.choice(gentype)
    generatestarted9 = random.choice(gentype)
    generatestarted10 = random.choice(gentype)
    generatestarted = str(("+44"+"7""{}"+generatestarted6+generatestarted7+generatestarted8+generatestarted9+generatestarted10)).format(prefix)
    print(generatestarted)
    savenumbers = open("prefix.txt","a").write(generatestarted+"\n")