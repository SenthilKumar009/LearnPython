
sentance = "The quick brown fox jumps over the lazy dog"

n = 4

for word in sentance.split(" "):
    if len(word) > n:
        print(word)


