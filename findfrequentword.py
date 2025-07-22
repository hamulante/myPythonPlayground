import re #为了用re模块

def findfrequentword(sentence):

    #去掉标点
    sentence = re.sub(r'[^\w\s]', '', sentence)
 

    frequency = {}



    for i in sentence.split(' '): #以逗号为分割找出真正的数字元素;i是一个单词
        if i in frequency:
            frequency[i]=frequency[i]+1
        else:
            frequency[i]=1
    
    top_word = max(frequency, key=frequency.get)#根据value反推key
    return top_word


if __name__=='__main__':
    sentence = input("input a sentence")
    top_word=findfrequentword(sentence)
    print(top_word)