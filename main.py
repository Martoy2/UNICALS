import ctypes
from colorama import init, Fore


init(autoreset=True)

version="UNCIALS V0.2"

ctypes.windll.kernel32.SetConsoleTitleW(version)

f_change = open('ChangeLog.unical', 'r+')
for i in (f_change):
    if i != "   ":
        if "+" in i:
            print(Fore.GREEN + i.replace('\n', ''))
        elif "-" in i:
            print(Fore.RED + i.replace('\n', ''))
        else:
            print(i.replace('\n', ''))

a=int(input('''
Celka: 1| Akrien: 2 | : 
'''))
if a==1:
    dd='MODER:D.HELPER:HELPER:MAGISTER:BULL:TITAN:BUNNY:AVENGER:DRAGON:OVERLORD:RABBIT:HERO:IMPERATOR:TIGER:'
elif a==2:
    dd='---------| IMPERATOR |------------------| TIGER |------------------| DRAGON |------------------| OVERLORD |------------------| LUCIFER |------------------| BUNNY |------------------| MAGISTER |------------------| RABBIT |---------'

while ValueError!=None:
    try:
        f_base = open('base.txt', 'r+').readlines()
        ValueError=None
    except:
        ValueError="I don't see base.txt"
        print(ValueError)
        f_base = open('base.txt', 'w')
        f_base.close()
    try:
        f_parse = open('parse.txt').readlines()
        ValueError=None
    except:
        ValueError="I don't see parse.txt"
        print(ValueError)
        f_parse = open('parse.txt', 'w')
        f_parse.close()
print("base.txt load")
print('parse.txt load')
f_unical = open('unical.txt', 'w')
print('unical.txt created')
print("start checking")

def check(i):
    f_base = open('base.txt', 'r+').readlines()
    for g in range(len(f_base)):
        if i==f_base[g]:
            return False
    return True



def count_lines(filename='parse.txt', chunk_size=1<<13):
    with open(filename) as file:
        return sum(chunk.count('\n')
                for chunk in iter(lambda: file.read(chunk_size), ''))

unicals=0
repeated=0
left = int(count_lines())

ctypes.windll.kernel32.SetConsoleTitleW(f"{version} UNICALS: {unicals} REPEATED: {repeated} LEFT: {left}")

counter=0

for i in range(len(f_parse)):
    if f_parse[i].replace('\n', '').replace("+", '') in dd:
        f_unical.write(f_parse[i])  
        print("New Group: " + Fore.YELLOW + f_parse[i].replace("-", '').replace('\n', '').replace("+", ''))
        left-=1
    else:
        if check(f_parse[i]) == False:
            repeated+=1
            print(f_parse[i].replace("\n", '') + Fore.RED + " - REPEATE")
            ctypes.windll.kernel32.SetConsoleTitleW(f"{version} UNICALS: {unicals} REPEATED: {repeated} LEFT: {left}")
        else:
            f_base=open('base.txt', 'a')
            if counter==0:
                f_base.write("\n")
                counter+=1
            f_base.write(f_parse[i])
            f_unical.write(f_parse[i])
            print(f_parse[i].replace("\n", '') + Fore.GREEN + " - UNICAL")
            f_base.close()
            unicals+=1
            ctypes.windll.kernel32.SetConsoleTitleW(f"{version} UNICALS: {unicals} REPEATED: {repeated} LEFT: {left}")
        left-=1
        ctypes.windll.kernel32.SetConsoleTitleW(f"{version} UNICALS: {unicals} REPEATED: {repeated} LEFT: {left}")
f_unical.close()

print("Great!")

input('Press Enter for close\n')