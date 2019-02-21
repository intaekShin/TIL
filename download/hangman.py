import random

wordlist = '''girl boy man woman truck car money mouse donkey have run jump walk wall catch note paper morning dark hill order put smell burn pet angry sad happy miss late hole child worry ugly full chew carry visit top rest water fire wood seat post latter shell kill die try easy skill far start own bake ready wait watch map wish salt use noodle area puzzle  tail puppy sand dig war hard soft coin kind fun win race poor lie hide dead way call lose net deep cry gift blow bark tear press ship sink talk think site web hit strike help hand sleep bed bad room sell earth foot one two three four five six seven eight nine ten korea japan usa china python
'''.split()
ans = []
word = []
Home = False
Rand = False
while not Home:
    if not Rand:
        Rand = True
        r = random.randint(0, 126)
        select = wordlist[r]
        h = len(select)
        wrong = 0
        del ans[::]
        del word[::]
        for i in range(h):
            ans.append('*')
            word.append(select[i])
    print("The Answer = ", ans)
    get = input()
    if get == select:
        print("Congratulations! You got the answer!")
        break
    if get in word:
        for k in range(h):
            if word[k] == get:
                ans[k] = get
        continue
    elif get not in word:
        wrong += 1
    if '*' not in ans:
        print("Congratulations! You got the answer!")
    if wrong != 0:
        if wrong == 1:
            print("0")
            continue
        elif wrong == 2:
            print("0\n|\n|")
            continue
        elif wrong == 3:
            print("  0\n /|\n/ |")
            continue
        elif wrong == 4:
            print("  0\n /|\\\n/ | \\")
            continue
        elif wrong == 5:
            print("  0\n /|\\\n/ | \\\n /\n/")
            continue
        elif wrong == 6:
            print("  0    DEAD\n /|\\\n/ | \\\n / \\\n/   \\")
            print("Oh, NO!! You Lost The Game! The answer was :", select, "!")
    Gettf = input("You wanna play again?? (y/n): ")
    Home = Gettf
    if Home == 'y' or Home == 'Y':
        Home = False
        Rand = False
        continue
    elif Home == 'n' or Home == 'N':
        Home = True
    else:
        print("Error, Saw It Coming!")

d = input()
