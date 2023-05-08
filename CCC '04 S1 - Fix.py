def fix(words):
    for i,word in enumerate(words):
        for j,test in enumerate(words):
            # don't test word again itself, prevent index out of bounds error
            if i == j or len(test) < len(word):
                continue
            
            # test if the start or end matches word
            length = len(word)
            if test[:length] == word or test[-length:] == word:
                return "No"
    return "Yes"


for i in range(int(input())):
    words = [input() for _ in range(3)]
    print(fix(words))

