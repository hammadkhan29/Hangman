import random
import sys
record = 'abcdefghijklmnopqrstuvwxyz'
score = 0
info = []
result = 0
print('-------------------------Welcome to Hangman--------------------------')
print()
def getFile():
    f = open("words.txt", "r")
    data =  f.read()
    newData = data.split()
    return newData
newData = getFile()
def display():
    while True:
        print('1)Play the game\n2)Login as admin\n3)Press 3 to exit')
        print()
        choice = input('How do you wanna proceed?')
        if choice == '1':
            global result ,info ,score
            userDetail()
            maxi = readScore()
            getWord(maxi)
            while True and result>0:
                choice = input('Wanna keep playing?..Enter y or Y:\nPress any other key to exit')
                if choice == 'y' or choice == 'Y':
                    getWord(maxi)
                    break
                else:
                    print('Exiting the game !!!\nBye Bye user !!!')
                    break        
            info.append(score)
            def writeScore(info):
                f = open('scores.txt','a')
                for data in info:
                    f.write(str(data)+',')
                f.write('\n')
                f.close()
            writeScore(info)
        elif choice == '2':
            username = input('Enter your username')
            password = input('Enter your password')
            admin(username,password)
        elif choice =='3':
            sys.exit()
        else:
            print('Enter a valid option')
            print('---------------------------------------------------------------------')
            continue
def userDetail():
    global info
    name = input('Enter name:')
    username = input('Enter username:')
    info =[name , username ]
def getWord(maxi):
    global newData
    secretWord = random.choice(newData)
    newData.remove(secretWord)
    hide(secretWord,maxi)
def readScore():
    count = -1
    track = []
    f = open('scores.txt','r')
    data = f.readlines()
    for item in data:
        item = item.split(',')
        track.append(item)
        count+=1
    size = len(track)-1
    if size > 0:
        maxi = int(track[0][2])
        for i in track:
            if maxi < int(i[2]):
                maxi = int(i[2])
        print('Highest score is ',maxi,'........')
        return maxi
    else:
        print('Highest score is 0.......')
        return 0
def hide(secretWord,maxi):
    real_word = 'test'
    secret_word = ['_']*len(real_word)
    NoOfguess = 6
    warning = 3
    vowels ='aeiou'
    record1= '''A B C D E F G H I J
K L M N O P Q R S T
    U V W X Y Z'''
    record = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        if NoOfguess > 0 and warning > 0:
            print(' '.join(secret_word))
            print()
            guess = input('Guess letter :...')
            guess = guess.lower()
            if guess not in record:
                warning -= 1
                print('Invalid guess... You have lost 1 warning')
            elif guess not in real_word:
                if guess in vowels:
                    NoOfguess -= 2
                    print('Wrong guess... You have lost 2 guess')
                else:
                    NoOfguess -= 1
                    print('Wrong guess... You have lost 1 guess')
                record = record.replace(guess,'')
            else:
                for i , letter in enumerate(real_word):
                    if letter != '_' and guess == letter :
                        secret_word[i] = letter
                        record = record.replace(guess,'')
                        guess1 = guess.upper()
                        record1 = record1.replace(guess1,' ')
            print(record1)
            print('guess',NoOfguess,'warning',warning)
            print('---------------------------------------------------------------------')
            if (''.join(secret_word)) == real_word:
                global result
                print(' '.join(secret_word))
                print('Congratulations !!! You have successfully guess the word')
                result += scoreCalculate(real_word,NoOfguess)
                if result < maxi:
                    print('Your score is:',result)
                    break
                else:
                    print('Congratulations!!!....You have set a new highscore:',result)
                    break
        else:
            print('You have runout of chances..')
            print('Secret Word:', real_word.upper())
            break
def scoreCalculate(a,b):
    global score
    count = 0
    global record
    for i in record:
        if i in a:
            count += 1
    score += b*count
    return b*count
def admin(username,password):
    if username == 'admin' and password == 'admin':
        while True:
            print('1)Add word\n2)Reset leadersboard\n3)Press 3 to exit')
            choice = input('Enter your action')
            if choice == '1':
                word= input('Enter new word')
                word= word.lower()
                f = open('words.txt','a')
                f.write(' '+str(word))
                f.close()
            elif choice == '2':
                f = open('scores.txt','w')
                f.write(' ')
                f.close
            elif choice == '3':
                break
            else:
                print('Enter a valid input')
    else:
        print('Wrong cedentials')
display()
