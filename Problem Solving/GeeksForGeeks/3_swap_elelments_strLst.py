def swap_char(str_list, charFind, CharReplace):
    res = [word.replace(charReplace, '-').replace(charFind,CharReplace).replace('-', charFind) for word in str_list]
    return res

strLst = ['Gfg', 'is', 'best', 'for', 'Geeks']

charFind = input('Please enter the character you want to find: ')
charReplace = input('Please enter the character you want to replace: ')

print(swap_char(strLst, charFind, charReplace))

