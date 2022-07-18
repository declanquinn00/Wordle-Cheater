# 5 letter word
def split(word):
    return list(word)

def wcheck(word, list):
    wlist = split(word)
    tmplist = []
    for i, letter in enumerate(wlist):
        if letter != ' ':
            tmplist = []
            for item in list:
                if item[i] == letter:
                    tmplist.append(item)
            list = tmplist
    return list

def lcheck(l, list):
    newlist = []
    for i in l:
        for word in list:
            if(l in word):
                newlist.append(word)
    return newlist


def main():
    filename = '5letterwords.txt'
    with open(filename) as f:
        list = f.read().splitlines()
    word = input('Type 5 characters ')
    if(len(word)<5):
        print('Too short')
    elif(len(word)>5):
        print('too long')
    else:
        result = wcheck(word, list)
        size = len(result)
        if(size ==0):
            print('There are no matching words')
        else:
            letters = split(input('Enter any known letters'))
            for l in letters:
                result = lcheck(l, result)
            size = len(result)
            print('There are ' + str(size) + ' possible words it could be')
            print(result)

main()

