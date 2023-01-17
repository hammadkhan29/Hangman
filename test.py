name = 'hammmad'
blank ='______'
for i in name:
    choose = input('enter :')
    if i == choose:
        loc = name.index(i)
        blank = blank.replace(blank[loc],choose)
    print(blank)
