
wordList = ['amma', 'appa', 'thambi', 'pappa', 'kuttyma', 'appa', 'amma', 'pappa', 'thambi', 'thambi', 'pappa', 'wife']

wordDict = {}

for word in wordList:
    if word not in wordDict.keys():
        wordDict[word] = 1
    else:
        wordDict[word]+=1

for key, value in wordDict.items():
    print(key + " : "+ str(value))