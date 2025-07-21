def lettercounts(sentence):
    count={}
    letter = sentence.lower()
    print(letter) #hello world
    for i in letter:
        if i.isalpha():#是不是字母
            if i not in count:
                count[i]=1
            else:
                count[i] = count[i]+1

    print(count)
    return count  

if __name__=='__main__':
    sentence = input("Please type a sentencne.")#Hello World
    lettercounts(sentence)
    
