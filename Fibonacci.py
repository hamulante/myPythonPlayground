# 循环的实现方法
def Fibonacci(n):
    if n==0:
        return [0]
    elif n==1:
        return [0,1]
    
    result = [0,1]
    
    for n in range(2,n):
        next = result[-1]+result[-2]
        result.append(next)
    return result

if __name__=="__main__":
    length = input("请给出序列长度")
    # length = 1, [0]
    # length = 2, [0,1]
    length = int(length)
    result = Fibonacci(length) #传进来的n是length，数组也是0开始，所以length=2，n=2，无需-1
    print(result)