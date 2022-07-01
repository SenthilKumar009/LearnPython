def mysplit(strng):
    #newlst = [strng.split(' ')]
    newlst = []
    start = 0

    if strng.isspace():
        return newlst

    for i in range(len(strng)):
        if strng[i] == ' ':
            space = i
            word = strng[start:space]
            newlst.append(word)
            start = space + 1
        elif i == len(strng)-1:
            space = i+1
            word = strng[start:space]
            newlst.append(word)
            #start = space + 1

    if '' in newlst:
        newlst.remove('')

    return list(newlst)

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))